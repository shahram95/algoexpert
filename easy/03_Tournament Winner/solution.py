def tournamentWinner(competitions, results):
    score_dict = dict()

    for competition,result in zip(competitions,results):
        winner = competition[not(result)]
        score_dict[winner] = score_dict.get(winner,0)+3
    return max(score_dict, key=score_dict.get)