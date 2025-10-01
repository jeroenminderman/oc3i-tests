"""tests for example.py"""
from src.example import print_something


def test_print_something(capsys):
    test_input = "Hello, RAP!"
    print_something(test_input)
    captured = capsys.readouterr()
    assert captured.out.strip() == test_input  # nosec
