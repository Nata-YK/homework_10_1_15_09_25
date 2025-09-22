import pytest


@pytest.fixture
def card_number_list():
    return '7000792289606361'


@pytest.fixture
def card_number_mask():
    return '7000 79** **** 6361'


@pytest.fixture
def card_account_list():
    return '73654108430135874305'


@pytest.fixture
def card_account_mask():
    return '**4305'


@pytest.fixture
def card_empty():
    return " "