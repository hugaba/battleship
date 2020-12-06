import numpy as np
import random
import string

def shoot(coordinates, enemy_grid):
    """
    Function that check if the coordinates given by the player are matching a ship place. 
    
    ------
    coordinates : tuple of int 
                  coordinates of where the user wants to shoot
    coordinates_ships: list of tuples of int
                       list of coordinates where there still is ships to hit
    enemy_grid: list of list of int
                list of what there is in each case
    ------
    Return the grid with the hit spot and the list of tuple where there is still ships to hit
    
    """
    already_asked_coordinates = [""]  
    # use of function get coordinates to had the tuple where the user already shoot 
    already_asked_coordinates = get_coordinates(enemy_grid, 3) + get_coordinates(enemy_grid,1)

    # use of function get coordinates to had the tuple where the ships are
    coordinates_ships = get_coordinates(enemy_grid, 2)
    
    # check if user already hit spot
    if coordinates in already_asked_coordinates:
        print("\nYou already hit shoot here\n")
        return enemy_grid, coordinates_ships
    
    # check if the shoot hit or miss target 
    if coordinates in coordinates_ships:
        updated_grid = update_grid(enemy_grid, coordinates, 3)
        print("\nyou hit I.A.\n")
    else:        
        updated_grid = update_grid(enemy_grid, coordinates, 1)
        print("\nyou missed I.A.\n")
        
    return updated_grid

def get_coordinates(grid, value):
    """
    Function that takes the enemy grid and convert the cells with ship into coordinates.
    
    -------
    grid : list of list of int
           list of what there is in each case
    value : int
            value to compare with
    -------
    return the coordinates where the is the given value
    """
    coordinates = []
    
    # loop over each row
    for i in range(0, len(grid)):
        # loop over each column
        for j in range(0, len(grid[i])):
            # check if the value of the cell is equal to the value
            if grid[i][j] == value:
                coordinates.append((i, j))
    return coordinates

def ask_coordinates(enemy_grid):
    """
    Function that asks the user for coordinates where he wants to shoot
    
    ------
    enemy_grid: list of list of int
                list of what there is in each case
    ------
    return the coordinates of where the user want to shoot
    """
    # make a list of alphabet letter in uppercase
    line_list = list(string.ascii_uppercase)
    # reduce the list down to the size of the list
    line_list = line_list[0:len(enemy_grid)]
    # make a list of numbers up to the size of the grid
    column_list = list(range(1,(len(enemy_grid) + 1)))
    line = ""
    # initialized with value out of column_list
    column = 100 
    
    # while the user don't write a letter in the good range it keeps asking user the coordinate
    while line.capitalize() not in line_list:
        line = input(f"Enter first coordinate [A:{line_list[len(line_list) - 1]}]: ")
        # if letter not in the list, print a message and go back to the beginning of the loop
        if line.capitalize() not in line_list:
            print(f"You need to enter a letter between A and {line_list[len(line_list) - 1]}")
    
    # while the user don't write a number in the good range it keeps asking user the coordinate
    while int(column) not in column_list:
        value = input(f"Enter second coordinate [1:{column_list[len(column_list) -1]}]: ")
        exception = f"You need to enter a number between 1 and {len(column_list)}"
        
        # try to convert to int the value entered by user
        try :
            column = int(value)
            
            # if number no in good range print an error and asks for coordinate again
            if int(column) not in column_list:
                print(exception)
        # if it can't convert the value into int, it means the value is a string and asks for coordinate again
        except:
            print(exception)
            
    #when both coordinates are in the good format and range we add them to the coordinate variable
    coordinates = (int(line_list.index(line.capitalize())), (int(column) - 1))    
    return coordinates

def update_grid(grid, coordinates, value):
    """
    Update the celles in the enemy grid with the value of what is in this cell
    ------
    grid : list of list of int
           list of what there is in each case
    coordinates : tuple of int
                  coordinates of where the update is wanted
    value : int
            value to update with
    ------
    return a list a list of int withe the value updated in the given coordinate
    """
    grid[coordinates[0]][coordinates[1]] = value
    return grid

def draw_title():
    title = """
    8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    8                                                                                                              8
    8  888888b          d8888  888888888  888888888  888       888888888   .d8888b.   888   888  8888888  888888b  8
    8  888    b        d88888  888888888  888888888  888       888        d88P  Y88b  888   888    888    888    b 8
    8  888    p       d88P888     888        888     888       888         Y88b.      888   888    888    888    8 8
    8  8888888       d88P 888     888        888     888       888888       Y888b.    888888888    888    888    P 8
    8  888    b     d88P  888     888        888     888       888888         Y88b.   888888888    888    888888P  8
    8  888     8   d888888888     888        888     888       888               888  888   888    888    888      8
    8  888     p  d88P    888     888        888     888       888        Y88b  d88P  888   888    888    888      8
    8  8888888P  d88P     888     888        888     88888888  888888888    Y8888P    888   888  8888888  888      8
    8                                                                                                              8
    8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    """
    print(title)

