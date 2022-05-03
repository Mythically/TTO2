import challonge, pprint

my_user = "TheMythh"
my_api_key = "KpgOkCV50nJ4nWrIPEwj5dwT71yRVvWcM7SueADm"
challonge.set_credentials(my_user, my_api_key)

ids = []
rounds_players = []
titles = []

def getTournaments():
    global ids
    tournaments = challonge.tournaments.index()
    ids = [eachID['id'] for eachID in tournaments]


def getParticipants(idt):
    participants = [challonge.participants.index(idt)]
    people = []
    x = ""
    for person in participants:

        for thing in range(len(person)):
            people.append({
                'name': person[thing]['name'],
                'ID': person[thing]['id']
            })

    return people


def getRounds():
    global titles
    titles = []
    i = 0
    for round in rounds_players:
        titles.append(f"Round {i}")
        i+=1


def getMatches(idt):
    global rounds_players
    rounds_players = []
    rounds = -1
    people = getParticipants(idt)
    matches = [challonge.matches.index(idt)]
    for match in matches:
        for seed in match:
            if rounds != seed['round'] - 1:
                print(rounds, seed['round']-1)
                rounds_players.append([])
                rounds = seed['round'] - 1
            for person in people:
                if seed['player1_id'] == person['ID']:
                    name1 = person['name']
                if seed['player2_id'] == person['ID']:
                    name2 = person['name']
            rounds_players[seed['round'] - 1].append({
                "player1": {
                    'name': name1,
                    'ID': seed['player1_id']
                },
                "player2": {
                    'name': name2,
                    'ID': seed['player2_id'],
                }
            })
    getRounds()
    pprint.pprint(rounds_players)
    return rounds_players


# getMatches(11119218)
