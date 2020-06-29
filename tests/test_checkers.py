import pytest
import validator_collection_br.checkers_br as checkers_br


@pytest.mark.parametrize('value, fails, allow_empty', [
    ('020.388.410-80', False, False),
    (2038841080, True, False),
    ('20.388.410-80', True, False),
    ('0020.388.410-80', True, False),
    ('02038841080', True, False),
    ('020.388.410-00', True, False),
    ('333.333.333-33', True, False),
    ('not-an-cpf', True, False),
    ('', True, False),
    (None, True, False),
])
def test_is_cpf(value, fails, allow_empty):
    expects = not fails
    result = checkers_br.is_cpf(value)
    assert result == expects


@pytest.mark.parametrize('value, fails, allow_empty', [
    ('33.000.167/0001-01', False, False),
    (33000167000101, True, False),
    ('33.000.167/001-01', True, False),
    ('033.000.167/0001-01', True, False),
    ('33000167000101', True, False),
    ('33.000.167/0001-02', True, False),
    ('11.111.111/1111-11', True, False),
    ('not-an-cnpj', True, False),
    ('', True, False),
    (None, True, False),
])
def test_is_cnpj(value, fails, allow_empty):
    expects = not fails
    result = checkers_br.is_cnpj(value)
    assert result == expects


@pytest.mark.parametrize('value, fails, allow_empty', [
    ('2260487-88.2018.8.26.0000', False, False),
    ('0006825-34.2019.8.26.0344', False, False),
    ('1003021-30.2017.8.26.0338', False, False),
    ('1017313-77.2019.8.26.0361', False, False),
    (22604878820188260000, True, False),
    ('1005458-57.2017.8.26.0361', True, False),
    ('0011497-26.2017.8.23.0451', True, False),
    ('1005364-92.2016.9.26.0577', True, False),
    ('1010244-95.2020.8.26.0114', True, False),
    ('1001629-45.2018.8.26.0481', True, False),
    ('1004335-98.2015.8.26.0132', True, False),
    ('0016294520188260481', True, False),
    ('00016294520188260481', True, False),
    ('not-an-cnj', True, False),
    ('', True, False),
    (None, True, False),
])
def test_is_cnj(value, fails, allow_empty):
    expects = not fails
    result = checkers_br.is_cnj(value)
    assert result == expects
