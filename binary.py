def parse_binary(binary):
    if not all(char in '01' for char in binary):
        raise ValueError(f"Invalid binary literal: {binary}")

    decimal = 0
    for i in range(len(binary)):
        digit = binary[-i-1]
        decimal += int(digit) * 2**i

    return decimal