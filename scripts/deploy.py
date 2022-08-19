import click

from ape import project
from ape.cli import NetworkBoundCommand, account_option, network_option
from ape.types import AddressType


@click.command(cls=NetworkBoundCommand)
@network_option()
@account_option()
@click.option(
    "--signer",
    default="0xfCEAdAFab14d46e20144F48824d0C09B1a03F2BC",  # Coinbase signer
    type=AddressType,
    help="The address that will be signing oracle price updates",
)
def cli(network, account, signer):
    account.deploy(project.Oracle, signer)
