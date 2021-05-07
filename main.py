# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1
#1. Spelers die hebben gescoord
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

#2. Minuten waarin is gescoord
goal_0 = 32
goal_1 = 54

#3. wie scoorde wanneer
scorers =player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1)
print(scorers)

#4. gebruik f-strings
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)

#part2
#1. kies een speler
player = 'Erwin Koeman'
#2. voormaan
first_name = player[:player.find(" ")]
#3. aantal letters achternaam
last_name_len = len(player[player.find(" ")+1:len(player)])
#4. naam afgekort
name_short = player[:1]+"."+player[player.find(" "):]
#5. chant
chant = ((first_name+"! ")*(len(first_name)-1))+((first_name+"!"))
#6. good chant
good_chant = chant[-1] != " "
















