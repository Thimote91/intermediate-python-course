def main():
  import random
  dice_rolls = int(input('How many dice would you like to roll?'));dice_sum = 0
  dice_size = int(input('How many sides are the dice? '))
  nb_team = int(input('How many team play?'));nb_players = int(input('How many players in every team:'))
  teams_name,players_name = [''] * nb_team,[['' for j in range(nb_players)] for i in range(nb_team)]
  for i in range(0,nb_team):
    teams_name[i] = str(input("{} enter the name of you're team:".format('Team '+str(i+1))))
    for j in range(0,nb_players):
        players_name[i][j] = str(input(f"Player {j+1} of {teams_name[i]} input you're name:"))
  team_score = [[0,teams_name[i]] for i in range(nb_team)]#Score de chaque équipe au début de la partie

  for i in range(0,len(players_name)):
    for j in range(0,len(players_name[i])):
      for y in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1:
          print(f'{players_name[i][j]} rolled a {roll}! Critical Fail')
        elif roll == dice_size:
          print(f'{players_name[i][j]} rolled a {roll}! Critical Success!')
        else:
          print(f'{players_name[i][j]} rolled a {roll}')
      team_score[i][0] += dice_sum
      print(f'{players_name[i][j]} have rolled a total of {dice_sum}')
      dice_sum = 0
  best_score = team_score[0][0];win_team = team_score[0][1]
  for i in range(len(team_score)):
    if team_score[i][0] > best_score:
        win_team = team_score[i][1]
        best_score = team_score[i][0]
  print(f'{win_team} have won this game with {best_score} points.')

if __name__== "__main__":
  main()
