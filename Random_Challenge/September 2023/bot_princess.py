def displayPathtoPrincess(n,grid):
    m = 'm'
    p = 'p'
    
    for row,col in enumerate(grid):
        if m in col:
            m_col = col.index(m)
            m_row = row
        if p in col:
            p_col = col.index(p)
            p_row = row
    movement = []
    for _ in range(n):
        if m_col > p_col:
            movement.append('LEFT')
            m_col-=1
        elif m_col == p_col:
            break
        else:
            movement.append('RIGHT')
            m_col+=1
    for _ in range(n):
        if m_row > p_row:
            movement.append('UP')
            m_row-=1
        elif m_row == p_row:
            break
        else:
            movement.append('DOWN')
            m_row+=1
    return(print(*movement, sep='\n'))
        

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)