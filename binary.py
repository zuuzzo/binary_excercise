def parse_binary(binary):
    # Check if the input is a valid binary number
    if not all(char in '01' for char in binary):
        raise ValueError("Invalid binary input")

    # Convert the binary number to decimal
    decimal = 0
    for i in range(len(binary)):
        digit = binary[-i-1]
        decimal += int(digit) * 2**i

    return decimal