
# coding: utf-8

# In[ ]:


import random as random
import numpy as np
import movement as move
import gamemap as gm
from player import Player
from IPython.display import clear_output
        
def initialize():
    game_map = gm.GameMap()
    player = Player(coordinates=game_map.generate_coordinates())
    game_map.add_actor_to_map(player)
    
    return {'game_map': game_map, 'player': player}

def print_game_board(session):
    clear_output(wait=True)
    session['player'].print_stats()
    session['game_map'].print_small_map(session['player'])
    
    
def ask_for_input(options):
    user_input = input("Choose an option {0}:".format((options.title())))
    user_input = user_input.lower()
    
    return options, user_input

def moving_loop(session):
    while True:
        options, user_input = ask_for_input(options="up, down, left, right, exit")
        
        if user_input not in (options):
            print("Not an appropriate choice.")
            continue    
            
        if user_input in ["up", "down", "left", "right"]:
            move.walk(session['player'], user_input)        
            session['game_map'].move_actor_on_map(session['player'])
            print_game_board(session)
        
        elif user_input.lower()=="exit":
            break

def play_loop():
    while True:
        options, user_input = ask_for_input(options="new game, exit")
        
        if user_input not in (options):
            print("Not an appropriate choice.")
            continue
    
        if user_input=="new game":
            session = initialize()
            print_game_board(session)
            moving_loop(session)

        elif user_input=="exit":
            break
    
play_loop()

