import pytest


@pytest.fixture(scope="session")
def deployer(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def reader(accounts):
    return accounts[1]


@pytest.fixture(scope="session")
def oracle(project, deployer):
    return deployer.deploy(project.Oracle)
