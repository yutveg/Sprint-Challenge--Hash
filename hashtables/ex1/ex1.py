def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    look_up = {}
    for index, weight in enumerate(weights):
        print(weight, index)
        look_up[weight] = index
    
    

    for index, weight in enumerate(weights):
        print(f"limit is {limit}, weight is {weight}, need a {limit - weight}")
        if limit - weight in look_up:
            if limit - weight > weight:
                return (look_up[limit - weight], index)
            else:
                return (index, look_up[limit - weight])

            
    return None
