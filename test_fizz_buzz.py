from io import StringIO
from unittest.mock import patch

import pytest

from fizz_buzz import fizzbuzz


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (15, "fizzbuzz\n"),  # 正常系: 15の倍数
        (9, "fizz\n"),  # 正常系: 3の倍数
        (10, "buzz\n"),  # 正常系: 5の倍数
        (7, "7\n"),  # 正常系: その他の数値
    ],
)
def test_fizzbuzz_normal(input_value, expected_output):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        fizzbuzz(input_value)
        assert mock_stdout.getvalue() == expected_output


@pytest.mark.parametrize(
    "invalid_input",
    [
        "abc",  # 文字列
        3.14,  # 浮動小数点数
        [15],  # リスト
        None,  # NoneType
    ],
)
def test_fizzbuzz_invalid_input(invalid_input):
    with pytest.raises(ValueError, match="入力は整数でなければなりません"):
        fizzbuzz(invalid_input)
