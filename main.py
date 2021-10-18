import pygame
import pygame.font

# start variables

pygame.init()

table = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

win_x = 600
win_y = 600
line_width = 10
screen = pygame.display.set_mode((win_x, win_y))
clock = pygame.time.Clock()

pygame.font.init()
my_font = pygame.font.SysFont('Aerial', 60)

x_img = pygame.image.load("X.png")
x_img = pygame.transform.scale(x_img, (128, 128))
o_img = pygame.image.load('O.png')
o_img = pygame.transform.scale(o_img, (128, 128))

players_turn = 'x'

images = [20, 215, 415,
          20, 215, 415,
          20, 215, 415]

images_true = [0, 0, 0,
               0, 0, 0,
               0, 0, 0]

winner = 0
win = False

row1_win = False
row2_win = False
row3_win = False
col1_win = False
col2_win = False
col3_win = False
diag1_win = False
diag2_win = False


def win_check():
    global winner, win
    global row1_win, row2_win, row3_win, col1_win, col2_win, col3_win, diag1_win, diag2_win
    if table[0] == table[1] == table[2] and table[0] != 0:
        winner = table[0]
        win = True
        row1_win = True
    if table[3] == table[4] == table[5] and table[3] != 0:
        winner = table[3]
        win = True
        row2_win = True
    if table[6] == table[7] == table[8] and table[6] != 0:
        winner = table[6]
        win = True
        row3_win = True
    if table[0] == table[4] == table[8] and table[0] != 0:
        winner = table[0]
        win = True
        diag1_win = True
    if table[2] == table[4] == table[6] and table[2] != 0:
        winner = table[2]
        win = True
        diag2_win = True
    if table[0] == table[3] == table[6] and table[0] != 0:
        winner = table[0]
        win = True
        col1_win = True
    if table[1] == table[4] == table[7] and table[1] != 0:
        winner = table[1]
        win = True
        col2_win = True
    if table[2] == table[5] == table[8] and table[2] != 0:
        winner = table[2]
        win = True
        col3_win = True


def draw_winning_line():
    if row1_win is True:
        pygame.draw.line(screen, (255, 0, 0), (25, 85), (575, 85), width=5)
    if row2_win is True:
        pygame.draw.line(screen, (255, 0, 0), (25, 290), (575, 290), width=5)
    if row3_win is True:
        pygame.draw.line(screen, (255, 0, 0), (25, 490), (575, 490), width=5)
    if col1_win is True:
        pygame.draw.line(screen, (255, 0, 0), (95, 25), (95, 575), width=5)
    if col2_win is True:
        pygame.draw.line(screen, (255, 0, 0), (290, 25), (290, 575), width=5)
    if col3_win is True:
        pygame.draw.line(screen, (255, 0, 0), (490, 25), (490, 575), width=5)
    if diag1_win:
        pygame.draw.line(screen, (255, 0, 0,), (30, 20), (550, 550), width=5)
    if diag2_win is True:
        pygame.draw.line(screen, (255, 0, 0,), (550, 20), (30, 550), width=5)


def mouse_ifs_and_validations():
    global players_turn
    if x <= 195 and y <= 195:
        if table[0] == 0:
            if players_turn == 'x':
                table[0] = 'x'
                players_turn = 'o'
            else:
                table[0] = 'o'
                players_turn = 'x'
    elif x <= 395 and y <= 195:
        if table[1] == 0:
            if players_turn == 'x':
                table[1] = 'x'
                players_turn = 'o'
            else:
                table[1] = 'o'
                players_turn = 'x'
    elif x <= 600 and y <= 195:
        if table[2] == 0:
            if players_turn == 'x':
                table[2] = 'x'
                players_turn = 'o'
            else:
                table[2] = 'o'
                players_turn = 'x'
    elif x <= 195 and y <= 395:
        if table[3] == 0:
            if players_turn == 'x':
                table[3] = 'x'
                players_turn = 'o'
            else:
                table[3] = 'o'
                players_turn = 'x'
    elif x <= 395 and y <= 395:
        if table[4] == 0:
            if players_turn == 'x':
                table[4] = 'x'
                players_turn = 'o'
            else:
                table[4] = 'o'
                players_turn = 'x'
    elif x <= 600 and y <= 395:
        if table[5] == 0:
            if players_turn == 'x':
                table[5] = 'x'
                players_turn = 'o'
            else:
                table[5] = 'o'
                players_turn = 'x'
    elif x <= 195 and y <= 600:
        if table[6] == 0:
            if players_turn == 'x':
                table[6] = 'x'
                players_turn = 'o'
            else:
                table[6] = 'o'
                players_turn = 'x'
    elif x <= 395 and y <= 600:
        if table[7] == 0:
            if players_turn == 'x':
                table[7] = 'x'
                players_turn = 'o'
            else:
                table[7] = 'o'
                players_turn = 'x'
    elif x <= 600 and y <= 600:
        if table[8] == 0:
            if players_turn == 'x':
                table[8] = 'x'
                players_turn = 'o'
            else:
                table[8] = 'o'
                players_turn = 'x'


def draw_lines():
    pygame.draw.line(screen, (0, 0, 0), (win_x / 3 - line_width / 2, 0), (win_x / 3 - line_width / 2, win_y),
                     line_width)
    pygame.draw.line(screen, (0, 0, 0), (win_x / 3 * 2 - line_width / 2, 0), (win_x / 3 * 2 - line_width / 2, win_y),
                     line_width)
    pygame.draw.line(screen, (0, 0, 0), (0, win_y / 3 - line_width / 2), (win_x, win_y / 3 - line_width / 2),
                     line_width)
    pygame.draw.line(screen, (0, 0, 0), (0, win_y / 3 * 2 - line_width / 2), (win_x, win_y / 3 * 2 - line_width / 2),
                     line_width)


def render():
    for i in range(0, 10):
        if i <= 2:
            images_true[i] = 1
            if table[i] == 'x':
                screen.blit(x_img, (images[i] + 10, 20))
            elif table[i] == 'o':
                screen.blit(o_img, (images[i] + 20, 20))
        elif i <= 5:
            images_true[i] = 1
            if table[i] == 'x':
                screen.blit(x_img, (images[i] + 10, 225))
            elif table[i] == 'o':
                screen.blit(o_img, (images[i] + 20, 225))
        elif i <= 8:
            images_true[i] = 1
            if table[i] == 'x':
                screen.blit(x_img, (images[i] + 10, 425))
            elif table[i] == 'o':
                screen.blit(o_img, (images[i] + 20, 425))


# while cycle
running = True
while running:
    mouse_presses = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if mouse_presses[0]:
            x, y = pygame.mouse.get_pos()
            mouse_ifs_and_validations()

    win_check()

    screen.fill((255, 255, 255))
    draw_lines()
    render()
    pygame.display.update()

    if win is True:
        draw_winning_line()
        pygame.display.update()
        pygame.time.wait(3000)
        break

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    message = my_font.render(f"{winner.upper()} wins!", False, (0, 0, 0))

    screen.fill((255, 255, 255))
    screen.blit(message, (150, 290))
    pygame.display.update()
