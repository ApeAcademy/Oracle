"""
@title A price feed oracle that publishes ETH/USD pricing information
@dev
    Prices are accurate to 6 decimal places
    (e.g. `price * eth_amount / 1e6 = usd_amount`)
"""

price: public(uint256)
oracle: public(address)


@external
def __init__():
    self.oracle = msg.sender


@external
def set_price(price: uint256):
    """
    @notice Update the `price` that this contract stores
    @dev Only `self.oracle` may update the price
    @param price The new price update
    """
    assert msg.sender == self.oracle
    self.price = price
