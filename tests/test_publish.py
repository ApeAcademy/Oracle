def test_publish_price(oracle, deployer):
    oracle.set_price(int(1500e6), sender=deployer)
    assert oracle.price() == int(1500e6)