def draw_won():
    text = """
    88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    8                                                                                       8
    8 Y88b     d88Y   d8888b    888    888         888             888  8888888  88b    888 8
    8  Y88b   d88Y   d88  88b   888    888         888             888    888    888b   888 8
    8   Y88b d88Y   d88    88b  888    888         888             888    888    8888b  888 8
    8    Y88888Y    888    888  888    888         888             888    888    888Y8b 888 8
    8     Y888Y     888    888  888    888         888   d88888b   888    888    888 Y8b888 8
    8      888      Y88    88Y  888    888         Y88b d88Y Y88b d88Y    888    888  Y8888 8
    8      888       Y88  88Y    Y88  88Y           Y88888Y   Y88888Y     888    888   Y888 8
    8      888        Y8888Y      Y8888Y             Y888Y     Y888Y    8888888  888    Y88 8
    8                                                                                       8
    88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    """
    print(text)

def draw_ia_won():
    text = """
    888888888888888888888888888888888888888888888888888888888888888888888888888888888
    8                                                                               8
    8 8888888            d8888             888             888  8888888  88b    888 8
    8   888             d88888             888             888    888    888b   888 8
    8   888            d88P888             888             888    888    8888b  888 8
    8   888           d88P 888             888             888    888    888Y8b 888 8
    8   888          d88P  888             888   d88888b   888    888    888 Y8b888 8
    8   888         d888888888             Y88b d88Y Y88b d88Y    888    888  Y8888 8
    8   888   888  d88P    888 888          Y88888Y   Y88888Y     888    888   Y888 8
    8 8888888 888 d88P     888 888           Y888Y     Y888Y    8888888  888    Y88 8
    8                                                                               8
    888888888888888888888888888888888888888888888888888888888888888888888888888888888
    """
    print(text)

def list_places(grid, boat_size):
    """
    fonction qui retourne une liste composée de listes de coordonnées, chaque liste 
    représentant les endroits où il est possible de placer sur la grille grid un
    bateau de la taille boat_size
    """
    
    # on initialise la liste de choix :
    list_choices = []
    
    # on liste d'abord l'ensemble des choix pour une disposition horizontale :
    for i in range(len(grid)):
        # on regarde chaque ligne une par une :
        current_line = grid[i,:]
        # on regarde à chaque indice de la ligne si on peut placer le bateau à cet endroit, en plaçant
        # son côté gauche à l'endroit de l'indice :
        for indice in range(len(current_line)):
            # on arrête de chercher si le bateau est trop grand pour la taille de grille restante :
            if boat_size > (len(current_line) - indice):
                break
            # on initialise différentes variables :
            boat_size_left = boat_size
            possible_starting_position = True
            current_possible_position = []
            current_indice = indice
            # on regarde si la position qui commence par "indice" est toujours possible, et si
            # oui, on complète current_possible_position avec les coordonnées, jusqu'à ce qu'il
            # ne reste plus de "bateau" à placer :
            while possible_starting_position:
                if current_line[current_indice] == 2:
                    possible_starting_position = False
                elif current_line[current_indice] == 0:
                    current_possible_position.append((i,current_indice))
                    current_indice += 1
                    boat_size_left -= 1
                if boat_size_left <= 0:
                    break
            # si on a réussi a placer l'ensemble du bateau, on ajoute current_possible_position
            # à la liste de choix possibles :
            if possible_starting_position:
                list_choices.append(current_possible_position)
            
    
    # on liste ensuite l'ensemble des choix pour une disposition verticale :
    for i in range(len(grid)):
        # on regarde chaque colonne une par une :
        current_column = grid[:,i]
        # on regarde à chaque indice de la colonne si on peut placer le bateau à cet endroit, en plaçant
        # le haut du bateau à l'endroit de l'indice :
        for indice in range(len(current_column)):
            # on arrête de chercher si le bateau est trop grand pour la taille de grille restante :
            if boat_size > (len(current_column) - indice):
                break
            # on initialise différentes variables :
            boat_size_left = boat_size
            possible_starting_position = True
            current_possible_position = []
            current_indice = indice
            # on regarde si la position qui commence par "indice" est toujours possible, et si
            # oui, on complète current_possible_position avec les coordonnées, jusqu'à ce qu'il
            # ne reste plus de "bateau" à placer :
            while possible_starting_position:
                if current_column[current_indice] == 2:
                    possible_starting_position = False
                elif current_column[current_indice] == 0:
                    current_possible_position.append((current_indice, i))
                    current_indice += 1
                    boat_size_left -= 1
                if boat_size_left <= 0:
                    break
            # si on a réussi a placer l'ensemble du bateau, on ajoute current_possible_position
            # à la liste de choix possibles :
            if possible_starting_position:
                list_choices.append(current_possible_position)
        
    # on retourne la liste de l'ensemble des choix :
    return list_choices

