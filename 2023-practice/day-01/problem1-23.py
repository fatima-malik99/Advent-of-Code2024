def find_calibration_value(line):
    # Find all digits in the line
    digits = [char for char in line if char.isdigit()]
    
    if not digits:
        return 0
    
    # Combine first and last digit
    return int(digits[0] + digits[-1])

def calculate_total_calibration(filename):
    total = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                calibration_value = find_calibration_value(line.strip())
                total += calibration_value
                
        return total
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Example usage
# if __name__ == "__main__":
filename = "input.txt"  # Replace with your input file name
result = calculate_total_calibration(filename)
    
if result is not None:
    print(f"The sum of all calibration values is: {result}")
