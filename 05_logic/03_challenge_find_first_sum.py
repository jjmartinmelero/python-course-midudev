# Objetivo
# Dado un array de números y un número objetivo (goal), necesitamos encontrar los dos primeros números en el array cuya suma sea igual a ese número objetivo. Si existe tal combinación, la función debe devolver los índices de estos dos números. Si no se encuentra ninguna combinación, debe devolver None.

# example:
# nums = [4,5,6,2]
# goal = 8
# find_first_sum(nums, goal) -> [2,3]



nums = [4,5,6,2]
goal = 8

def find_first_sum(nums, goal):
    for idx, num in enumerate(nums):
        for second_num in range(len(nums) - 1):
            if((nums[(second_num + 1)] + num) == goal):
                return [idx, (second_num + 1)]

print(find_first_sum(nums, goal))