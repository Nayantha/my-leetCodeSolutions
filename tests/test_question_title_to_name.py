import sys

import pytest

from question_title_to_name import main


@pytest.mark.parametrize("title, expected", [
    ("Length of Last Word", "length_of_last_word")
])
def test_main(title: str, expected: str, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: title)
    assert main() == expected
