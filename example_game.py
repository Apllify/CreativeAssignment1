import game_lib

#THIS IS A VERY BASIC EXAMPLE OF A DART THROWING GAME !!!

game_lib.set_grid_width(10)
game_lib.set_grid_height(10)

while(True):
    
    game_lib.reset_grid()
    
    x = input("Please input the x position of your dart (q to quit) ==> ")
    
    if x == "q":
        break
    
    y = input("Please input the y position of your dart (q to quit) ==> ")
    
    if y == "q" :
        break
    
    
    
    try:
        x = int(x)
        y = int(x)
    except:
        print("Veuillez entrez des coordonnées valides !")
        continue 
    
    if x not in range(game_lib.grid_width) or y not in range(game_lib.grid_height) :
        print("Veuillez entrez des coordonnées valides !")
        continue
    
    
    game_lib.set_grid_element_at(x, y, "X")
    
    game_lib.display()