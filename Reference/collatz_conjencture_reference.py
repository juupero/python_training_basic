def get_cycle_length(n):
    """ 
    takes an integer 1 < n < 10000
    returns the number of steps it
    will take to get to 1
    by performing n // 2 if n is even
    and n * 3 + 1 if n is odd
    int -> int
    print(get_cycle_length(5)) -> 6
    print(get_cycle_length(1)) -> 1
    print(get_cycle_length(197)) -> 27
    """
    cycle_length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        cycle_length += 1

    return cycle_length


def get_cycle_length_range(start, end):
    """ 
    takes 2 integers 1 < start, end < 10000
    finds the number for which it takes
    the maximum amount of steps to get to
    1 and returns the length of that cycle

    int, int -> int
    print(get_cycle_length_range(5, 100)) -> 119
    print(get_cycle_length_range(200, 100)) -> 125
    print(get_cycle_length_range(1, 2)) -> 2
    """

    # swap 2 variables if needed
    if start > end:
        start, end = end, start
    return max(get_cycle_length(n) for n in range(start, end+1))