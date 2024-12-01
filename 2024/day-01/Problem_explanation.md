## Time and Space Complexity Analysis

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