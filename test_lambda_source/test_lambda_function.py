from ..lambda_source.lambda_function import capital_case, lambda_handler
import pytest

def test_capital_case():
    assert capital_case("data") == "Data"

def test_lambda_handler():
    responce = lambda_handler("","")
    assert responce == {
        'statusCode': 200,
        'body': '"Hello from Lambda!"',
        'data': '""'
    }