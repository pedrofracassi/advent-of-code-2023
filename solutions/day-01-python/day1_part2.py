file = open("input.txt", "r")

total = 0

digits = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

for line in file:
    line = line.strip()

    first_digit = None
    first_digit_index = None
    last_digit = None
    last_digit_index = None

    for i, char in enumerate(line):
        if char.isdigit():
            if first_digit is None:
                first_digit = char
                first_digit_index = i
                last_digit = char
                last_digit_index = i
            else:
                last_digit = char
                last_digit_index = i

    for i, digit in enumerate(digits):
        # https://www.geeksforgeeks.org/python-all-occurrences-of-substring-in-string/
        ocurrences = [i for i in range(len(line)) if line.startswith(digit, i)]

        for ocurrence in ocurrences:
            if ocurrence < first_digit_index:
                first_digit = str(i)
                first_digit_index = ocurrence
            elif ocurrence > last_digit_index:
                last_digit = str(i)
                last_digit_index = ocurrence

    line_value = int(first_digit + last_digit)

    print(f"{line}: {first_digit} + {last_digit} = {line_value}")
    total += line_value

print(f"\nTotal: {total}")