"""
@title A price feed oracle that publishes ETH/USD pricing information
@dev
    Prices are accurate to 6 decimal places
    (e.g. `price * eth_amount / 1e6 = usd_amount`)
"""
MAX_UPDATE_DELAY: constant(uint256) = 5 * 60  # seconds

price: public(uint256)
oracle: public(address)
last_update: public(uint256)


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

    assert block.timestamp >= self.last_update + MAX_UPDATE_DELAY

    self.price = price
    self.last_update = block.timestamp
