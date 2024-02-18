"""Solution for Leetcode Problem:
Number of Ways to Reach a Position After Exactly k Steps"""

from functools import cache


def number_of_ways(start_pos: int, end_pos: int, k: int) -> int:
    """
    Solving Leetcode Problem.
    https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
    Given two positive integers startPos and endPos
    Initially, you are standing at position startPos on an infinite
    number line. With one step, you can move either one position to the left,
    or one position to the right.
    Given a positive integer k, return the number of different ways to
    reach the position endPos starting from startPos, such that you
    perform exactly k steps. Since the answer may be very large, return it
    modulo 109 + 7.
    """
    MOD = 10**9+7
    # define dp[cur_pos][k] = number of ways to reach cur_pos after k steps
    # dp[cur_pos][k] = dp[cur_pos-1][k-1] + dp[cur_pos+1][k-1]
    # base case: dp[end_pos][0] = 1

    @cache
    def dp(cur_pos, k):
        if k == 0:
            return 1 if cur_pos == end_pos else 0
        return (dp(cur_pos-1, k-1) + dp(cur_pos+1, k-1)) % MOD
    return dp(start_pos, k)


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
    print(number_of_ways(1, 2, 3))


def test_number_of_ways_2():
    """
    Example 2:
    Input: startPos = 264, endPos = 198, k = 68
    Output: 1
    """
    print(number_of_ways(264, 198, 68))


if __name__ == "__main__":
    test_number_of_ways()
    test_number_of_ways_2()
