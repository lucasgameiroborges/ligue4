#General imports
from turtle import title
import numpy as np
import pygame
import sys
import math

#Intern imports
import bt

#Colors
WHITE = (255,255,255)
BLUE = (0,0,255) 
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

#Board rows and columns
ROW_COUNT = 6
COLUMN_COUNT = 7

#################################################################################################################################################
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

###
 
def drop_piece(board, row, col, piece):
    board[row][col] = piece

###
 
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

###
 
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

###
 
def print_board(board):
    print(np.flip(board, 0))

###
 
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
 
    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
 
    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
 
    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

###
 
def menu():
    pass

###
 
def end_screen(player, player1_score, player2_score, screen):
    pygame.time.wait(time_win)
    screen.fill([255, 255, 255])
    screen.blit(bg_end, (0,0))

    if player == 1:
        label_title = title_font.render("Player 1 wins!", 1, RED)
    else:
        label_title = title_font.render("Player 2 wins!", 1, BLUE)

    title_rect = label_title.get_rect(center=(width/2, 50))
    screen.blit(label_title, title_rect)

    label_score = score_font.render(f"Player 1 [{player1_score}] x [{player2_score}] Player 2", 1, WHITE)
    score_rect = label_score.get_rect(center=(width/2, 0.6*height/2))
    screen.blit(label_score, score_rect)

    replay_button.draw(screen)
    menu_button.draw(screen)
    exit_button.draw(screen)

    pygame.display.update()

###
 
def center_imag(imag, coord, scale):
    if coord == 'x':
        return width/2 - scale*imag.get_width()/2
    if coord == 'y':
        return height/2 - scale*imag.get_height()/2

###
 
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
     
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c] == 1:
                screen.blit(piece_1, (int(c*SQUARESIZE+SQUARESIZE/2)-45, height-int(r*SQUARESIZE+SQUARESIZE/2)-45))
                #pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                screen.blit(piece_2, (int(c*SQUARESIZE+SQUARESIZE/2)-45, height-int(r*SQUARESIZE+SQUARESIZE/2)-45))
               #pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

#################################################################################################################################################

#Create board
board = create_board()
print_board(board)

#Constant values
time_exit = 400
time_win = 1200

#State variables
turn = 0 #rand()
player1_score = 0
player2_score = 0
repeat_game = False
game_over = False
 
#Initalize pygame
pygame.init()
 
#Define screen size
SQUARESIZE = 100
 
#Define width and height of board
width = COLUMN_COUNT*SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)

#Create Screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ligue4')

#Images
#_Pieces images
piece_1 = pygame.transform.scale(pygame.image.load('p_red.png'), (2*RADIUS, 2*RADIUS))
piece_2 = pygame.transform.scale(pygame.image.load('p_blue.png'), (2*RADIUS, 2*RADIUS))

#_Buttons images
replay_img = pygame.image.load('replay.png').convert_alpha()
menu_img = pygame.image.load('menu.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#_Background images
bg_end = pygame.image.load('bg_teste.jpg').convert_alpha()

#Calling function draw_board again
draw_board(board)
pygame.display.update()

#Buttons
#_Menu buttons

#_End screen buttons
scale_end = 0.7
replay_button = bt.Button(center_imag(replay_img, 'x', scale_end), 0.8*(4/3)*center_imag(replay_img, 'y', scale_end), replay_img, scale_end)
menu_button = bt.Button(center_imag(menu_img, 'x', scale_end), 0.9*(5/3)*center_imag(menu_img, 'y', scale_end), menu_img, scale_end)
exit_button = bt.Button(center_imag(exit_img, 'x', scale_end), 1.9*center_imag(exit_img, 'y', scale_end), exit_img, scale_end)

#Labels
#_Menu labels

#_End screen labels
title_font = pygame.font.SysFont("monospace", 30)
score_font = pygame.font.SysFont("monospace", 30)
options_font = pygame.font.SysFont("monospace", 30)

#Run Game
while not game_over:
    #menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                screen.blit(piece_1, (posx-43, 5))
            else: 
                screen.blit(piece_2, (posx-43, 5))
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if repeat_game:
                repeat_game = False
                continue
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            print(event.pos)

            # #Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
 
                    if winning_move(board, 1):
                        player1_score += 1
                        print_board(board)
                        draw_board(board)
                        end_screen(1, player1_score, player2_score, screen)

                        while not game_over:
                            pygame.event.pump()
                            if replay_button.get_pressed():
                                pygame.event.clear()
                                screen.fill(BLACK)
                                board = create_board()
                                turn = (player1_score + player2_score)%2
                                repeat_game = True
                                break
                            if menu_button.get_pressed():
                                pygame.event.clear()
                                menu()
                                print("menu")
                            if exit_button.get_pressed():
                                game_over = True                                                      

            # # Ask for Player 2 Input
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
 
                    if winning_move(board, 2):
                        player2_score += 1
                        print_board(board)
                        draw_board(board)
                        end_screen(2, player1_score, player2_score, screen)

                        while not game_over:
                            pygame.event.pump()
                            if replay_button.get_pressed():
                                pygame.event.clear()
                                screen.fill(BLACK)
                                board = create_board()
                                turn = (player1_score + player2_score)%2
                                repeat_game = True
                                break
                            if menu_button.get_pressed():
                                pygame.event.clear()
                                menu()
                                print("menu")
                            if exit_button.get_pressed():
                                game_over = True   

            if not game_over:            
                print_board(board)
                draw_board(board)
                if not repeat_game:
                    turn += 1
                    turn = turn % 2
 
            if game_over:
                pygame.time.wait(time_exit)