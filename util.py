# -*- coding: utf-8 -*-
'''
title           :util.py
description     :Utilities used in the games
author          :Pablo Gonzalez Carrizo (unmonoqueteclea)
date            :20180802
notes           :
python_version  :3.6
'''
import pygame
from pygame.locals import RLEACCEL
import tkinter as tk
from tkinter import ttk

'''
 ***** CONSTANTS ******
'''
WIDTH = 640  # Window width
HEIGHT = 480  # Window height
FPS = 30  # Frames per second

DIRECTION_UPWARDS = 1  # Pong player movement upwards
DIRECTION_DOWNWARDS = -1  # Pong player movement downwards
DIRECTION_STILL = 0  # Pong player no movement

MOVEMENT_RIGHT = 1  # Racing car movement right
MOVEMENT_LEFT = -1  # Racing car movement keft
MOVEMENT_STOP = 0  # Racing car no movement

MENU_MAIN = 0  # Main menu
MENU_PONG = 1  # Pong menu
MENU_TRAIN_PONG = 2  # Training pong
MENU_PLAY_PONG = 3  # AutoPlay pong
MENU_RACING = 5  # Racing menu
TRAINING_SCREEN = 4  # Training screen
MENU_TRAIN_RACING = 6  # Training racing
MENU_PLAY_RACING = 7  # Autoplay racing

GAME_NAMES = {MENU_PONG: "Pong Game", MENU_RACING: "Racing Game"}

# Menu selection
SELECTED_PONG = 0
SELECTED_RACING = 1
SELECTED_QUIT = 2
SELECTED_AUTO = 2
SELECTED_TRAIN = 3
SELECTED_BACK = 4

GAME_MENU_OPTIONS = {
    SELECTED_TRAIN: {
        MENU_PONG: MENU_TRAIN_PONG,
        MENU_RACING: MENU_TRAIN_RACING
    },
    SELECTED_AUTO: {
        MENU_PONG: MENU_PLAY_PONG,
        MENU_RACING: MENU_PLAY_RACING
    },
    SELECTED_BACK:{
        MENU_PONG: MENU_MAIN,
        MENU_RACING: MENU_MAIN
    }
}

ML_BIGML = 0

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Racing game car colors
CAR_COLORS = (red, green, yellow, blue, black)

'''
 *** FUNCTIONS ****
'''


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText, newText.get_rect()


# Get text font
def get_font(type):
    font = "images/EffectsEighty.ttf"
    if type == "titles" or type == 0:
        font = "images/EffectsEighty.ttf"
    elif type == "normal" or type == 1:
        font = 'images/DroidSans.ttf'
    return font


# Load image into pygame sprite
def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error as message:
        raise SystemExit(message)
    image = image.convert()
    if transparent:
        # We suppose the top left corner is transparent
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image


# Shows TKinter PopUp message
def popupmsg(msg):
    popup = tk.Tk()
    x = popup.winfo_screenwidth()/2 - 185
    y = popup.winfo_screenheight()/2 - 50
    popup.geometry("+%d+%d" % (x, y))
    popup.wm_title("Error !")
    label = ttk.Label(popup, text=msg, font=("Verdana", 10))
    label.pack(side="top", fill="x", padx=100, pady=20)
    B1 = ttk.Button(popup, text="Okay",  command = popup.destroy)
    B1.pack(pady=20)
    popup.mainloop()