import ape

from eth_utils import to_int

def test_publish_price(chain, oracle, deployer, signer, encode_message):
    time = chain.pending_timestamp
    price = int(1500e6)
    msg = encode_message(time, price)
    sig = signer.sign_message(msg)
    oracle.set_price(time, price, to_int(sig.r), to_int(sig.s), to_int(sig.v), sender=deployer)
    assert oracle.price() == int(1500e6)

    price = int(2000e6)
    msg = encode_message(time, price)
    sig = signer.sign_message(msg)
    with ape.reverts():
        oracle.set_price(time, price, to_int(sig.r), to_int(sig.s), to_int(sig.v), sender=deployer)
   
    chain.pending_timestamp += 5 * 60
    
    time = chain.pending_timestamp
    price = int(2000e6)
    msg = encode_message(time, price)
    sig = signer.sign_message(msg)
    oracle.set_price(time, price, to_int(sig.r), to_int(sig.s), to_int(sig.v), sender=deployer)
    assert oracle.price() == int(2000e6)
