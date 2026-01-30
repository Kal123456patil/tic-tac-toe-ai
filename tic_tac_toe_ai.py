import math

HUMAN = 'X'
AI = 'O'

human_wins = 0
ai_wins = 0
draws = 0

def create_board():
    return [' ' for _ in range(9)]

def print_board(board):
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw(board):
    return ' ' not in board

def minimax(board, is_maximizing):
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = AI

print("🤖 AI-Based Tic-Tac-Toe (Minimax)")
print("You = X | AI = O")

while True:
    board = create_board()

    while True:
        print_board(board)

        # Human move
        try:
            move = int(input("Your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("❌ Enter number between 1 and 9.")
                continue
            if board[move] != ' ':
                print("❌ Cell already occupied.")
                continue
        except ValueError:
            print("❌ Enter numbers only.")
            continue

        board[move] = HUMAN

        if check_winner(board, HUMAN):
            print_board(board)
            print("🎉 You Win!")
            human_wins += 1
            break

        if is_draw(board):
            print_board(board)
            print("😐 It's a Draw!")
            draws += 1
            break

        # AI move
        ai_move(board)

        if check_winner(board, AI):
            print_board(board)
            print("🤖 AI Wins!")
            ai_wins += 1
            break

        if is_draw(board):
            print_board(board)
            print("😐 It's a Draw!")
            draws += 1
            break

    print("\n📊 Scoreboard")
    print("Human Wins:", human_wins)
    print("AI Wins:", ai_wins)
    print("Draws:", draws)

    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing 😊")
        break
