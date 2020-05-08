import itertools

def intersection(arrays):

    """
    YOUR CODE HERE
    """
    
    result = []
    # convert lists to dictionaries for instant look up 

    for index, arr in enumerate(arrays):
        arrays[index] = {i : 1 for i in arr}
    
    # iterate through each array
    for arr in arrays:
        # iterate through each number of array
        for num in arr:
            # set flag initialize index
            contains = True
            i = 0

            # create while loop to iterate through with flag = contains
            while contains and i < len(arrays):
                if num not in arrays[i]:
                    contains = False
                # if we've checked the last array
                elif i + 1 == len(arrays):
                    if num not in result:
                        result.append(num)

                i += 1
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
