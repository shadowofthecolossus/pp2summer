nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, nums))
result2 = list(filter(lambda x: x % 2 == 0, nums))
print(result)
print(result2)