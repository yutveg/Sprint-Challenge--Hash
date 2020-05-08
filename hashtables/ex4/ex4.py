def has_negatives(a):

    """
    YOUR CODE HERE
    """
    look_up = {}
    for number in a:
        if number not in look_up:
            look_up[number] = 1
    result = []
    for number in a:
        if number * -1 in look_up and number > 0:
            result.append(number)
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
