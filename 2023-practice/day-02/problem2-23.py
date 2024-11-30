def parse_game(line):
    # Split into game ID and sets
    game_part, sets_part = line.split(': ')
    game_id = int(game_part.split(' ')[1])
    
    # Process each set
    sets = sets_part.strip().split('; ')
    max_colors = {'red': 0, 'green': 0, 'blue': 0}
    
    for set_info in sets:
        # Process each color count in the set
        colors = set_info.split(', ')
        for color_info in colors:
            count, color = color_info.split(' ')
            count = int(count)
            max_colors[color] = max(max_colors[color], count)
    
    return game_id, max_colors

def is_game_possible(max_colors, limits):
    return (max_colors['red'] <= limits['red'] and 
            max_colors['green'] <= limits['green'] and 
            max_colors['blue'] <= limits['blue'])

def solve_cube_game(filename):
    # Define the cube limits
    limits = {'red': 12, 'green': 13, 'blue': 14}
    possible_games_sum = 0
    
    with open(filename, 'r') as file:
        for line in file:
            game_id, max_colors = parse_game(line.strip())
            if is_game_possible(max_colors, limits):
                possible_games_sum += game_id
    
    return possible_games_sum

# Example usage
filename = 'input2.txt'
result = solve_cube_game(filename)
print(f"Sum of possible game IDs: {result}")
