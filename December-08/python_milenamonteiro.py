def cheating(rows):
    classroom = []
    for y in range(rows):
        classroom.append(input().split(' '))

    probab = []
    
    for r in range(len(classroom)):
        p_row = []
        row = classroom[r]
        
        for p in range(len(row)):
            seat = row[p]
            num = 0
            
            if p > 0 and row[p-1] == seat: num += 0.2
            if p + 1 < len(row) and row[p+1] == seat: num += 0.2

            if p > 0 and r > 0 and classroom[(r-1)][p] == seat: num += 0.3
            if r + 1 < len(classroom) and classroom[(r+1)][p] == seat: num += 0.2

            if p > 0 and r > 0 and classroom[r-1][p-1] == seat: num += 0.025
            if p > 0 and r + 1 < len(classroom) and classroom[(r+1)][p-1] == seat: num += 0.025

            if r > 0 and p + 1 < len(classroom[r-1]) and classroom[r-1][p+1] == seat: num += 0.025
            if r + 1 < len(classroom) and p + 1 < len(row) and classroom[r+1][p+1] == seat: num += 0.025

            p_row.append(num)
        
        probab.append(p_row)
        
    for row in probab:
        print(row)
