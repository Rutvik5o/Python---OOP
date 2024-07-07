#(21)=>Create a dictionary that will accpect cricket players name and scores in a match.also we are retrieving runs by a entering the player's name.

cricket_score={}


def add_score(player_name,score):

    if player_name in cricket_score:

        cricket_score[player_name].append(score)

    else:

        cricket_score[player_name] = [score]


add_score("Player 1",60)

add_score("Player 2",74)

add_score("Player 1",99)

add_score("Player 4",23)



def get_score(player_name):
    
    if player_name in cricket_score:

        return cricket_score[player_name]
    
    else:

        return "Player not found"
    


player_name = "Player 1"

print(f"Scores for {player_name} : {get_score(player_name)}")


player_name = "Player 2"

print(f"Scores for {player_name} : {get_score(player_name)}")

player_name = "Player 4"

print(f"Scores for {player_name} : {get_score(player_name)}")



