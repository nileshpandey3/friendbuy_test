# import requests
#
# from data import request_payload, test_email, host_url, test_password
#
#
# def get_auth_token():
#     r = requests.post(f"{host_url}/auth", json=request_payload).json()
#     token = r["token"]
#     return token
#
#
# def get_all_users():
#     """Test to retrieve the list of all users"""
#
#     auth_token = get_auth_token()
#     headers = {
#         'accept': 'application/json',
#         'Authorization': f'{auth_token}'
#     }
#     resp = requests.get(f"{host_url}/users", headers=headers)
#     # raise error in case of an unsuccessful request
#     resp.raise_for_status()
#     json_resp = resp.json()
#     # retrieve the first user from the list of all users
#     user_email_resp = json_resp[0]["email"]
#     user_password_resp = json_resp[0]["password"]
#     assert test_email == user_email_resp, "User's email is incorrect"
#     assert test_password == user_password_resp, "User's password is incorrect"
#
#
# def get_all_users_invalid_token():
#     """test to check the api response for an invalid auth token"""
#
#     resp = requests.get(f"{host_url}/users", headers={"Authorization": 'garbage_value'})
#     # If the auth token value is not valid then we should get a 403 access forbidden error
#     assert resp.status_code == 403
#
#
# def get_all_users_empty_token():
#     """test to check the api response for empty token value"""
#
#     resp = requests.get(f"{host_url}/users", headers={"Authorization": None})
#     assert resp.status_code == 401
#
#
# def get_individual_user():
#     """test to fetch an individual user info"""
#
#     auth_token = get_auth_token()
#     headers = {
#         'accept': 'application/json',
#         'Authorization': f'{auth_token}'
#     }
#     resp = requests.get(f"{host_url}/users/0", headers=headers)
#     resp.raise_for_status()
#     json_resp = resp.json()
#     user_id_resp = json_resp[0]["id"]
#     user_group = json_resp[0]["group"]
#     assert user_id_resp == 0, "User has incorrect ID"
#     assert user_group == "non-admin", "User belongs to incorrect group"
#
#
# ## Test Run
#
# # Valid/Happy path test to assert a successful response
# get_all_users()
# # this test should fail as the GET user endpoint is accepting garbage value and still returning the correct response
# get_all_users_invalid_token()
# # this test will pass as I am asserting on the expected failure code, which is 401 [unauthorized]
# get_all_users_empty_token()
# get_individual_user()
