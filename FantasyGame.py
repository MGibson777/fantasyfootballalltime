import pandas as pd
import random



df = pd.read_excel("FantasyFootballOver100.xlsx")

length = len(df)

quarterback_options = []
halfback_options = []
receiver_options = []
tightend_options = []

# Will take any players from excel and add them to player pools

for num in range(length):
    if df.iloc[num,1] == "QB" and df.iloc[num,0] not in quarterback_options:
        quarterback_options.append(df.iloc[num,0])
    if df.iloc[num,1] == "RB" and df.iloc[num,0] not in halfback_options:
        halfback_options.append(df.iloc[num,0])
    if df.iloc[num,1] == "WR" and df.iloc[num,0] not in receiver_options:
        receiver_options.append(df.iloc[num,0])
    if df.iloc[num,1] == "TE" and df.iloc[num,0] not in tightend_options:
        tightend_options.append(df.iloc[num,0])

#print(quarterback_options)
#print(halfback_options)
#print(receiver_options)
#print(tightend_options)

# Convert players into dictionaries
players = {


}

for player in quarterback_options:
    player
    players[player] = {}
for player in halfback_options:
    player
    players[player] = {}
for player in receiver_options:
    player
    players[player] = {}
for player in tightend_options:
    player
    players[player] = {}


#print(players)

#Number of Teams Pre Draft Setup

num_teams = input("how many teams are drafting, maximum of 12")
number = int(num_teams)
original_number = int(num_teams)
picks = int(num_teams)*4

x = 0
# The Draft

teams = []

for num in range(int(num_teams)):
    team_name = "team" + str(num)
    teams.append(team_name)
    teams[num] = []



teams[0] = []


z = 0

while picks != 0:
    while number != 0:
        selection = input(f"Team {z} pick your quarterback {random.sample(quarterback_options, 5)}")
        teams[z].append(selection)
        z = z +1
        number = number -1
    number = original_number
    z = 0
    while number != 0:
        selection = input(f"Team {z} pick your halfback {random.sample(halfback_options, 5)}")
        teams[z].append(selection)
        z = z + 1
        number = number - 1
    number = original_number
    z = 0
    while number != 0:
        selection = input(f"Team {z} pick your halfback#2 {random.sample(halfback_options, 5)}")
        teams[z].append(selection)
        z = z + 1
        number = number - 1
    number = original_number
    z = 0
    while number != 0:
        selection = input(f"Team {z} pick your receiver {random.sample(receiver_options, 5)}")
        teams[z].append(selection)
        z = z + 1
        number = number - 1
    number = original_number
    z = 0
    while number != 0:
        selection = input(f"Team {z} pick your receiver #2 {random.sample(receiver_options, 5)}")
        teams[z].append(selection)
        z = z + 1
        number = number - 1
    number = original_number
    z = 0
    while number != 0:
        selection = input(f"Team {z} pick your receiver #3 {random.sample(receiver_options, 5)}")
        teams[z].append(selection)
        z = z + 1
        number = number - 1
    number = original_number
    z = 0
    while number != 0:
        selection = input(f"Team {z} pick your tightend {random.sample(tightend_options, 5)}")
        teams[z].append(selection)
        z = z + 1
        number = number - 1
    number = original_number
    z = 0
    while number != 0:
        #print(z)
        #print(teams[z])
        z = z + 1
        number = number -1
    picks = 0


for num in range(length):
            players[df.iloc[num,0]][df.iloc[num, 2]] = df.iloc[num, 3]
            #print(players)


w =0
team_total_points = 0

for team in teams:
    y = players[teams[w][0]]
    year = random.choice(list(y))
    points = int(players[teams[w][0]][year])
    team_total_points = points
    print(f'\nQuarterback for team {w}, {teams[w][0]}, year {year}, he scored {points}')
    y = players[teams[w][1]]
    year = random.choice(list(y))
    points = int(players[teams[w][1]][year])
    team_total_points = team_total_points + points
    print(f'Halfback for team {w}, {teams[w][1]}, year {year}, he scored {points}')
    y = players[teams[w][2]]
    year = random.choice(list(y))
    points = int(players[teams[w][2]][year])
    team_total_points = team_total_points + points
    print(f'Halfback#2 for team {w}, {teams[w][2]}, year {year}, he scored {points}')
    y = players[teams[w][3]]
    year = random.choice(list(y))
    points = int(players[teams[w][3]][year])
    team_total_points = team_total_points + points
    print(f'Wide Receiver for team {w}, {teams[w][3]}, year {year}, he scored {points}')
    y = players[teams[w][4]]
    year = random.choice(list(y))
    points = int(players[teams[w][4]][year])
    team_total_points = team_total_points + points
    print(f'Wide Receiver #2 for team {w}, {teams[w][4]}, year {year}, he scored {points}')
    y = players[teams[w][5]]
    year = random.choice(list(y))
    points = int(players[teams[w][5]][year])
    team_total_points = team_total_points + points
    print(f'Wide Receiver #3 for team {w}, {teams[w][5]}, year {year}, he scored {points}')
    y = players[teams[w][6]]
    year = random.choice(list(y))
    points = int(players[teams[w][6]][year])
    team_total_points = team_total_points + points
    print(f'TightEnd for team {w}, {teams[w][6]}, year {year}, he scored {points}')
    print(f"Team {w} total points is {team_total_points}\n")
    w = w + 1
    team_total_points = 0
