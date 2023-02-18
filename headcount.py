import numpy as np

def count_teams_headcount(event):
    rows = len(event)
    cols = len(event[0])
    team_counts = []

    for i in range(rows):
        for j in range(cols):
            if event[i][j] == 1:
                team_size = 0
                stack = [(i,j)]
                while stack:
                    row, col = stack.pop()
                    if event[row][col] == 1:
                        team_size += 1
                        event[row][col] = 0
                        if row > 0 and event[row-1][col] == 1:
                            stack.append((row-1, col))
                        if row+1 < rows and event[row+1][col] == 1:
                            stack.append((row+1, col))
                        if col > 0 and event[row][col-1] == 1:
                            stack.append((row, col-1))
                        if col+1 < cols and event[row][col+1] == 1:
                            stack.append((row, col+1))
                team_counts.append(team_size)
    total_headcount = sum(team_counts)
    return f'{len(team_counts)} teams of {sorted(team_counts, reverse=True)} totaling {total_headcount}'

print(count_teams_headcount([[1,1,0,0,0,0,1,1],
 [1,1,0,1,1,0,1,1],
 [0,0,0,1,1,0,0,0],
 [1,1,0,1,1,0,1,1],
 [1,1,0,0,0,0,1,1]]))