def create_grid_different_lengths(list_enemy_boats = [5, 4, 3, 3, 2], size_grid = 10):
    
    # on initialise un tableau d'entier, tous nuls :
    grid = np.zeros((size_grid, size_grid), dtype=np.int8)
    
    # on initialise un booléen qui représente si la fonction a réussi à trouver une bonne disposition :
    ok_grid = False
    
    # tant qu'une disposition n'a pas été trouvée ...
    while not ok_grid:
        # on classe les bateaux par taille, du plus grand au plus petit, que l'on place dans une nouvelle liste :
        list_boats_to_place = list_enemy_boats
        list_boats_to_place.sort(reverse=True)
        # tant qu'il reste des bateaux à placer ...
        while len(list_boats_to_place) > 0:
            # on sort le plus grand bateau de la liste :
            current_boat_size = list_enemy_boats.pop(0)
            # on liste l'ensemble des positions possibles où le bateau peut être placé :
            list_possible_places = list_places(grid, current_boat_size)
            # si aucune position n'est disponible, on recommence la recherche depuis le début :
            if len(list_possible_places) == 0 :
                break
            # on choisit un endroit aléatoire et on y place le bateau :
            chosen_boat_position = random.choice(list_possible_places)
            # on place le bateau sur la grille :
            for coordinates in chosen_boat_position:
                grid[coordinates[0]][coordinates[1]] = 2
        # si on a réussi a placer tous les bateaux, on arrête la boucle :
        if len(list_boats_to_place) == 0:
            ok_grid = True
        
    # on initialise la liste des coordonnées des bateaux :
    list_coordinates = get_coordinates(grid, 2)
        
    return list_coordinates, grid

def enemy_shoot(your_grid):
    """
    Function that generates coordinates for IA and updates the grid after shooting
    -------
    your_ship_coordinates: tuple of int
                           coordinates of all your remaining ships on the grid
    your_grid : list of list of ints
                grid with all informations
    -------
    Return the updated grid with the shoot of IA and the coordinates of the remaining ships
    """
    already_asked_coordinates = []
    # Takes the coordinates of missed and hit shoots
    already_asked_coordinates = get_coordinates(your_grid, 3) + get_coordinates(your_grid, 1)
    # Use of function get_coordinates to have the coordinates of your ships
    your_ships_coordinates = get_coordinates(your_grid, 2)
    
    # list for higher probability targets in order to target next to already hit ships
    higher_probability_targets = []
    already_hit_ships = get_coordinates(your_grid, 3)
    for coordinates in already_hit_ships:
        higher_probability_targets.append(((coordinates[0]-1), coordinates[1]))
        higher_probability_targets.append(((coordinates[0]+1), coordinates[1]))
        higher_probability_targets.append((coordinates[0], (coordinates[1]+1)))
        higher_probability_targets.append((coordinates[0], (coordinates[1]-1)))


    if len(higher_probability_targets) > 0:
        for coordinates2 in higher_probability_targets:
            if coordinates2[0] < 0 or coordinates2[0] > (len(your_grid) -1) or coordinates2[1] < 0 or coordinates2[1] > (len(your_grid)-1) :
                higher_probability_targets.remove(coordinates2)
            elif coordinates2 in already_asked_coordinates:
                higher_probability_targets.remove(coordinates2)
    
    print(higher_probability_targets)
    
    prob = random.random()
    print(prob)

    if prob > 0.4 and len(higher_probability_targets) > 0:
        # Choice between higher probability targets
        coordinates = random.choice(higher_probability_targets)
        print("ok")
    else:
        # Randomly generates coordinates 
        coordinates = (random.randint(0, (len(your_grid) -1)), random.randint(0, (len(your_grid) -1)))
        print("not ok")

    # If coordinates have already been asked, it generates new coordinates
    while coordinates in already_asked_coordinates:
        coordinates = (random.randint(0, (len(your_grid) -1)), random.randint(0, (len(your_grid) -1)))
    
    print(coordinates)
    
    # Check if ship has been hit and upgrade of the grid
    if coordinates in your_ships_coordinates:
        updated_grid = update_grid(your_grid, coordinates, 3)
        print("IA hit you\n")
    else:
        updated_grid = update_grid(your_grid, coordinates, 1)
        print("IA missed you\n")
        
    return updated_grid

def display_grid(grid, player, player_name):  #fonction de mise en forme du plateau
