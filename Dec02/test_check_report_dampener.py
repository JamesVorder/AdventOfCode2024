import pytest
import main


def test_safe_reports():
    assert main.check_report_dampener([1, 1, 2, 3]) == 1, "The report should be safe, only one violation"
    assert main.check_report_dampener([1, 2, 1, 3]) == 1, "The report should be safe, only one violation"
    assert main.check_report_dampener([1, -1, 2, 3]) == 1, "The report should be safe, only one violation"
    assert main.check_report_dampener([1, 5, 2, 3]) == 1, "The report should be safe, only one violation"

def test_unsafe_reports():
    assert main.check_report_dampener([1, 2, 3, 7, 8]) == 0, "The report should be considered unsafe."