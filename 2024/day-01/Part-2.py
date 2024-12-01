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
            # 3. left, right = ... assigns the two numbers to variables
            left, right = line.strip().split()
            
            # Convert strings to integers and add to lists
            left_list.append(int(left))   # Add to end of left list
            right_list.append(int(right)) # Add to end of right list

    # After reading all lines, our lists would be:
    # left_list = [3, 4, 2, 1, 3, 3]
    # right_list = [4, 3, 5, 3, 9, 3]
    return left_list, right_list

# 2. Second Function: Calculating Similarity Score
def calculate_similarity_score(left_list, right_list):
    total_score = 0  # Initialize total score to zero
    
    # right_numbers is just another name for right_list
    right_numbers = right_list
    
    # For each number in the left list
    for num in left_list:
        # Count how many times this number appears in right list
        occurrences = right_numbers.count(num)
        
        # Multiply number by its occurrences and add to total
        total_score += num * occurrences
    
    return total_score

# 3. Main Function: Orchestrating Everything
def main():
    # Specify where our input file is located
    file_path = 'd:/Fatima/AOC2024/Advent-of-Code2024/2024/day-01/input.txt'
    
    # Read the numbers from file
    left_list, right_list = read_input(file_path)
    
    # Safety check (in case reading failed)
    if left_list is None or right_list is None:
        return
    
    # Calculate and print the similarity score
    result = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score is: {result}")

# 4. Program Entry Point
if __name__ == "__main__":
    main()