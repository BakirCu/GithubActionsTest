from ..lambda_source.lambda_function import capital_case
import pytest

def test_capital_case():
    assert capital_case("data") == "Data"
