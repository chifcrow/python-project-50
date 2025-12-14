import sys
from typing import List

import pytest

from gendiff.scripts import gendiff as cli


def _run_cli(monkeypatch: pytest.MonkeyPatch, args: List[str]) -> int:
    monkeypatch.setattr(sys, "argv", args)
    try:
        cli.main()
    except SystemExit as exc:
        return int(exc.code) if exc.code is not None else 0
    return 0


def test_cli_prints_result(monkeypatch: pytest.MonkeyPatch,
                           capsys: pytest.CaptureFixture[str]) -> None:
    args = [
        "gendiff",
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
    ]
    code = _run_cli(monkeypatch, args)
    captured = capsys.readouterr()

    assert code == 0
    assert captured.err == ""
    assert captured.out.strip().startswith("{")
    assert "follow" in captured.out


def test_cli_unknown_format(monkeypatch: pytest.MonkeyPatch,
                            capsys: pytest.CaptureFixture[str]) -> None:
    args = [
        "gendiff",
        "--format",
        "xml",
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
    ]
    code = _run_cli(monkeypatch, args)
    captured = capsys.readouterr()

    assert code == 2
    assert "Unknown format: xml" in captured.err
