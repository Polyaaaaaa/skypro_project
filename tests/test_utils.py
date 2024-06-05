import json
import os
from unittest.mock import Mock, patch

from pandas import DataFrame

from src.utils import get_csv_file_as_DataFrame, get_list_of_transactions, get_xlsx_file_as_DataFrame


@patch("builtins.open", create=True)
def test_get_list_of_transactions(mock_open: Mock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_list_of_transactions(os.path.join("..", "data", "operations.json")) == [{"test": "test"}]
    mock_open.assert_called_once_with(os.path.join("..", "data", "operations.json"), "r", encoding="utf-8")


def test_get_sum_transactions() -> None:
    mock_random = Mock(return_value=351.383168)
    assert mock_random() == 351.383168


@patch("pandas.read_excel")
def test_get_xlsx_file_as_DataFrame(mock_read_excel: Mock) -> None:
    mock_read_excel.return_value = DataFrame({"key": ["value"]})
    assert get_xlsx_file_as_DataFrame("test.xlsx") == {"key": {0: "value"}}


@patch("pandas.read_csv")
def test_get_csv_file_as_DataFrame(mock_read_excel: Mock) -> None:
    mock_read_excel.return_value = DataFrame({"key": ["value"]})
    assert get_csv_file_as_DataFrame("test.csv") == {"key": {0: "value"}}
