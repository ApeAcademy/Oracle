import os
from decimal import Decimal
from datetime import datetime
from coinbasepro import AuthenticatedClient as CoinbasePro
import click

from eth_utils import to_int, to_bytes

from ape import chain, project
from ape.cli import NetworkBoundCommand, account_option, network_option
from ape.types import AddressType

client = CoinbasePro(
    key=os.environ["COINBASE_API_KEY"],
    secret=os.environ["COINBASE_SECRET"],
    passphrase=os.environ["COINBASE_PASSPHRASE"],
)


def fetch_eth_price():
    signed_prices = client.get_signed_prices()
    time = int(signed_prices["timestamp"])
    price = Decimal(signed_prices["prices"]["ETH"])
    signature = to_bytes(hexstr=signed_prices["signatures"][1])
    return datetime.fromtimestamp(time), price, signature


@click.group()
def cli():
    """
    Read and publish prices to the coinbase oracle
    """


@cli.command()
def read_price() -> Decimal:
    time, price, _ = fetch_eth_price()
    print(f"[{__name__}] Current Price: {price} ({time})")


@cli.command(cls=NetworkBoundCommand)
@network_option()
@account_option()
@click.option("--address", default=None, type=AddressType)
def daemon(network, account, address):
    if address is None:
        address = project.Oracle.deployments[-1]
        click.echo(f"Publishing to Oracle contract at {address}")

    account.set_autosign(True)

    oracle = project.Oracle.at(address)
    for block in chain.blocks.poll_blocks():
        if block.timestamp - oracle.last_update() >= 5 * 60:
            signed_prices = client.get_signed_prices()
            time, price, signature = fetch_eth_price()
            time = int(time.timestamp())
            price = int(price * Decimal(1e6))
            r = to_int(signature[:32])
            s = to_int(signature[32:64])
            v = to_int(signature[64:])
            oracle.set_price(time, price, r, s, v, sender=account)
