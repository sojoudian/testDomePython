def find_uniqe_numbers(numbers):
    counts = {}
    for n in numbers:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    return [n for n, c in counts.items() if c == 1]    
    

if __name__ == '__main__':
    print(find_uniqe_numbers([1, 2, 1, 3]))

#print(find_uniqe_numbers(([1, 2, 3, 1]))
