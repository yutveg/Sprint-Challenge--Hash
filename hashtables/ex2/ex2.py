#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    look_up = {}
    for ticket in tickets:
        look_up[ticket.source] = ticket.destination
    
    route = []
    first_destination = look_up["NONE"]
    route.append(first_destination)
    # cur_node = first destination
    cur_node = first_destination
    while cur_node != "NONE":
        cur_node = look_up[cur_node]
        route.append(cur_node)
    
    return route
