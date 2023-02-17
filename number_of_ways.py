from tqdm import tqdm


def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    """
    Solving Leetcode Problem.
    https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
    
    Given two positive integers startPos and endPos
    Initially, you are standing at position startPos on an infinite
    number line. With one step, you can move either one position to the left,
    or one position to the right.
    
    Given a positive integer k, return the number of different ways to
    reach the position endPos starting from startPos, such that you
    perform exactly k steps.
    """
    # start with path of length 1
    paths = [[startPos]]

    # loop k times
    for i in tqdm(range(k)):
        for path in paths:
            new_path = path.copy()
            last_position = new_path[-1]

            # exist fast if not going to make to end
            if endPos - last_position > (k - i - 1):
                continue
            # path that goes to the left
            new_path_left = new_path + [last_position - 1]

            # path that goes to the right
            new_path_right = new_path + [last_position - 1]

            # add paths to the left and right
            paths.append(new_path_left)
            paths.append(new_path_right)

    num_ways = 0
    for path in paths:
        if path[-1] == endPos:
            new_ways += 1
    return num_ways


def test_number_of_ways():
    """
    Example 1:

    Input: startPos = 1, endPos = 2, k = 3
    Output: 3
    Explanation: We can reach position 2 from 1 in exactly 3 steps
    in three ways:
    - 1 -> 2 -> 3 -> 2.
    - 1 -> 2 -> 1 -> 2.
    - 1 -> 0 -> 1 -> 2.
    It can be proven that no other way is possible, so we return 3.
    """
    print(numberOfWays(1, 2, 3))

if __name__ == "__main__":
    test_number_of_ways()
