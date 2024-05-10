import pygame, sys
from pygame.locals import QUIT

import playsound
import threading
import os

import ui
import countdown
import play_sound

pygame.init()

WIDTH, HEIGHT = 500, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Eye-saver')

def set_font(font_type:str="Segoe-UI", font_size:int=24):
    font = pygame.font.SysFont(font_type, font_size)
    return font

times_up_sound_file_name = os.path.join("sound", "times_up.mp3")
bell_chime_sound_file_name = os.path.join("sound", "bell_chime.mp3")

file_repeat_count = 0




time_info_file = "time_count.txt"


def read_file(out_info_1, out_info_2, out_info_3):
    with open(time_info_file, "r") as file:
        out_info_1 = int(file.readline())
        out_info_2 = int(file.readline())
        out_info_3 = int(file.readline())
        file.close()
    return (out_info_1, out_info_2, out_info_3)
def write_file(lst):
    with open(time_info_file, "w") as file:
        file.write('\n'.join(lst))
        file.close()



line_1 = None
line_2 = None
line_3 = None

list_in = []


thread = None
time_status = "Type in your time to start!"

def countdown_restart(hrs:int, mins:int, secs:int, times_up:str, thread, file_repeat_count):
    hrs, mins, secs = read_file(out_info_1=hrs, out_info_2=mins, out_info_3=secs)
    file_repeat_count = 0
    if (times_up == "Times up!" or times_up =="Type in your time to start!"):
        times_up = "You still have time"
    
    thread = threading.Thread(target=countdown.cdown, args=(hrs, mins, secs))
    thread.start()
    print(f"There are {threading.active_count()} threads running currently.")

    return times_up, hrs, mins, secs, file_repeat_count



text_color = ui.COLORS["LIGHT_BLUE"]
passive_color = ui.COLORS["DARKEST_BLUE"]
active_color = ui.COLORS["MEDIUM_BLUE"]
bg_color = ui.COLORS["NAVY"]

if (line_1 and line_2 and line_3) != None:
    preset_time = f"{line_1}:{line_2}:{line_3}"
else:
    preset_time = "0:30:0"

control_box_info = {"button_color_passive":passive_color, "button_color_active":active_color, "button_x":(WIDTH*0.025), "button_y":(HEIGHT*0.66), "button_width":(WIDTH*0.45), "button_height":(HEIGHT*0.2), "button_border":5, "button_border_radius":10, "text":"START", "text_color":text_color, "text_x":(WIDTH*0.25), "text_y":(HEIGHT*0.76)}
input_box_info = {"box_color_passive":passive_color, "box_color_active":active_color, "box_x":(WIDTH*0.525), "box_y":(HEIGHT*0.66), "box_width":(WIDTH*0.45), "box_height":(HEIGHT*0.2), "box_border":None, "box_border_radius":10, "text":preset_time, "text_color":text_color, "text_x":(WIDTH*0.75), "text_y":(HEIGHT*0.76)}



user_input_text = input_box_info["text"]
input_box_click_active = False




