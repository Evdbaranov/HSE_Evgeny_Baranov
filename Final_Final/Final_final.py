def fib(n):
    a,b = 0,1
    result = []
    for _ in range(n):
        result.append(a)
        a,n=b,a+b
    return result
print ("Фибоначчи:", fib(8))

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0
    for char in reversed(s):
        curr = roman[char]
        if curr < prev:
            res -= curr
        else:
            res += curr
        prev = curr
    return res
print (roman_to_int('III'))
print (roman_to_int ('LVIII'))
print (roman_to_int ('MCMXCIV'))

def is_monotonic(nums):
    increasing = all(x <= y for x, y in zip(nums, nums[1:]))
    decreasing = all(x >= y for x, y in zip(nums, nums[1:]))
    return increasing or decreasing

print(is_monotonic([1,2,2,3]))    # True
print(is_monotonic([6,5,4,4]))    # True
print(is_monotonic([1,3,2]))      # False