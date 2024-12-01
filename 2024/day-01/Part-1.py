# 1. First Function: Reading the Input
def read_input(file_path):
    # Create empty lists to store our numbers
    left_list = []    # Will store numbers from first column
    right_list = []   # Will store numbers from second column
    
    # Open and read the file
    # 'r' means read mode, 'file' is like a handle to read the file
    with open(file_path, 'r') as file:
        # Go through the file line by line
        for line in file:
            # For each line (e.g., "3 4"):
            # 1. strip() removes any extra spaces or newlines
            # 2. split() divides the line at the space: "3 4" becomes ["3", "4"]
            # 3. map(int, ...) converts each string to integer: ["3", "4"] becomes [3, 4]
            # 4. left, right = ... assigns the two numbers to variables
            left, right = map(int, line.strip().split())
            
            # Add these numbers to our lists
            left_list.append(left)   # Add to end of left list
            right_list.append(right) # Add to end of right list

    # After reading all lines, our lists would be:
    # left_list = [3, 1, 5]
    # right_list = [4, 2, 8]
    return left_list, right_list

# 2. Second Function: Calculating the Distance
def calculate_total_distance(left_list, right_list):
    # Sort both lists in ascending order
    # [3, 1, 5] becomes [1, 3, 5]
    # [4, 2, 8] becomes [2, 4, 8]
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    total_distance = 0  # Initialize sum to zero
    
    # zip pairs up elements from both lists:
    # [1, 3, 5] and [2, 4, 8] becomes pairs: (1,2), (3,4), (5,8)
    for left, right in zip(left_sorted, right_sorted):
        # For each pair:
        # 1. Calculate absolute difference: |left - right|
        # 2. Add it to total_distance
        distance = abs(left - right)  # abs makes negative numbers positive
        total_distance += distance    # Add to running total
    
    # After loop:
    # |1-2| + |3-4| + |5-8| = 1 + 1 + 3 = 5
    return total_distance

# 3. Main Function: Orchestrating Everything
def main():
    # Specify where our input file is located
    file_path = "d:/Fatima/AOC2024/Advent-of-Code2024/2024/day-01/input.txt"
    
    # Read the numbers from file
    left_list, right_list = read_input(file_path)
    
    # Safety check (in case reading failed)
    if left_list is None or right_list is None:
        return
    
    # Calculate the final answer
    result = calculate_total_distance(left_list, right_list)
    
    # Print the result in a nice format
    print(f"The total distance between the lists is: {result}")

# 4. Program Entry Point
# This ensures the main() function only runs if this file is run directly
if __name__ == "__main__":
    main()