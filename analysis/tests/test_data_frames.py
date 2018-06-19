import pytest
import sys

sys.path.insert(0, '../')
import data_frame_op
import json
import pandas

from pprint import pprint

def get_test_df():
    # Funcao apenas para fins de testes
    with open('test.json') as f:
        data = json.load(f)
    return [data_frame_op.create_data_frame(data)]

def test_creation():
    df = get_test_df()
    assert type(df[0]) == pandas.core.frame.DataFrame

def test_get_domain():
    domain = 'https://www.youtube.com/watch?v=MXzKLpYTfBE'
    res = data_frame_op.get_domain(domain)
    assert res == 'https://www.youtube.com'

def test_domain_count():
    df = get_test_df()
    res = data_frame_op.domain_count(df)
    assert res['https://todoscomciro.com'] == 2