#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import random
import string
from battleship_function import *

play_again = True

while play_again:

    draw_title()
    
    level = ""
    
    # selection of difficulty
    while level not in ["easy", "medium", "hard"]:     
        level = input("What level do you want? (easy/medium/hard) ")
    
    # definition of grid parameters for each level
    if level == "easy":
        grid_size = 4
        list_enemy_boats = [3, 2, 2]
        list_ally_boats = [3, 2, 2]
    elif level == "medium":
        grid_size = 10
        list_enemy_boats = [5, 4, 3, 3, 2]
        list_ally_boats = [5, 4, 3, 3, 2]
    elif level == "hard":
        grid_size = 10
        list_enemy_boats = [4, 3, 2]
        list_ally_boats = [4, 3, 2]

    # building of the grid with grid parameters filled with 0
    enemy_grid = np.zeros((grid_size, grid_size), dtype=np.int8)
    your_grid = np.zeros((grid_size, grid_size), dtype=np.int8)
    
    # positioning of ships on the grid
    list_coordinates_enemy_ships, enemy_grid = create_grid_different_lengths(list_enemy_boats, size_grid = grid_size)
    list_of_your_ships, your_grid = create_grid_different_lengths(list_ally_boats, size_grid = grid_size)
    
    # while there is still ships on the enemy grid or your grid
    while len(list_coordinates_enemy_ships) > 0 and len(list_of_your_ships) > 0:
        
        # display of the grid
        print("----------------------------------------------------------------------------------")
        
        display_grid(your_grid, True, "player")
        display_grid(enemy_grid, False, "I.A.")
        
        print("----------------------------------------------------------------------------------\n")

        # asks the user for coordinates to shoot
        coordinates = ask_coordinates(enemy_grid)
        enemy_grid, list_coordinates_enemy_ships = shoot(coordinates, list_coordinates_enemy_ships, enemy_grid)
        
        #opponent turn
        your_grid, list_of_your_ships = enemy_shoot(list_of_your_ships, your_grid)
    
    # checking who won
    if len(list_coordinates_enemy_ships) < 1:
        # on indique au joueur qu'il a gagné la partie :
        draw_won()
    elif len(list_of_your_ships) <1:
        draw_ia_won()
    
    choice =""
    # while the user haven't write a good answer we keep asking if he wants to play again
    while choice.capitalize() not in ["Y", "N"]:
        #asks the user to write a choice between Y and N
        choice = input("Do you want to play again? (Y/N)")
        # if choice is N, play_again becomes False and the main while is stopped
        if choice == "N":
            print("Goodbye!")
            play_again = False