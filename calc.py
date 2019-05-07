import pygame
import collections

pygame.init()
WHITE = (255, 255, 255)
GREY = (192, 192, 192)
BLACK = (0, 0, 0)
DGREY = (169, 169, 169)
BGREEN = (0, 106, 78)

Button = collections.namedtuple("Button", ["label", "color", "x", "y", "length", "height"])

def make_buttons():
    buttons = {}
    
    length, width = 59, 49
    x1, x2, x3, x4 = 2, 61, 120, 179

    buttons['AC'] = Button('AC', BGREEN, x1, 139, length, width)
    buttons['MYS'] = Button('MYS', BGREEN, x2, 139, length, width)
    buttons['√'] = Button('√', BGREEN, x3, 139, length, width)
    buttons['÷'] = Button('÷', BGREEN, x4, 139, length, width)

    buttons['7'] = Button('7', GREY, x1, 188, length, width)
    buttons['8'] = Button('8', GREY, x2, 188, length, width)
    buttons['9'] = Button('9', GREY, x3, 188, length, width)
    buttons['x'] = Button('x', BGREEN, x4, 188, length, width)

    buttons['4'] = Button('4', GREY, x1, 237, length, width)
    buttons['5'] = Button('5', GREY, x2, 237, length, width)
    buttons['6'] = Button('6', GREY, x3, 237, length, width)
    buttons['-'] = Button('-', BGREEN, x4, 237, length, width)

    buttons['1'] = Button('1', GREY, x1, 286, length, width)
    buttons['2'] = Button('2', GREY, x2, 286, length, width)
    buttons['3'] = Button('3', GREY, x3, 286, length, width)
    buttons['+'] = Button('+', BGREEN, x4, 286, length, width)

    buttons['0'] = Button('0', GREY, x1, 335, length * 2, width)
    buttons['.'] = Button('.', GREY, x3, 335, length, width)
    buttons['='] = Button('=', BGREEN, x4, 335, length, width)

    return buttons

def add_buttons(buttons):
    for button in buttons.values():
        pygame.draw.rect(screen, button.color, pygame.Rect(button.x, button.y, button.length, button.height))
        pygame.draw.rect(screen, BLACK, pygame.Rect(button.x, button.y, button.length, button.height), 1)

if __name__ == "__main__":
    screen = pygame.display.set_mode((234, 384))
    buttons = make_buttons()

    while True:
        screen.fill(BLACK)
        add_buttons(buttons)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()