import requests
from behave import then

from features.steps.ui_data import host_url, request_payload, test_email, test_password


@then("Verify successful GET request for retrieving entire user list")
def get_all_users(context):
    """Test to retrieve the list of all users"""

    auth_token = get_auth_token(context)
    headers = {
        'accept': 'application/json',
        'Authorization': f'{auth_token}'
    }
    resp = requests.get(f"{host_url}/users", headers=headers)
    # raise error in case of an unsuccessful request
    resp.raise_for_status()
    json_resp = resp.json()
    # retrieve the first user from the list of all users
    user_email_resp = json_resp[0]["email"]
    user_password_resp = json_resp[0]["password"]
    assert test_email == user_email_resp, "User's email is incorrect"
    assert test_password == user_password_resp, "User's password is incorrect"


@then("Verify successful GET request to retrieve individual user info")
def get_individual_user(context):
    """Test to fetch an individual user info"""

    auth_token = get_auth_token(context)
    headers = {
        'accept': 'application/json',
        'Authorization': f'{auth_token}'
    }
    resp = requests.get(f"{host_url}/users/0", headers=headers)
    resp.raise_for_status()
    json_resp = resp.json()
    user_id_resp = json_resp["id"]
    user_group = json_resp["group"]
    assert user_id_resp == 0, "User has incorrect ID"
    assert user_group == "non-admin", "User belongs to incorrect group"


@then("Verify a user can successfully authenticate and receive an auth token")
def get_auth_token(context):
    r = requests.post(f"{host_url}/auth", json=request_payload).json()
    token = r["token"]
    assert token is not None
    return token


@then("Verify GET users API response for invalid auth token")
def get_all_users_invalid_token(context):
    """test to check the api response for an invalid auth token"""

    resp = requests.get(f"{host_url}/users", headers={"Authorization": 'garbage_value'})
    # If the auth token value is not valid then we should get a 403 access forbidden error
    assert resp.status_code == 403


@then("Verify GET users API response when no auth token is provided")
def get_all_users_empty_token(context):
    """test to check the api response for empty token value"""

    resp = requests.get(f"{host_url}/users", headers={"Authorization": None})
    assert resp.status_code == 401
