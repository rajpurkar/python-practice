from tqdm import tqdm


def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    # start with path of length 1
    paths = [startPos]

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

