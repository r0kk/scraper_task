(raw_snapshots_duplicates) = (
    "com,gsmarena)/ 20001109161000 http://www.gsmarena.com:80/ text/html 200 ZEMOMKIPQWDLOZHOQ35QUUEAZ7TPACOQ 2470\n"
    "com,gsmarena)/ 20001109161000 http://www.gsmarena.com:80/ text/html 200 ZEMOMKIPQWDLOZHOQ35QUUEAZ7TPACOQ 2470\n"
    "com,gsmarena)/ 20001109161000 www.gsmarena.com:80/ text/html 200 NECWVVYFYOILUHI6725ZBMR65GHK55NQ 2674"
)


[(raw_snapshots_different_months), selected_month, raw_snapshots_expected_output] = [
    (
        "com,gsmarena)/ 20191109101000 http://www.gsmarena.com:80/ text/html 200 ZEMOMKIPQWDLOZHOQ35QUUEAZ7TPACOQ 2470\n"
        "com,gsmarena)/ 20191117161000 http://www.gsmarena.com:80/ text/html 200 ZEMOMKIPQWDLOZHOQ35QUUEAZ7TPACOQ 2470\n"
        "com,gsmarena)/ 20191209161000 http://www.gsmarena.com:80/ text/html 200 ZEMOMKIPQWDLOZHOQ35QUUEAZ7TPACOQ 2470\n"
        "com,gsmarena)/ 20190709161000 http://www.gsmarena.com:80/ text/html 200 ZEMOMKIPQWDLOZHOQ35QUUEAZ7TPACOQ 2470\n"
        "com,gsmarena)/ 20191109103000 http://www.gsmarena.com:80/ text/html 200 ZEMOMKIPQWDLOZHOQ35QUUEAZ7TPACOQ 2470\n"
        "com,gsmarena)/ 20181009161000 http://www.gsmarena.com:80/ text/html 200 ZEMOMKIPQWDLOZHOQ35QUUEAZ7TPACOQ 2470"
    ),
    "201911",
    ["20191109101000", "20191117161000", "20191109103000"]
]

snaps_url = "http://web.archive.org/web/20200101064922id_/https://www.gsmarena.com//"

snaps = [{
    "DAILY_INTEREST":
    {
        "Xiaomi Redmi Note 8 Pro": 40004,
        "Xiaomi Redmi Note 8": 31643,
        "Samsung Galaxy A51": 29802,
        "Samsung Galaxy A71": 20893,
        "Samsung Galaxy A50": 19764,
        "Xiaomi Mi Note 10 Pro": 19568,
        "Oppo Reno3 Pro": 17915,
        "Apple iPhone 11 Pro Max": 16874,
        "Samsung Galaxy A70": 16520,
        "Samsung Galaxy Note10 Lite": 16326,
    },
    "SNAP_TIME": "20200101064922",
    "STATUS_CODE": "200",
    "URL": "http://web.archive.org/web/20200101064922id_/https://www.gsmarena.com//"
}]

db_daily_table = [
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 1,
        "PHONE": "Xiaomi Redmi Note 8 Pro",
        "DAILY_HITS": 40004
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 2,
        "PHONE": "Xiaomi Redmi Note 8",
        "DAILY_HITS": 31643
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 3,
        "PHONE": "Samsung Galaxy A51",
        "DAILY_HITS": 29802
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 4,
        "PHONE": "Samsung Galaxy A71",
        "DAILY_HITS": 20893
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 5,
        "PHONE": "Samsung Galaxy A50",
        "DAILY_HITS": 19764
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 6,
        "PHONE": "Xiaomi Mi Note 10 Pro",
        "DAILY_HITS": 19568
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 7,
        "PHONE": "Oppo Reno3 Pro",
        "DAILY_HITS": 17915
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 8,
        "PHONE": "Apple iPhone 11 Pro Max",
        "DAILY_HITS": 16874
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 9,
        "PHONE": "Samsung Galaxy A70",
        "DAILY_HITS": 16520
    },
    {
        "SNAP_TIME": "2020-01-01 06:49:22",
        "RANKING": 10,
        "PHONE": "Samsung Galaxy Note10 Lite",
        "DAILY_HITS": 16326
    },
]
