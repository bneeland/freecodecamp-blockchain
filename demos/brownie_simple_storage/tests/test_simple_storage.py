from brownie import SimpleStorage, accounts

def test_deploy():
    # Step 1: Arrange
    account = accounts[0]
    # Step 2: Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Step 3: Assert
    assert starting_value == expected
