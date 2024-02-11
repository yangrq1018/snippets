import random


def step_move_one_by_one(length, array):
    """Move top array to bottom by length times"""
    while length > 0:
        length -= 1
        array = array[1:] + array[:1]
    return array


def step_firstN_to_middle(firstN, array):
    """Put the first N items of array into a random position
    in the remaining array, the position can be the first or the last"""
    if firstN < 0 or firstN > len(array):
        raise ValueError("firstN is out of range")
    firstN_items = array[:firstN]
    remaining_array = array[firstN:]
    if len(remaining_array) > 0:
        # [0]1,[1] 2,[2] 3[3]
        random_position = random.randint(1, len(remaining_array) - 1)
    else:
        random_position = 0
    array = (
        remaining_array[:random_position]
        + firstN_items
        + remaining_array[random_position:]
    )
    return array


def magic():
    array = ["A", "B", "C", "D"]
    random.shuffle(array)
    print(f"洗牌后: {array}")
    array += array
    print(f"撕开牌: {array}")
    array = step_move_one_by_one(random.randint(2, 99), array)
    print(f"名字轮转: {array}")
    array = step_firstN_to_middle(3, array)
    print(f"前三张插中间: {array}")
    star = array[0]
    array = array[1:]
    print(f"star: {star}, array: {array}")
    # Southerners: 1, Northeners: 2, Unknown: 3
    array = step_firstN_to_middle(random.randint(1, 3), array)
    print(f"南北方: {array}")
    # Male/Female throw away top 1/2 card(s)
    array = array[random.randint(1, 2) :]
    print(f"男女: {array}")
    # length of name
    # 见证奇迹的时刻 = 7
    array = step_move_one_by_one(7, array)
    print(f"见证奇迹的时刻: {array}")
    while len(array) > 1:
        array = array[1:] + array[:1]
        print(f"好运留下来: {array}")
        array = array[1:]
        print(f"烦恼丢出去: {array}")
    print(f"star: {star}, last card: {array[0]}")


if __name__ == "__main__":
    magic()
