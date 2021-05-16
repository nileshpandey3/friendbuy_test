## Friendbuy UI+API Test Automation suite

### How to run the tests

#### Pre-reqs:
1. Install selenium by ``pip install selenium`` 
2. Install requests library by `pip install requests`
3. Install behave bdd framework by running `pip install behave`
   
#### Steps:
1. Clone or download the project and open it in a suitable IDE e.g. Pycharm
2. `cd` to the project directory and to run the entire test suite just type `behave`
3. To run specific features provide the feature filename as `behave features/friendbuy.feature`
OR `behave features/api_verification.feature`
4. To run specific scenario you can provide the line number of the scenario e.g.
`behave features/friendbuy.feature:4`
   
#### Notes:
1. If you run the entire test suite then all the test scenario will pass except one
which is as expected due to the bug in GET users api end point which accepts invalid auth token
   
