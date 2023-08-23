def base64_encode(input_string):
    BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bit_str = ""
    result = ""

    # Convert input string to binary
    for char in input_string:
        binary_char = bin(ord(char))[2:].zfill(8)
        bit_str += binary_char

    # Pad binary string with zeros to make it a multiple of 6 bits
    while len(bit_str) % 6 != 0:
        bit_str += "0"

    # Convert 6-bit binary chunks to Base64 characters
    for i in range(0, len(bit_str), 6):
        chunk = bit_str[i:i+6]
        decimal_val = int(chunk, 2)
        result += BASE64_ALPHABET[decimal_val]

    # Pad result with "=" characters to make it a multiple of 4 characters
    while len(result) % 4 != 0:
        result += "="

    return result

input_string = "Hello, world!"
encoded_string = base64_encode(input_string)
print(encoded_string) # SGVsbG8sIHdvcmxkIQ==