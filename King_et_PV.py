
# les potions

invisible_potion = (20, 20)   # coordonées de la potion
invisible_potion_color = (255, 192, 203)

draw_tile(invisible_potion[0], invisible_potion[1], invisible_potion_color)

if new_character == invisible_potion:
    draw_tile(invisible_potion[0], invisible_potion[1], (0,0,0))
    print(f"Vous avez récupéré une **invisble_potion**")
    
