m = 2
center = (2, 3)
forest_map = [
[1,0,0,0,1],
[1,0,1,1,1],
[1,1,0,1,1],
[1,0,1,1,0],
[0,1,0,1,1]
]

r = center[0]
c = center[1]

def count_trees(forest_map, r, c, m):
    trees = 0
    if (m%2==1):
        for i in range(r-(m//2),r+(m//2)+1):
            for j in range(c-(m//2),c+(m//2)+1):
                if(forest_map[i][j]==1):
                    trees += 1
    else:
        for i in range(r-(m//2),r+(m//2)+1):
            for j in range(c-(m//2),c+(m//2)+1):
                if(forest_map[i][j]==1):
                    trees += 1
    return trees

ans = count_trees(forest_map, r, c, m)
print(ans)