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
def __init__(oracle: address):
    self.oracle = oracle


@external
def set_price(
    time: uint256,
    price: uint256,
    r: uint256,
    s: uint256,
    v: uint256,
):
    """
    @notice Update the `price` that this contract stores
    @dev Only a payload signed by `self.oracle` may update the price
    @param time The time from which the price originated
    @param price The new price update
    @param r The `r` parameter of the signature signing `message` signed by `self.oracle`
    @param s The `s` parameter of the signature signing `message` signed by `self.oracle`
    @param v The `v` parameter of the signature signing `message` signed by `self.oracle`
    """
    # NOTE: If `time > block.timestamp`, this will also fail
    assert block.timestamp - time <= MAX_UPDATE_DELAY
    assert block.timestamp >= self.last_update + MAX_UPDATE_DELAY

    message: bytes32 = keccak256(_abi_encode(b"prices", time, b"ETH", price))
    message_hash: bytes32 = keccak256(concat(b"\x19Ethereum Signed Message:\n32", message))
    signer: address = ecrecover(message_hash, v, r, s)
    assert signer == self.oracle

    self.price = price
    self.last_update = block.timestamp
