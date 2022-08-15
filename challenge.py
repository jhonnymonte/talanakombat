from players import *


def set_up_and_run_match(match_data):
    #value player
    player_1 = match_data['player1']
    player_2 = match_data['player2']
    print(player_1)
    print(player_2)

    set_player_one(player_1, player_2)

    let_the_carnage_begins(player_1, player_2)


#who should start with a less o combo moves
def set_player_one(player_1, player_2):
    length_moves_player_1 = len(player_1["movimientos"] + player_1["golpes"])
    length_moves_player_2 = len(player_2["movimientos"] + player_2["golpes"])
    
    if length_moves_player_2 < length_moves_player_1:
        change_player_data(player_1, player_2)

    elif length_moves_player_2 == length_moves_player_1:
        if len(player_2["movimientos"]) < len(player_1["movimientos"]):
            change_player_data(player_1, player_2)
        
        elif len(player_2["movimientos"]) == len(player_1["movimientos"]):
            if player_2["golpes"] < player_1["golpes"]:
                change_player_data(player_1, player_2)




def change_player_data(player_1, player_2):
    global moves_player_1, moves_player_2,special_moves_player_1,special_moves_player_2,hit_damage_player_1,hit_damage_player_2
    player_1, player_2 = player_2, player_1
    moves_player_1, moves_player_2 = moves_player_2, moves_player_1
    special_moves_player_1, special_moves_player_2 = special_moves_player_2, special_moves_player_1
    hit_damage_player_1, hit_damage_player_2 = hit_damage_player_2, hit_damage_player_1



def let_the_carnage_begins(player_1, player_2):
    end_of_stamina = 0
    stamina_player_1 = 6
    stamina_player_2 = 6
    turn = max(len(player_1['movimientos']),len(player_2['movimientos']))
    list_of_moves = {}
    

    while end_of_stamina < turn:
        try:
            turn_moves_player_1 = player_1['movimientos'][end_of_stamina]
            turn_tap_button_player_1 = player_1['golpes'][end_of_stamina]
            help_text_player_1 = turn_moves_player_1 + turn_tap_button_player_1
            if len(help_text_player_1) > 2:
                try:
                    special_moves = special_moves_player_1[help_text_player_1]
                    stamina_player_2 -= hit_damage_player_1[help_text_player_1]
                    if stamina_player_2 < 0:
                        break
                except KeyError:
                    special_moves = "Amaga un golpe especial"  
                text_player_1 = (f'{players["player1"]} {special_moves}')
                
                
            elif len(help_text_player_1) == 2 and turn_tap_button_player_1 == '':
                text_player_1 = (f'{players["player1"]} se mueve ')
                
            else:
                text_player_1 = (f'{players["player1"]} {moves_player_1[turn_moves_player_1]} {tap_button[turn_tap_button_player_1]}')
                stamina_player_2 -= hit_damage_player_1[turn_tap_button_player_1]
                if stamina_player_2 < 0:
                        break
            print(text_player_1, help_text_player_1)
            
            
        except IndexError:
            pass

        try:
            turn_moves_player_2 = player_2['movimientos'][end_of_stamina]
            turn_tap_button_player_2 = player_2['golpes'][end_of_stamina]
            help_text_player_2 = turn_moves_player_2 + turn_tap_button_player_2
            if len(help_text_player_2) > 2:
                try:
                    special_moves = special_moves_player_2[help_text_player_2]
                    stamina_player_1 -= hit_damage_player_2[help_text_player_2]
                    if stamina_player_1 < 0:
                        break
                except KeyError:
                    special_moves = "Amaga un golpe especial "

                text_player_2 = (f'{players["player2"]} {special_moves}')
            elif len(help_text_player_2) == 2 and turn_tap_button_player_2 == '' :
                text_player_2 = (f'{players["player2"]} se mueve')
                
            else:
                text_player_2 = (f'{players["player2"]} {moves_player_2[turn_moves_player_2]} {tap_button[turn_tap_button_player_2]}')
                stamina_player_1 -= hit_damage_player_2[turn_tap_button_player_2]
                if stamina_player_1 < 0:
                        break
            print(text_player_2,help_text_player_2)
            end_of_stamina += 1
        except IndexError:
            pass


    if stamina_player_1 > stamina_player_2:
        winner,stamina = players["player1"],stamina_player_1
    else:
        winner,stamina = players["player2"],stamina_player_1

    print(f" {winner} wins y todavia le quedaba {stamina} puntos de vida")
    print(list_of_moves)
    