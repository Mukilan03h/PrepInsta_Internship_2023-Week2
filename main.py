def display_game_state(positions):
    print("[ 0 , 1 , 2 , 3 , 4 , 5 , 6 ]")
    print(positions)

def take_user_input():
    return input("Press q to quit\nEnter position of piece: ")

def check_quit_condition(pos):
    if pos == 'q':
        print("You Lose")
        return True
    return False

def convert_input_to_int(pos):
    try:
        return int(pos)
    except ValueError:
        return -1  # Invalid input

def check_valid_position(pos):
    return 0 <= pos <= 6

def check_empty_leaf(pos, positions):
    pos2 = positions.index('-')
    return pos != pos2

def check_valid_moves_for_G(pos, positions):
    if pos + 1 <= 6 and positions[pos + 1] == '-':
        return pos + 1
    elif pos + 2 <= 6 and positions[pos + 2] == '-' and positions[pos + 1] == 'B':
        return pos + 2
    else:
        return -1  # Invalid move

def check_valid_moves_for_B(pos, positions):
    if pos - 1 >= 0 and positions[pos - 1] == '-':
        return pos - 1
    elif pos - 2 >= 0 and positions[pos - 2] == '-' and positions[pos - 1] == 'G':
        return pos - 2
    else:
        return -1  # Invalid move

def make_move(pos, pos2, positions):
    positions[pos], positions[pos2] = positions[pos2], positions[pos]

def check_winning_condition(positions):
    return positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']

def main():
    positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']
    while True:
        display_game_state(positions)
        pos = take_user_input()
        if check_quit_condition(pos):
            break
        pos = convert_input_to_int(pos)
        if not check_valid_position(pos):
            print("Invalid Move")
            continue
        if not check_empty_leaf(pos, positions):
            print("Invalid Move")
            continue
        pos2 = -1
        if positions[pos] == 'G':
            pos2 = check_valid_moves_for_G(pos, positions)
        elif positions[pos] == 'B':
            pos2 = check_valid_moves_for_B(pos, positions)
        if pos2 == -1:
            print("Invalid Move")
            continue
        make_move(pos, pos2, positions)
        if check_winning_condition(positions):
            print("You Win")
            break

if __name__ == "__main__":
    main()
