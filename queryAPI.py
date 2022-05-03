import challonge, pprint

my_user = "TheMythh"
my_api_key = "KpgOkCV50nJ4nWrIPEwj5dwT71yRVvWcM7SueADm"
challonge.set_credentials(my_user, my_api_key)
# ids = []


def getTournaments():
    global ids
    tournaments = challonge.tournaments.index()
    ids = [eachID['id'] for eachID in tournaments]
    # return ids
    # print(ids)

def getParticipants():
    participants = [challonge.participants.index(11108882)]
    people = []
    x = ""
    for person in participants:

        for thing in range(len(person)):
            people.append({
                'name': person[thing]['name'],
                'ID': person[thing]['id']
            })

    return people


def getMatches():
    rounds_players = []
    rounds = -1
    people = getParticipants()
    matches = [challonge.matches.index(11108882)]
    for match in matches:
        for seed in match:
            if rounds != seed['round'] - 1:
                rounds_players.append([])
                rounds = seed['round']-1
            for person in people:
                if seed['player1_id'] == person['ID']:
                    name1 = person['name']
                if seed['player2_id'] == person['ID']:
                    name2 = person['name']
            rounds_players[seed['round']-1].append({
                "player1": {
                    'name': name1,
                    'ID': seed['player1_id']
                },
                "player2": {
                    'name': name2,
                    'ID': seed['player2_id'],
                }
            })
    return rounds_players
    # pprint.pprint(rounds_players)
    # for round in rounds_players[0]:
    #     pprint.pprint(round)
    #     for players in round:
    #         print(players)

    # pprint.pprint(ids)
    # pprint.pprint(participants)
    # pprint.pprint(matches)



    # rounds_players.append([])
    # rounds_players.append([])
    # rounds_players.append([])
    # rounds_players[rounds].append("cccccccccc")
    # rounds_players[1].append("aaaaa")
    # rounds_players[2].append("bbbbbbbb")
    # pprint.pprint(rounds_players)