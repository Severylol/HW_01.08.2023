import os
os.system('cls')
def process_football_matches():
    n = int(input("Введите количество завершенных игр: "))
    teams = {}

    for _ in range(n):
        match_result = input().split(";")
        team1, score1, team2, score2 = match_result
        score1, score2 = int(score1), int(score2)

        if team1 not in teams:
            teams[team1] = [0, 0, 0, 0, 0]
        teams[team1][0] += 1
        if score1 > score2:
            teams[team1][1] += 1
            teams[team1][4] += 3  #добавляю 3 очка за победу
        elif score1 == score2:
            teams[team1][2] += 1  #увеличиваю количество ничьих
            teams[team1][4] += 1  #1 очко за ничью
        else:
            teams[team1][3] += 1  #увеличиваю количество поражений

        #обработка второй команды
        if team2 not in teams:
            teams[team2] = [0, 0, 0, 0, 0]
        teams[team2][0] += 1
        if score2 > score1:
            teams[team2][1] += 1
            teams[team2][4] += 3
        elif score2 == score1:
            teams[team2][2] += 1
            teams[team2][4] += 1
        else:
            teams[team2][3] += 1

    #ыывод сводной таблицы
    for team, stats in teams.items():
        print(f"{team}:{stats[0]} {stats[1]} {stats[2]} {stats[3]} {stats[4]}")

if __name__ == "__main__":
    process_football_matches()
