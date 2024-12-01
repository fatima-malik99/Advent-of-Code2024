## Solution Walkthrough - Part 1

### Calculating Total Distance
Processing each pair of sorted numbers:

1. **First Pair (Smallest Numbers)**
   - Left list: 1
   - Right list: 2
   - Calculate difference: |1 - 2| = 1
   - Running total = 1

2. **Second Pair**
   - Left list: 3
   - Right list: 4
   - Calculate difference: |3 - 4| = 1
   - Running total = 2

3. **Third Pair**
   - Left list: 5
   - Right list: 8
   - Calculate difference: |5 - 8| = 3
   - Running total = 5

### Step-by-Step Process
1. **Initial Lists**
   ```python
   left_list = [3, 1, 5]
   right_list = [4, 2, 8]
   ```

2. **After Sorting**
   ```python
   left_sorted = [1, 3, 5]
   right_sorted = [2, 4, 8]
   ```

3. **Pairing and Calculations**
   - Pair 1: |1 - 2| = 1
   - Pair 2: |3 - 4| = 1
   - Pair 3: |5 - 8| = 3

4. **Final Sum**
   ```python
   total_distance = 1 + 1 + 3 = 5
   ```

**Final Result:** 5
---
## Solution Walkthrough - Part 2
### Calculating Similarity Score for solution 2
Processing each number in `left_list`:

1. **First number (3)**
   - Count occurrences of 3 in right_list: 3 times
   - Add to score: `3 * 3 = 9`
   - Total score = 9

2. **Second number (4)**
   - Count occurrences of 4 in right_list: 1 time
   - Add to score: `4 * 1 = 4`
   - Total score = 13

3. **Third number (2)**
   - Count occurrences of 2 in right_list: 0 times
   - Add to score: `2 * 0 = 0`
   - Total score = 13

4. **Fourth number (1)**
   - Count occurrences of 1 in right_list: 0 times
   - Add to score: `1 * 0 = 0`
   - Total score = 13

5. **Fifth number (3)**
   - Count occurrences of 3 in right_list: 3 times
   - Add to score: `3 * 3 = 9`
   - Total score = 22

6. **Sixth number (3)**
   - Count occurrences of 3 in right_list: 3 times
   - Add to score: `3 * 3 = 9`
   - Total score = 31

**Final Result:** 31

Input file contains:
3 4
1 2
5 8

Step 1 - After read_input():
left_list = [3, 1, 5]
right_list = [4, 2, 8]

Step 2 - In calculate_total_distance():
1. Sort the lists:
   left_sorted = [1, 3, 5]
   right_sorted = [2, 4, 8]

2. Calculate differences:
   First pair:  |1- = 1
   Second pair: |3-4| = 1
   Third pair:  |5-8| = 3

3. Sum all differences:
   total_distance = 1 + 1 + 3 = 5

Final output:
"The total distance between the lists is: 5"