FPS = 60
while True:
    control_button_click_active = False
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if (event.type == pygame.KEYDOWN and input_box_click_active):
            if event.key == pygame.K_BACKSPACE:
                user_input_text = user_input_text[:-1]
            elif event.key == pygame.K_RETURN:
                list_in = user_input_text.split(':')
                if ((int(list_in[1]) <= 60)and (int(list_in[2]) <= 60)):
                    write_file(lst=list_in)
                    if threading.active_count() < 2:
                        time_status, line_1, line_2, line_3, file_repeat_count = countdown_restart(hrs=line_1, mins=line_2, secs=line_3, times_up=time_status, thread=thread, file_repeat_count=file_repeat_count)
                else:
                    print("Too many minutes or seconds. There are only 60 seconds in a minute, 60 minutes in an hour!!! Go do some math.")
                input_box_click_active = False

                
            else:
                if (((event.unicode.isdigit()) or ((event.unicode == ':') and (user_input_text.count(':') < 2))) and (len(user_input_text) < 17)):
                    user_input_text += event.unicode




        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            zone_x = ((input_box_info["box_x"]<=mouse_pos[0]) and (mouse_pos[0]<=(input_box_info["box_x"]+input_box_info["box_width"])))
            zone_y = ((input_box_info["box_y"]<=mouse_pos[1]) and (mouse_pos[1]<=(input_box_info["box_y"]+input_box_info["box_height"])))
            if (zone_x and zone_y):
                input_box_click_active = not(input_box_click_active)
            
            
               
            zone_x = ((control_box_info["button_x"]<=mouse_pos[0]) and (mouse_pos[0]<=(control_box_info["button_x"]+control_box_info["button_width"])))
            zone_y = ((control_box_info["button_y"]<=mouse_pos[1]) and (mouse_pos[1]<=(control_box_info["button_y"]+control_box_info["button_height"])))
            if zone_x and zone_y and (threading.active_count() == 1):                       
                time_status, line_1, line_2, line_3, file_repeat_count = countdown_restart(hrs=line_1, mins=line_2, secs=line_3, times_up=time_status, thread=thread, file_repeat_count=file_repeat_count)
                control_button_click_active = not(control_button_click_active)
                if (time_status == "Type in your time to start!"):
                    list_in = user_input_text.split(':')
                    if ((int(list_in[1]) <= 60)and (int(list_in[2]) <= 60)):
                        write_file(lst=list_in)
                        if threading.active_count() < 2:
                            time_status, line_1, line_2, line_3, file_repeat_count = countdown_restart(hrs=line_1, mins=line_2, secs=line_3, times_up=time_status, thread=thread, file_repeat_count=file_repeat_count)
                    else:
                        print("Too many minutes or seconds. There are only 60 seconds in a minute, 60 minutes in an hour!!! Go do some math.")
                    input_box_click_active = False


            
        

    if control_button_click_active:
        control_button_color = control_box_info["button_color_active"]
    else:
        control_button_color = control_box_info["button_color_passive"]
    if input_box_click_active:
        box_color = input_box_info["box_color_active"]
    else:
        box_color = input_box_info["box_color_passive"]



    #Drawing the background
    ui.draw_bg(WIN=WIN, bg_color=bg_color, win_width=WIDTH, win_height=HEIGHT)

    #Drawing the control button
    ui.draw_button(WIN=WIN, button_color=control_button_color, button_x=control_box_info["button_x"], button_y=control_box_info["button_y"], button_width=control_box_info["button_width"], button_height=control_box_info["button_height"], button_border=control_box_info["button_border"], button_border_radius=control_box_info["button_border_radius"]) #Drawing the outline
    font = set_font() #Specify the font
    ui.write_ui_text(WIN=WIN, font=font, text=control_box_info["text"], color=control_box_info["text_color"], text_x=control_box_info["text_x"], text_y=control_box_info["text_y"]) #Drawing the text of the control button

    #Drawing the input box
    ui.draw_button(WIN=WIN, button_color=box_color, button_x=input_box_info["box_x"], button_y=input_box_info["box_y"], button_width=input_box_info["box_width"], button_height=input_box_info["box_height"], button_border_radius=input_box_info["box_border_radius"])
    font = set_font(font_type="Segoe_UI", font_size=24)
    ui.write_ui_text(WIN=WIN, font=font, text=user_input_text, color=text_color, text_x=input_box_info["text_x"], text_y=input_box_info["text_y"])

    try:
        t_up = countdown.times_up
    except AttributeError:
        t_up = False


    if t_up:
        font = set_font(font_type="Segoe-UI", font_size=48)
        time_status = "Times up!"
        control_box_info["text"] = "RESET"
        try:
            times_up_sound_thread.join()
        except NameError:
            pass
        finally:
            bell_chime_sound_thread = threading.Thread(target=play_sound.psound, args=(str(bell_chime_sound_file_name)))
            bell_chime_sound_thread.start()
            print(f"There are {threading.active_count()} threads running currently.")
            bell_chime_sound_thread.join()
            while file_repeat_count < 1:
                times_up_sound_thread = threading.Thread(target=play_sound.psound, args=(str(times_up_sound_file_name)))
                times_up_sound_thread.start()
                print(f"There are {threading.active_count()} threads running currently.")
                file_repeat_count += 1
    elif time_status == "You still have time":
        font = set_font(font_type="Segoe-UI", font_size=24)
        ui.write_ui_text(WIN=WIN, font=font, text=(f"Your reminder is for {line_1} hrs, {line_2} mins, {line_3} secs."), color=text_color, text_x=(WIDTH*0.5), text_y=(HEIGHT*0.1))


    ui.write_ui_text(WIN=WIN, font=font, text=time_status, color=text_color, text_x=(WIDTH*0.5), text_y=(HEIGHT*0.5))
    pygame.display.update()