file = open("input.txt", "r")

total = 0

for line in file:
    line = line.strip()

    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
                last_digit = char
            else:
                last_digit = char

    line_value = int(first_digit + last_digit)

    print(f"{line}: {line_value}")
    total += line_value

print(f"\nTotal: {total}")