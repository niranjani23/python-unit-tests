#!/usr/bin/env python
import pytest
import requests

@pytest.fixture(autouse=True)
def response():
    return requests.get("http://127.0.0.1:5000/provider/api/items")


def test_get_items_check_status_code():
    response = requests.get("http://127.0.0.1:5000/provider/api/items")
    assert response.status_code == 200


def test_get_first_item():
    response = requests.get("http://127.0.0.1:5000/provider/api/items")
    response_body = response.json()
    assert response_body["items"][0]["name"] == "Strawberries"


def test_get_len_of_items():
    response = requests.get("http://127.0.0.1:5000/provider/api/items")
    response_body = response.json()
    assert len(response_body["items"]) == 2


# Creating a data driven test
test_data_items = [
    (3,"Parsimmons",5.0,"Grocery"),
    (4,"Apples",8.2,"Grocery"),
    (5,"Beans",5.5,"Grocery"),
    (6,"Oranges",3.5,"Grocery")
]

@pytest.mark.parametrize("item_id,name,price,expected_type",test_data_items)
def test_using_data_object_get_price(item_id,name,price,expected_type):
    response = requests.get("http://127.0.0.1:5000/provider/api/items")
    response_body = response.json()
    print (response_body)
    assert response_body["items"][0]["type"] == expected_type
    #assert response_body["items"][0]["name"] == "Strawberries"
