def collatz_bottom_up(n):
    """
    The Collatz Conjecture is one of the most famous unsolved puzzles in mathemmatics.

    The conjecture states that the following two operations, on any number positive integer,
    will eventually produce the number 1:

    OP1: If the number is even, divide by two
    OP2: If the number is odd, multiple by 3 and add 1.

    ex1. For the number 4:
    f(4)= 2 -> f(2)=1, which satisfy the condition
    ex2. For the number 5:
    f(5)=15+1 -> f(16)=8 -> f(4) -> ... -> 1, which also satisfies the condition.

    We call the sequence of operations above a "Collatz Sequence".

    Using bottom-up Dynamic Programming, determine the length of the longest Collatz Sequence
    out of all numbers 0 through n.

    :param n: The upper limit for the Collatz sequence
    :return: The length of the longest Collatz sequence for a number in the range 1 to n (included)
    :rtype: int
    """

    # create list n+1, as division will always be higher than 0
    length = [0] * (n+1)
    # set the base case
    length[1] = 1

    # for each number after the base case
    for i in range(2, n+1):
        current = i
        counter = 0

        while True:

            # if number lower than i, we get it from the lenght list
            if current < i:
                counter += length[current]
                break

            # else we continiue to transform it
            if current % 2 == 0:
                current = current // 2

            else:
                current = (current * 3) + 1
            counter += 1

        # save the lenght of the current number
        length[i] = counter

    return max(length)
