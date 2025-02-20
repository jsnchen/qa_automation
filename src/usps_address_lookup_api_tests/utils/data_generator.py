import random_address

def generate_random_address(state):
    """
    Generates a random address for the given state.
    
    :param state: State code (e.g., "CA", "NY")
    :return: Dictionary with address details
    """
    random_addr = random_address.real_random_address_by_state(state)
    print(state)
    print(random_addr)
    return {
        "address1": random_addr.get("address1", ""),
        "address2": random_addr.get("address2", ""),
        "city": random_addr.get("city", ""),
        "state": random_addr.get("state", ""),
        "zip": random_addr.get("postalCode", ""),
    }
