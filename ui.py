import pygame, sys


COLORS = {
        "NAVY":(3, 0, 28),
        "DARKEST_BLUE":(48, 30, 103),
        "MEDIUM_BLUE":(91, 143, 185),
        "LIGHT_BLUE":(182, 234, 218)
        } #Access the color dictionary by calling COLORS["Your color"]


def draw_bg(WIN, bg_color:tuple, win_width:int, win_height:int):
    pygame.draw.rect(surface=WIN, color=bg_color, rect=(0, 0, win_width, win_height))


def draw_button(WIN, button_color:tuple, button_x:int, button_y:int, button_width:int, button_height:int, button_border:int=0, button_border_radius:int=-1):
    pygame.draw.rect(surface=WIN, color=button_color, rect=(button_x, button_y, button_width, button_height), width=button_border, border_radius=button_border_radius)

def write_ui_text(WIN, font, text, color:tuple, text_x:int, text_y:int): #It will display the text in the center
    text = str(text)
    #(0, 0, 0) is black, to make black text
    text = font.render(text, True, color)

    #get the rect of the text
    text_rect = text.get_rect()

    #set the position of the text
    text_rect.center = (text_x, text_y)
    #add text to window
    WIN.blit(text, text_rect)


