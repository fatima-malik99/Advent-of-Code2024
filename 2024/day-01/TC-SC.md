
---
## Time and Space Complexity Analysis- Part 1

### Overall Program Complexity

#### Time Complexity: O(n log n)
- `read_input()`: O(n)
- `calculate_total_distance()`: O(n log n)
- The bottleneck is the sorting operation

#### Space Complexity: O(n)
- Input lists: O(n)
- Sorted lists: O(n)
- Total space needed is proportional to input size

### Detailed Analysis with Example (n = 1000 lines)

#### Time Complexity Breakdown
1. **Reading Input - O(n)**
   - Reads 1000 lines
   - Each line operation (strip, split, append) is O(1)
   - Total: ~1000 operations

2. **Calculating Distance - O(n log n)**
   - Sorting 1000 numbers: ~10,000 operations (1000 * log₂1000)
   - Looping through 1000 pairs: 1000 operations
   - Total: ~11,000 operations

#### Space Complexity Breakdown
1. **Original Lists**
   - `left_list`: 1000 numbers
   - `right_list`: 1000 numbers

2. **Sorted Lists**
   - `left_sorted`: 1000 numbers
   - `right_sorted`: 1000 numbers

**Total Space**: ~4000 number storage slots

---

## Time and Space Complexity Analysis- Part 2

### Overall Program Complexity

#### Time Complexity: O(n²)
- `read_input()`: O(n)
- `calculate_similarity_score()`: O(n²)
- The bottleneck is the counting operation in the right list

#### Space Complexity: O(n)
- Input lists: O(n)
- No additional significant space needed
- Total space proportional to input size

### Detailed Analysis with Example (n = 1000 lines)

#### Time Complexity Breakdown
1. **Reading Input - O(n)**
   - Reads 1000 lines
   - Each line operation (strip, split, append) is O(1)
   - Total: ~1000 operations

2. **Calculating Similarity Score - O(n²)**
   - For each number in left list (1000 iterations):
     - Count occurrences in right list (1000 operations)
   - Total: 1000 * 1000 = 1,000,000 operations
   - Example:
     - First number: 1000 comparisons
     - Second number: 1000 comparisons
     - And so on...

#### Space Complexity Breakdown
1. **Input Storage**
   - `left_list`: 1000 numbers
   - `right_list`: 1000 numbers
   - Total: 2000 number storage slots

2. **Additional Variables**
   - `total_score`: 1 number
   - Temporary variables: Constant space
   - Total: O(1) extra space

**Total Space**: ~2000 number storage slots

### Optimization Notes
1. **Time Efficiency**
   - Current implementation: O(n²)
   - Could be improved to O(n) using a frequency dictionary
   - Trade-off: Slightly more space for much better time

2. **Space Efficiency**
   - Current implementation: O(n)
   - Already optimal for the required operations
   - Minimal additional memory usage


