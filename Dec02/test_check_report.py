import pytest
import main

def test_success():
    assert main.check_report([1, 2, 3, 4, 5]) == 1, "The report should be deemed safe"
    assert main.check_report([5, 4, 3, 2, 1]) == 1, "The report should be deemed safe"
    assert main.check_report([1, 2, 3, 4, 6]) == 1, "The report should be deemed safe"
    assert main.check_report([1, 2, 3, 4, 7]) == 1, "The report should be deemed safe"

def test_fail():
    assert main.check_report([1, 1, 3, 4, 7]) == 0, "The report should be deemed unsafe"
    assert main.check_report([1, 2, 3, 4, 8]) == 0, "The report should be deemed unsafe"
    assert main.check_report([1, 0, 3, 4, 5]) == 0, "The report should be deemed unsafe"
