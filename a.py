from turtle import right
from typing import DefaultDict
from tqdm import tqdm

def numberOfWays3(startPos: int, endPos: int, k: int, cache: dict = None) -> int:
    if cache is None:
        cache = {}
    if k == 0:
        if startPos == endPos:
            return 1
        return 0
    dist = endPos - startPos
    if dist > k:
        return 0
    if dist in cache and k in cache[dist]:
        return cache[dist][k]
    left_ways = numberOfWays3(startPos-1, endPos, k -1, cache)
    right_ways = numberOfWays3(startPos+1, endPos, k -1, cache)
    ways = left_ways + right_ways
    if dist not in cache:
       cache[dist] = {}
    cache[dist][k] = ways
    return left_ways + right_ways


def numberOfWays2(startPos: int, endPos: int, k: int) -> int:
    if k == 0:
        if startPos == endPos:
            return 1
        return 0
    if endPos - startPos > k:
        return 0
    return (
        numberOfWays2(startPos-1, endPos, k -1)
        #numberOfWays2(startPos+1, endPos, k -1)
        + numberOfWays2(startPos+1, endPos, k -1)
    )

def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    #paths = [startPos]
    paths = [[startPos]]
    for i in tqdm(range(k)):
        #for path in paths:
            # new_path = path.copy()
            # last_position = new_path[-1]
            # new_path_left = new_path + [last_position - 1]
            # new_path_right = new_path + [last_position - 1]
            # paths.append(new_path_left)
            # paths.append(new_path_right)
        for j in range(len(paths)):
            path = paths.pop(0)
            last_position = path[-1]
            # better error
            # if endPos - last_position > (k - i - 1):
            #     continue
            # if last_position - endPos > (k - i):
            #     continue
            if endPos - last_position > (k - i):
                continue
            new_path_left = path + [last_position - 1]
            new_path_right = path + [last_position + 1]
            paths.append(new_path_left)
            paths.append(new_path_right)
    num_ways = 0
    for path in paths:
        if path[-1] == endPos:
            #new_ways += 1
            num_ways += 1
    return num_ways
#print(numberOfWays2(startPos=1, endPos=2, k=3))
#print(numberOfWays2(startPos = 2, endPos = 5, k = 10))
# print(numberOfWays(startPos=2, endPos=5, k=10))


print(numberOfWays3(startPos=264, endPos=198, k=68, cache={}))
198
264
198
68