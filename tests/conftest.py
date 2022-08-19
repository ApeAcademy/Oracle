import pytest

from eth_abi import encode
from eth_account.messages import encode_defunct
from eth_utils import keccak


@pytest.fixture(scope="session")
def deployer(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def reader(accounts):
    return accounts[1]


@pytest.fixture(scope="session")
def signer(accounts):
    return accounts[2]


@pytest.fixture(scope="session")
def encode_message():
    def encode_message(timestamp, price):
        return encode_defunct(
            keccak(
                encode(
                    ["string", "uint64", "string", "uint64"],
                    ["prices", timestamp, "ETH", price],
                )
            )
        )
    return encode_message


@pytest.fixture(scope="session")
def oracle(project, deployer, signer):
    return deployer.deploy(project.Oracle, signer)
