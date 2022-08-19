import ape


def test_publish_price(oracle, deployer, reader):
    with ape.reverts():
        oracle.set_price(int(1500e6), sender=reader)
    
    oracle.set_price(int(1500e6), sender=deployer)
    assert oracle.price() == int(1500e6)
