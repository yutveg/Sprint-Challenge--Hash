def finder(files, queries):

    """
    YOUR CODE HERE
    """
    result = []
    look_up = {}
    for path in queries:
        look_up[path] = 1
    
    for fullpath in files:
        new_tuple = tuple(fullpath.split('/'))
        if new_tuple[-1] in look_up:
            result.append('/'.join(new_tuple))

    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
