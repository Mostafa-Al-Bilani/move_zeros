"""a fucntion that moves 0s to the end of the list and maintains the order of the other elements"""
numbers = [1, 2, 3, 4, 0, 0, 6, 0, 7, 0, 10, 123, 0, 12]
def move_zeros(numbers):
    counter = 0
    i = 0
    while i < len(numbers):
        if numbers[i] == 0:
            counter += 1
            numbers.pop(i)
        else:
            i += 1

    numbers.extend([0] * counter)
    return numbers
print(move_zeros(numbers))
