def decode(message_file):
    # Step 1: Read lines from the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Step 2 & 3: Parse lines and store pairs in a dictionary
    pairs = {}
    for line in lines:
        number, word = line.strip().split()
        pairs[int(number)] = word

    # Step 4: Traverse the pyramid structure and reconstruct the message
    message = ''
    current_number = 1  # Start with the smallest number
    while current_number in pairs:
        message += pairs[current_number] + ' '
        current_number += 1

    return message.strip()  # Remove trailing whitespace


# Example usage:
message_file = 'path_to_your_file.txt'  # Replace with the path to your .txt file
print(decode(message_file))