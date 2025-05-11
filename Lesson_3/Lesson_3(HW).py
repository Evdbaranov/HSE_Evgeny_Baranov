import math

from Lesson_3.lesson_2_data import courts

n = int(input())
def factorial (n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
print (factorial)

def max_of_three (numbers):
    if len(numbers) !=3:
        raise ValueError ("Так не пойдет")
    max_num = numbers[0]
    i=1
    while i<3:
        if numbers [i] > max_num:
            max_num = numbers
        i += 1
        return max_num
def triangle_area (a,b):
    return 0.5 * a * b

from lesson_2_data import courts

a = 0

for i in courts:
    print(courts['court_name'])