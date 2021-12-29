from brownie import SimpleStorage, accounts

def test_deploy():
    # Step 1: Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Step 2: Act
    starting_value = simple_storage.retrieve()
    expected = 0
    # Step 3: Assert
    assert starting_value == expected

def test_updating_storage():
    # Step 1: Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Step 2: Act
    expected = 15
    simple_storage.store(expected, {"from": account})
    # Step 3: Assert
    assert expected == simple_storage.retrieve()
