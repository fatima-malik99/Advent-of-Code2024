def get_calibration_value(line):
    # Dictionary to map spelled numbers to digits
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    digits = []
    
    # Iterate through each position in the line
    for i in range(len(line)):
        # Check if current character is a digit
        if line[i].isdigit():
            digits.append(line[i])
        else:
            # Check for spelled-out numbers starting at current position
            for word, digit in number_map.items():
                if line[i:].startswith(word):
                    digits.append(digit)
    
    # Return first and last digit combined
    if digits:
        return int(digits[0] + digits[-1])
    return 0

def solve_calibration(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            value = get_calibration_value(line)
            total += value
    return total

# Example usage
filename = 'input1-2.txt'
result = solve_calibration(filename)
print(f"Sum of calibration values: {result}")
