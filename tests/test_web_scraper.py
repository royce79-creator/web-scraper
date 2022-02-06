from web_scraper.web_scraper import get_citations_needed_report, get_citations_needed_count
import pytest

def test_count():
    url = 'https://en.wikipedia.org/wiki/Cuthwulf_(son_of_Cuthwine)'
    actual = get_citations_needed_count(url)
    expected = 3
    assert actual == expected

def test_count_incorrect():
    url = 'https://en.wikipedia.org/wiki/Cuthwulf_(son_of_Cuthwine)'
    actual = get_citations_needed_count(url)
    expected = 7
    assert actual != expected

def test_report():
    url = 'https://en.wikipedia.org/wiki/Cuthwulf_(son_of_Cuthwine)'
    actual = get_citations_needed_report(url).split('\n')[0] == "The date of the move is unclear, although if it was before 614 then Cuthwulf would have been the West Saxon commander at the Battle of Beandun mentioned above. This seems likely.[citation needed]"
    assert actual == True

def test_report_incorrectly():
    url = 'https://en.wikipedia.org/wiki/Cuthwulf_(son_of_Cuthwine)'
    actual = get_citations_needed_report(url).split('\n')[1] == "It is known that Cuthwulf married a Dumnonian princess Gwynhafar[citation needed]"
    assert actual == False
