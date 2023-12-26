def fibonacci_sequence(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return "Fibonacci sequence upto " + str(n) + " term: 0"
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_term = sequence[i-1] + sequence[i-2]
            sequence.append(next_term)
        return "Fibonacci sequence upto " + str(n) + " terms: " + str(sequence)

n = int(input("Enter the number of terms you want in the sequence: "))
print(fibonacci_sequence(n))
