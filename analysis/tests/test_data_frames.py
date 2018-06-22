import sys
import json
import pandas
sys.path.insert(0, '../')
import data_frame_op

def get_test_df():
    # Funcao apenas para fins de testes
    with open('test.json') as file:
        data = json.load(file)
    return [data_frame_op.create_data_frame(data)]

def test_creation():
    data_frame = get_test_df()
    assert isinstance(data_frame[0], pandas.core.frame.DataFrame)

def test_get_domain():
    domain = 'https://www.youtube.com/watch?v=MXzKLpYTfBE'
    res = data_frame_op.get_domain(domain)
    assert res == 'https://www.youtube.com'

def test_domain_count():
    data_frame = get_test_df()
    res = data_frame_op.domain_count(data_frame)
    assert res['https://todoscomciro.com'] == 2
