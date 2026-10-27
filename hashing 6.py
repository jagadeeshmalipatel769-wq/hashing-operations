def two_sum(nums, target):
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)

    return None


nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

print(f"Pair found: {result[0]} + {result[1]} = {target}")