
# coding: utf-8

# In[2]:


import random as random
import numpy as np
import movement as move
import gamemap as gm
from player import Player
from IPython.display import clear_output
        
def initialize():
    """Initialize the game settings. 
       
    Args:
        None

    Returns:
        (dictionary): dictionary containing:

            game_map (GameMap): The class GameMap instance to wrap
            player (Player): The class Player instance to wrap
               
    """
    
    game_map = gm.GameMap()
    player = Player(coordinates=game_map.generate_coordinates())
    game_map.add_actor_to_map(player)
    
    return {'game_map': game_map, 'player': player}

def print_game_board(session):
    """Print out the current game state. 
    
    Prints out the current player state and current map.
       
    Args:
        session (dictionary): A dictionary including all the current session objects.   

    Returns:
        None
               
    """
    
    clear_output(wait=True)
    session['player'].print_stats()
    session['game_map'].print_small_map(session['player'])
    
    
def ask_for_input(options):
    """Ask for input and return lower case string. 
    
    Asks the user for an input and return that input in a lower case string.
    
    The options argument is part of the function in order to make it clear
    what are the options without looking at the rest of the code we return 
    it for use in other places in the code.
           
    Args:
        options (string): A string including the options to chose from.   

    Returns:
        (tuple): tuple containing:

            options (string): A string including the options to chose from.
            user_input (string): A string of the user input in lower case.
               
    """
    
    user_input = input("Choose an option {0}:".format((options.title())))
    user_input = user_input.lower()
    
    return options, user_input

def moving_loop(session):
    """Ask for input and move the player using input. 
    
    Asks the user for a direction input using the ask_for_input function if the input
    is in the options string then we move the player using the walk function and move_actor_on_map
    function after the player is moved we present the player with the new game state using
    print_game_board function.
    
    If the player input is exit then we break out of the move loop. 
           
    Args:
        session (dictionary): A dictionary including all the current session objects.   

    Returns:
        None
               
    """
    
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
    """Ask for input and start or exit the game. 
    
    Asks the user if he wants to start a new game if he dose the we call the initialize
    fucntion to set the game strating state we then call theprint_game_board fucntion 
    to present the user with the current game state.
    
    If the player input is exit then we break out of the play loop and the progrem is terminated. 
           
    Args:
        None   

    Returns:
        None
               
    """
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

