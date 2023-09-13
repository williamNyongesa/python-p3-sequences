def print_fibonacci(length):
    sequence = []
    if length > 0 and length < 2:
        sequence.append(0)
    if length > 1  and length < 3:
        sequence.append(1)

    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence  # Return the complete sequence


result = print_fibonacci(9)
print(result)