def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    look_up = {}
    for index, weight in enumerate(weights):
        look_up[weight] = index
    
    

    for index, weight in enumerate(weights):
        if limit - weight in look_up:
            if index < look_up[limit - weight]:
                print((look_up[limit - weight], index))
                return (look_up[limit - weight], index)
            else:
                print((index, look_up[limit - weight]))
                return (index, look_up[limit - weight])

            
    return None
