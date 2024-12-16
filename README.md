Testing standards guide : 

 

Required tests: 

Unit tests: unit testing and component testing 

Integration tests: interaction between component testings 

Required test coverage: 

Required test coverage is minimum 80% of code base. why? 

We apply the Pareto Principle which states that 80% of all bugs can be found in 20% of program modules.  

Mocking: 

Use a shared directory which contains a BaseMock abstract class that is implement for each specific mock that we will need during our testing 

Don’t define mocks in test files, better use a specific file to define it 

Use unittest mocker to mock some method behaviour or responses. 

Use Mocks data file to centrelize all mocked data. 

Test dependencies: 

Testing dependency: 

-pytest	 

Mocks: 

-pytest-mock 

Coverage: 

-pytest-coverage 

Test configuration: 

Tests configurations are defined and reed from config.json file (the one which is on the project root directory) 

 

 

 

 

 

 

 

 

 

Pytest configuration: 

Pytest configurations is defined and reed from pytest.ini file (the one which is on the project root directory) 

Here is a base config: 

[pytest] 

minversion = 8.0 

addopts = --strict-markers –disable-warnings –v 

testpaths = tests 

python_files = */*_test.py 

python_classes = Tests* 

#Exclude enums/ exception/ dataclasses definition 

python_functions = test_* 

markers = 

Slow: marks tests as slow (deselect with ‘-m “not slow”’) 

Integration: marks integration tests 

log_cli = true 

log_cli_level = INFO 

log_cli_format = %(asctime)s [%(levelname)s] 

log_cli_data_format = %Y-%m-%d %H:%M:%S  

 

Test files naming pattern: 

-we should use this pattern of naming for test files: <module_or_feature> _test.py 

module_or_feature: Includes name of the module, component, or feature being tested 

Example: if you’re testing user_auth.py, the test file could be user_auth_test.py 

 

 

Test methods naming pattern: 

-we should use this pattern of naming for test methods: test_<UnitOfWork>_<Scenario>_<ExpectedOutCome> 

 

UnitOfWork: The specific function, method or behavior being tested. 

Example: create_user, authenticate, process_payment 

 

Scenario: The condition or situation under which the test is executed 

Example: with_valid_data, with_invalid_credentials, when_payment_fails 

 

ExpectedOutCome: The expected result or behavior 

Example: returns_success, raises_error, sends_notification 

Example of testing a shopping cart: 

test_add_item_to_cart_with_valid_date_returns_updated_cart 

test_remove_item_from_cart_when_item_exists_returns_success 

test_checkout_with_empty_cart_raises_error 

For edge cases we can explicitly detail the edge case in the <Scenario> like: *_edge_case_<describe_edge_case> _* 

For different params type we can resume the <Scenario> with key words like : *_with_valid_params_* 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Test fixture naming pattern [To discuss]: 

Mock fixtures: mock_<mockSubject> 

mockSubject can be : 

- A specific method name that is mocked 

- A specific scenario  

- A specific class or vendor class 

For example: 

Mock_get_users_with_valid_data	 

#Import directly defined data samples from data_mocks.py 

Tools fixture: <ToolName> 

ToolName : the name of the tool that we will use as a fixture. 

For example:  

Client 

Mocker 

Logger 

Db_connection 

... 

 

 

Don’t test exception definition file, dataclass difinition, 

 

 

Test directory layout: 

-Test/ 

- conftest.py : contain all needed mock and data fixtures for tests  

-mocks /: contain the abstract class for mocking data 

-base_mock.py: Base mock class ( will be inherited in other conftest.py )  

-unit_test /: contain all the functions/components tests 

-components_dir_1/: The dir which contain components can be services, repo, 	m		anagers, controllers, ... 

-component_1/ 

conftest.py : contain all needed mock and data fixtures for tests 			(optional) 

Mock_data.py: contain the needed data mocks for the component			    (optional) 

test_component1.py : testing file  

-component_2/ 

conftest.py : contain all needed mock and data fixtures for tests 			(optional) 

Mock_data.py: contain the needed data mocks for the component 			(optional) 

test_component2.py : testing file  

 

-integrations_test/: contain all the integration tests 

 

-integration1/ 

conftest.py : contain all needed mock and data fixtures for tests (optional) 

Mock_data.py: contain the needed data mocks for the component (optional) 

Test_integration1.py 

-integration2/ 

conftest.py : contain all needed mock and data fixtures for tests (optional) 

Mock_data.py: contain the needed data mocks for the component (optional) 

Test_integration2.py 

Pour les fixtures partagées entre les diff. Module on ajoute un repertoire /shared ?  

 

 

 

 

 

 

Unit test: 

[To be completed] 

Characteristics: 

[To be completed] 

Mocking: 

[To be completed] 

 

 

Integration test: 

Integration test are a level of software testing where individual modules or components of a system are combined and tested as a group. The goal of integration testing is to validate the interactions and interfaces between different components to ensure they work together as intended. 

 

 

Characteristics: 

 

Focus on component interactions: The aim is to check that the modules or systems communicate properly with each others, with a correct data flow and interactions. 

Covers end-to-end scenarios: Often tests end-to-end functionality involving multiple components, APIs, databases or external services 

Involves Real or Mocked Dependencies: Often use mocked/stubbed versions to simulate those interaction ( like databases or APIs) 

Mocking: 

Third part system: 

-We should mock all other third part systems(APIs, Auth) responses with request_mock fixtures for example. 

-Avoid mock patching function that can be naturally called when testing the integration	 

 

 

 

 

Database mocking [To be studied in the future]: 

-Use an in-memory data base ? No 

-Use a throwable docker container with the database images that lunches when we perform tests ?  

-Use a real database for test purpose only ? 

Test driven devolpment: 

[To be completed] 

Red Green Refactor methodologie:  

Red: [To be completed] 

Green: [To be completed] 

Refactor: [To be completed] 

 

Test debugger configuration: 

With vscode:  

[To be completed] 

With pycharm: 

 [To be completed] 

 

 

 

 

 

 

 

 

 
