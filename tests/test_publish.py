import ape


def test_publish_price(chain, oracle, deployer, reader):
    with ape.reverts():
        oracle.set_price(int(1500e6), sender=reader)
    
    oracle.set_price(int(1500e6), sender=deployer)
    assert oracle.price() == int(1500e6)


    with ape.reverts():
        oracle.set_price(int(2000e6), sender=deployer)
   
    chain.pending_timestamp += 5 * 60
    oracle.set_price(int(2000e6), sender=deployer)
    assert oracle.price() == int(2000e6)
