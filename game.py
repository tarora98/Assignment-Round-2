import random

class Board:

    def __init__(self, snakes, ladders):
        self.board_size = 100
        self.snakes = snakes
        self.ladders = ladders
        self.players = []

    # Add Player in the Board
    def add_player(self, player):
        self.players.append(player)

    # Move Player as per the steps
    def move_player(self, player, steps):
        # Base condition to consider
        if player.position == 0 and steps != 6:
            print(f"{player.name} needs a 6 to start.")
            return # stay at same position if not fullfill requirement

        current_position = player.position
        new_position = current_position + steps
        
        # Stay at same position if exceeds board size
        if new_position > self.board_size:
            print(f"{player.name} remains at {current_position} position.")
            return

        # Give the new position if new position lands on a snake's head or ladder's start.
        new_position = self.snakes.get(new_position, new_position)
        new_position = self.ladders.get(new_position, new_position)

        # A Player can overrule another when they hop on to the same position
        for p in self.players:
            if p != player and p.position == new_position:
                p.position = 0  # Sending other player to position 0 by overuled Player
                print(f"{player.name} overruled {p.name}. {p.name} goes back to start.")

        player.position = new_position

    # Condition to check the winner 
    def has_player_won(self, player):
        return player.position == self.board_size

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0  # Start from position 0

    def roll_dice(self):
        return random.randint(1, 6)

def setup_game():
    snakes = {}
    ladders = {}

    s = int(input("Enter Number Of Snakes Required: "))
    for _ in range(s):
        head, tail = map(int, input().split())
        snakes[head] = tail

    l = int(input("Enter Number Of Ladders Required: "))
    for _ in range(l):
        start, end = map(int, input().split())
        ladders[start] = end

    p = int(input("Enter Number Of Players Required: "))
    players = [input(f"Enter name for player {_+1}: ") for _ in range(p)]

    return snakes, ladders, players

# Main Logic
def start_game():
    
    # Intialize the board
    board = Board(snakes, ladders)
    
    # Fetch the Board with Snakes, Ladder and Player
    snakes, ladders, player_names = setup_game()

    # add the player in the boards
    for name in player_names:
        player = Player(name)
        board.add_player(player)

    current_player_index = 0
    
    while True:
        
        current_player = board.players[current_player_index]
        
        input(f"{current_player.name}'s turn. Press enter to roll the dice.")
        dice_roll = current_player.roll_dice()

        print(f"{current_player.name} rolled a {dice_roll}.")
        board.move_player(current_player, dice_roll)
        print(f"{current_player.name} is now at position {current_player.position}.")
        
        # Check the condition for win 
        if board.has_player_won(current_player):
            print(f"{current_player.name} has won the game!")
            break

        current_player_index = (current_player_index + 1) % len(board.players)

if __name__ == "__main__":
    start_game()
