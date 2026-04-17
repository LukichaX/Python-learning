def count_greater(numbers, x):
    count = 0
    for n in numbers:
        if n > x:
            count += 1

    return count

print(count_greater([1, 2, 3, 4, 5], 2))