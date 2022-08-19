import click

from ape import project
from ape.cli import NetworkBoundCommand, account_option, network_option


@click.command(cls=NetworkBoundCommand)
@network_option()
@account_option()
def cli(network, account):
    account.deploy(project.Oracle)
