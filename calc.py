import pygame
import collections

WHITE = (255, 255, 255)
GREY = (192, 192, 192)
BLACK = (0, 0, 0)
DGREY = (169, 169, 169)
BGREEN = (0, 106, 78)

Button = collections.namedtuple("Button", ["label", "color", "x", "y", "length", "height"])

def make_buttons():    
    length, width = 59, 49
    x1, x2, x3, x4 = 0, 59, 118, 177

    buttons = []

    buttons.append(Button('AC', BGREEN, x1, 139, length, width))
    buttons.append(Button('MYS', BGREEN, x2, 139, length, width))
    buttons.append(Button('MOD', BGREEN, x3, 139, length, width))
    buttons.append(Button('/', BGREEN, x4, 139, length, width))

    buttons.append(Button('7', GREY, x1, 188, length, width))
    buttons.append(Button('8', GREY, x2, 188, length, width))
    buttons.append(Button('9', GREY, x3, 188, length, width))
    buttons.append(Button('*', BGREEN, x4, 188, length, width))

    buttons.append(Button('4', GREY, x1, 237, length, width))
    buttons.append(Button('5', GREY, x2, 237, length, width))
    buttons.append(Button('6', GREY, x3, 237, length, width))
    buttons.append(Button('-', BGREEN, x4, 237, length, width))

    buttons.append(Button('1', GREY, x1, 286, length, width))
    buttons.append(Button('2', GREY, x2, 286, length, width))
    buttons.append(Button('3', GREY, x3, 286, length, width))
    buttons.append(Button('+', BGREEN, x4, 286, length, width))

    buttons.append(Button('0', GREY, x1, 335, length * 2, width))
    buttons.append(Button('.', GREY, x3, 335, length, width))
    buttons.append(Button('=', BGREEN, x4, 335, length, width))

    return buttons

def add_buttons(buttons):
    for button in buttons:
        pygame.draw.rect(screen, button.color, pygame.Rect(button.x, button.y, button.length, button.height))
        pygame.draw.rect(screen, BLACK, pygame.Rect(button.x, button.y, button.length, button.height), 1)
        font = pygame.font.Font(None, 25)
        functions = font.render(button.label, 1, BLACK)
        screen.blit(functions, (button.x + 10, button.y + 5))

def get_pressed_button(mx, my, buttons):
    for button in buttons:
        if button.x <= mx <= button.x + button.length and button.y <= my <= button.y + button.height:
            return button
    return None

def build_expression(expression, button):
    result = '' if expression == '0' else expression
    if button.label in ['AC', 'MYS']:
        return '0'
    elif button.label == 'MOD':
        return '0' if len(result) == 0 else result + '%'
    elif button.label == '=':
        return '0' if len(result) == 0 else str(eval(result))
    elif button.label in ['*', '/']:
        return '0' if len(result) == 0 else result + button.label
    else:
        return result + button.label

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((234, 384))
    buttons = make_buttons()
    screen.fill(BLACK)
    add_buttons(buttons)
    expression = '0'
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                button = get_pressed_button(mx, my, buttons)
                expression = build_expression(expression, button)
                print(expression)