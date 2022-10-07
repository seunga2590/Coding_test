def solution(numbers):
    new_numbers = list(range(10))
    data = []
    
    for i in numbers:
        new_numbers.remove(i)
    
    return sum(new_numbers)