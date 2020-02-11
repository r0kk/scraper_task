import time
import html.parser
import json
import logging
import re
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

import db


logging.basicConfig(level=logging.INFO)

WEBSITE = "gsmarena.com"
URL = "http://web.archive.org/cdx/search/cdx?url={}".format(WEBSITE)


def extract_snapshots(r_text, select_month=None):
    lines = re.split("\n", r_text)
    lines = [
        line for line in lines
        if len(line) > 99
        and re.search(" 200 ", line)
        and re.search(WEBSITE, line)
        and re.search("[0-9]{14}", line)
    ]
    snaps = []
    for line in lines:
        l_split = re.split(" ", line)
        snaps.append(
            {
                "SNAP_TIME": l_split[1],
                "STATUS_CODE": l_split[4],
                "URL": "http://web.archive.org/web/{}id_/{}/".format(l_split[1], l_split[2])
            }
        )
    snaps = [s for s in snaps if s["STATUS_CODE"] == "200"]
    snaps = list({s["SNAP_TIME"]: s for s in snaps}.values())
    if select_month:
        snaps = [s for s in snaps if re.findall(select_month + "[0-9]{2}", s["SNAP_TIME"])]
    return snaps


def hits_table(r_text):
    soup = BeautifulSoup(r_text, 'html.parser')
    page_table = soup.findAll("table", {"class": "module-fit green"})
    phones = [phone.text for phone in page_table[0].find_all("nobr")]
    daily_hits = [
        int(re.sub(",", "", freq.text)) for
        freq in page_table[0].find_all("td", {"headers": "th3c"})
    ]
    table = {p: daily_hits[i] for i, p in enumerate(phones)}
    return table


def db_prepare_snaps(snaps):
    """ Prepare daily hits phones table for writing to db
    """
    db_snaps = []
    for s in snaps:
        time_units = [s["SNAP_TIME"][:4]] + [s["SNAP_TIME"][i:i + 2] for i in range(4, 13, 2)]
        dt_format = "{}-{}-{} {}:{}:{}".format(*time_units)
        phones_rank = [
            {
                "SNAP_TIME": dt_format,
                "RANKING": rank + 1,
                "PHONE": phone,
                "DAILY_HITS": daily_hits
            } for rank, (phone, daily_hits) in enumerate(s["DAILY_INTEREST"].items())
        ]
        db_snaps += phones_rank
    return db_snaps


def main():
    r = requests.get(URL)
    snaps = extract_snapshots(r_text=r.text, select_month="202001")
    for snap in snaps:
        r = requests.get(snap["URL"])
        snap["DAILY_INTEREST"] = hits_table(r.text)
    db_snaps = db_prepare_snaps(snaps)
    db.write_to_db(db_snaps)


if __name__ == "__main__":
    main()
