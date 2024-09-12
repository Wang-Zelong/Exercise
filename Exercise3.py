import random

# Define grid size
grid_size = 5

# Randomly generate player and treasure locations
player_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
treasure_position = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

# Calculate initial distance
def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

initial_distance = calculate_distance(player_position, treasure_position)
max_moves = 10
moves_count = 0

while moves_count < max_moves:
    print(f"Your current location: {player_position}, Remaining number of moves: {max_moves - moves_count}")
    move = input("Please enter your direction of movement (N, S, E, W): ").upper()

    if move not in ['N', 'S', 'E', 'W']:
        print("Illegal input, please enter N, S, E or W.")
        continue

    # Update player location
    new_position = list(player_position)
    if move == 'N':
        new_position[1] += 1
    elif move == 'S':
        new_position[1] -= 1
    elif move == 'E':
        new_position[0] += 1
    elif move == 'W':
        new_position[0] -= 1

    # Check if the new location is within the grid
    if not (0 <= new_position[0] < grid_size and 0 <= new_position[1] < grid_size):
        print("Cannot leave the grid range")
        continue  # Do not reduce the number of moves

    player_position = tuple(new_position)  # 更新玩家位置
    moves_count += 1
    current_distance = calculate_distance(player_position, treasure_position)

    if player_position == treasure_position:
        print("Congratulations on finding the treasure!")
        break
    else:
        # Provide the relative location of the treasure
        if player_position[0] > treasure_position[0]:
            east_west = "west"
        elif player_position[0] < treasure_position[0]:
            east_west = "east"
        else:
            east_west = "same vertical line"

        if player_position[1] > treasure_position[1]:
            north_south = "south"
        elif player_position[1] < treasure_position[1]:
            north_south = "north"
        else:
            north_south = "same horizontal line"

        print(f"The treasure is yours {east_west} and {north_south}.")

    if moves_count == max_moves:
        print("You can no longer move, the game is over. The location of the treasure is:", treasure_position)
        break