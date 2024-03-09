import censoror
import pytest
import spacy
import en_core_web_trf

nlp = en_core_web_trf.load()

# Generate all test cases using parametrize

# Name and Date Test Variable
test_data1 = [("Mon, 7 May 2001", "███████████████")]

# Phone Number Test Variable
test_data2 = [("My phone number is 123-456-7890", "My phone number is ████████████")]

# Address Test Variable
test_data3 = [("123 Main St", "██████████")]


@pytest.mark.parametrize("input, expected", test_data1)
def test_censor_names_and_dates(input, expected):
    assert censoror.censor_names_and_dates(input, True, True)[0] == expected


@pytest.mark.parametrize("input, expected", test_data2)
def test_censor_phone_numbers(input, expected):
    assert censoror.censor_phone_numbers(input)[0] == expected


@pytest.mark.parametrize("input, expected", test_data3)
def test_censor_addresses(input, expected):
    assert censoror.censor_addresses(input)[0] == expected
