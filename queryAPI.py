import challonge, pprint


def getTournaments():
    tournaments = challonge.tournaments.index()
    ids = [tournaments[eachID]['id'] for eachID in tournaments]
    return ids


def getMatches(tournament_ids):
    matches = [challonge.matches.index(id) for id in tournament_ids]
    pprint.pprint(matches)
    return matches


def getParticipants(tounament_ids):
    participants = [challonge.participants.index(id) for id in tounament_ids]
    return participants


def buildData():
    all_tournament_ids = getTournaments()
    getParticipants(all_tournament_ids[0])
