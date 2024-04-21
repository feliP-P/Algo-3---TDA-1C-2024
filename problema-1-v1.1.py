def att(n):
    return n[1]

def deff(n):
    return n[2]

def nam(n):
    return n[0]

def find_best_players(players):
    players_ordered = sorted(players, key=nam)
    players_ordered = sorted(players_ordered, key=deff)
    players_ordered = sorted(players_ordered, key=att, reverse=True)
    return players_ordered[0:5], players_ordered[5:10]



def main():
    #print("enter team information:")
    T = int(input().strip())
    
    attackers_name = []
    defenders_name = []
    for case in range(1, T + 1):
        players = []
        for _ in range(10):
            name, attack, defense = input().strip().split()
            players.append((name, int(attack), int(defense)))


        attackers, defenders = find_best_players(players)
        attackers = sorted(attackers, key = nam)
        defenders = sorted(defenders, key = nam)

        for i in range(5):
            attackers_name.append(attackers[i][0])
            defenders_name.append(defenders[i][0])

    for case in range(1, T + 1):
        print(f"Case {case}:")
        print(f"({', '.join(attackers_name[(case-1)*5:case*5])})")
        print(f"({', '.join(defenders_name[(case-1)*5:case*5])})")
        #print(f"")


if __name__ == "__main__":
    main()