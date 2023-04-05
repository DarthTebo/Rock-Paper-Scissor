
def player(prev_play, opponent_history=[], sequences={}):
    turns = 3

    if prev_play != '':
        opponent_history.append(prev_play)

    if len(opponent_history) <= turns:
        return "P"

    if len(opponent_history) > turns + 1:
        opponent_history.pop(0)

    sec = "".join(opponent_history)
    sequences[sec] = sequences.get(sec, 0)+1

    secu = "".join(opponent_history[-turns:])
    next_turn = max([secu+"R", secu+"P", secu+"S"], key = lambda k: sequences.get(k,0))[-1]

    if next_turn == "R": return "P"
    if next_turn == "P": return "S"
    if next_turn == "S": return "R"
