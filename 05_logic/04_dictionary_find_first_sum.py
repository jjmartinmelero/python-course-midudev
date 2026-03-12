

# same 03 exercise - now with dictionary
nums = [4, 5, 6, 2]
goal = 8


def find_first_sum(nums, goal):
    seen = {}  # dictionary to save the number and the index

    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen:
            return [seen[missing], index]

        seen[value] = index  # save the actual number
        print(f"index: {index} - {value}")

    return None


print(find_first_sum(nums, goal))
