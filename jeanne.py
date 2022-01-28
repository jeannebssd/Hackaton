import random as rd

def room_information():
    '''
    return the list that contain the aleatory the top-left coordinate of the room, the length L and width l of the room
    '''
    L = rd.randint(1, 10) #longueur de la chambre
    l = rd.randint(1, 10) #largeur de la chambre
    x, y = rd.randint(1, 600-L), rd.randint(1, 600-l)
    return[[x,y], L, l]
        

#definition de la fonction pourtour dont on aura besoin pour generer les couloirs

def pourtour(room):
    """
    return the list of coordonnates of the walls, takes in argument the information on the room 
    """
    x0, y0 = room[0]
    L, l = room[1], room[2]
    liste = [[x0,y0]]
    mur_haut = [[x0+k,y0] for k in range(L)]
    mur_droit = [[x0+L,y0-k] for k in range(l)]
    mur_bas = [[x0+k,y0-l] for k in range(L)]
    mur_gauche = [[x0,y0-k] for k in range(l)]
    liste += mur_haut + mur_droit + mur_gauche + mur_bas
    return(liste)

