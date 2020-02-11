import pytest
import requests

import scraper
import prepared_data


@pytest.mark.parametrize(
    "r_text",
    [prepared_data.raw_snapshots_duplicates]
)
def test_removing_redundant_snapshots(r_text):
    snaps = scraper.extract_snapshots(r_text)
    assert len(snaps) == 1


@pytest.mark.parametrize(
    "r_text, select_month, expected",
    [(
        prepared_data.raw_snapshots_different_months,
        prepared_data.selected_month,
        prepared_data.raw_snapshots_expected_output
    )],
)
def test_select_snapshots_by_month(r_text, select_month, expected):
    snaps = scraper.extract_snapshots(r_text, select_month)
    for i in range(0, len(expected)):
        snaps[i]["SNAP_TIME"] == expected[i]


@pytest.mark.parametrize(
    "r_text, expected",
    [(
        requests.get(prepared_data.snaps_url).text,
        prepared_data.snaps[0]["DAILY_INTEREST"]
    )],
)
class TestDailyHitsTable:

    @pytest.fixture(autouse=True)
    def _daily_interest_table(self, r_text):
        self._daily_interest_table = scraper.hits_table(r_text)

    def test_daily_list_hits(self, expected):
        for phone, hits in expected.items():
            assert hits == self._daily_interest_table[phone]

    def test_daily_list_phone_order(self, expected):
        assert list(expected.keys()) == list(self._daily_interest_table.keys())


@pytest.mark.parametrize(
    "snaps, expected",
    [(prepared_data.snaps, prepared_data.db_daily_table)]
)
def test_db_snapshots_data_preparation(snaps, expected):
    db_daily_table = scraper.db_prepare_snaps(snaps)
    for i in range(len(expected)):
        for key in expected[i]:
            assert db_daily_table[i][key] == expected[i][key]
