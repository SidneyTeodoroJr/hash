# Definindo as constantes do jogo
X = "X"
O = "O"
EMPTY = " "
TIE = "Empate"
NUM_SQUARES = 9

# Função para exibir o tabuleiro
def display_board(board):
    print("\n\t", board[0], " | ", board[1], " | ", board[2])
    print("\t", "---------")
    print("\n\t", board[3], " | ", board[4], " | ", board[5])
    print("\t", "---------")
    print("\n\t", board[6], " | ", board[7], " | ", board[8], "\n")

# Função para validar a jogada
def ask_move(board, player):
    move = None
    while move not in range(NUM_SQUARES):
        move = int(input(f"{player}, faça sua jogada (0-8): "))
        if board[move] != EMPTY:
            move = None
            print("Posição ocupada, tente novamente.")
    return move

# Função para definir quem começa jogando
def who_goes_first():
    import random
    if random.randint(0, 1) == 0:
        return "Computador"
    else:
        return "Jogador"

# Função para criar um novo tabuleiro
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

# Função para atualizar o tabuleiro com a jogada
def make_move(board, move, player):
    board[move] = player

# Função para definir o vencedor
def check_winner(board):
    # Verificando as linhas
    for i in (0, 3, 6):
        if board[i] == board[i+1] == board[i+2] != EMPTY:
            winner = board[i]
            return winner
    # Verificando as colunas
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != EMPTY:
            winner = board[i]
            return winner
    # Verificando as diagonais
    if board[0] == board[4] == board[8] != EMPTY:
        winner = board[0]
        return winner
    if board[2] == board[4] == board[6] != EMPTY:
        winner = board[2]
        return winner
    # Verificando empate
    if EMPTY not in board:
        return TIE
    # Caso contrário, o jogo ainda não acabou
    return None

# Função principal do jogo
def main():
    print("Bem-vindo ao jogo da velha!\n")
    players = [X, O]
    turn = who_goes_first()
    print("O " + turn + " começa jogando.\n")
    board = new_board()
    display_board(board)
    while not check_winner(board):
        player = players[0] if turn == "Jogador" else players[1]
        move = ask_move(board, player)
        make_move(board, move, player)
        display_board(board)
        turn = "Jogador" if turn == "Computador" else "Computador"
    winner = check_winner(board)
    if winner == TIE:
        print("Empate!")
    else:
        print("Parabéns, " + winner + "! Você venceu o jogo.")
        print("Obrigado por jogar!")

# Iniciando o jogo
if __name__ == "__main__":
    main()
