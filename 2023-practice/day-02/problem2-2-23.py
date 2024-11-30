def parse_game(line):
    # Split into game ID and sets
    game_part, sets_part = line.split(': ')
    game_id = int(game_part.split(' ')[1])
    
    # Process each set
    sets = sets_part.strip().split('; ')
    min_required = {'red': 0, 'green': 0, 'blue': 0}
    
    for set_info in sets:
        # Process each color count in the set
        colors = set_info.split(', ')
        for color_info in colors:
            count, color = color_info.split(' ')
            count = int(count)
            # Keep track of maximum seen for each color (which becomes minimum required)
            min_required[color] = max(min_required[color], count)
    
    return game_id, min_required

def calculate_power(cubes):
    return cubes['red'] * cubes['green'] * cubes['blue']

def solve_cube_power(filename):
    total_power = 0
    
    with open(filename, 'r') as file:
        for line in file:
            _, min_required = parse_game(line.strip())
            power = calculate_power(min_required)
            total_power += power
    
    return total_power

# Example usage
filename = 'input2.txt'
result = solve_cube_power(filename)
print(f"Sum of powers: {result}")
