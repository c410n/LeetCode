class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if maze == None or len(maze) < 1:
            return 0
        
        if maze[start[0]][start[1]] == 1:
            return 0
        
        p = [start[:]]
        n = []
        
        maze[start[0]][start[1]] = 2
        
        while len(p) > 0:
            for y,x in p:
                t = y
                tmp = maze[y][x]
                while t+1 < len(maze) and maze[t+1][x] != 1:
                    t += 1
                    tmp += 1
                if maze[t][x] == 0 or maze[t][x] > tmp:
                    maze[t][x] = tmp
                    n.append([t, x])
                    
                t = y
                tmp = maze[y][x]
                while t-1 >= 0 and maze[t-1][x] != 1:
                    t -= 1
                    tmp += 1
                if maze[t][x] == 0 or maze[t][x] > tmp:
                    maze[t][x] = tmp
                    n.append([t, x])
                    
                t = x
                tmp = maze[y][x]
                while t+1 < len(maze[0]) and maze[y][t+1] != 1:
                    t += 1
                    tmp += 1
                if maze[y][t] == 0 or maze[y][t] > tmp:
                    maze[y][t] = tmp
                    n.append([y, t])
                    
                t = x
                tmp = maze[y][x]                
                while t-1 >= 0 and maze[y][t-1] != 1:
                    t -= 1
                    tmp += 1
                if maze[y][t] == 0 or maze[y][t] > tmp:
                    maze[y][t] = tmp
                    n.append([y, t])
                    
            p = n[:]
            n = []       
        if maze[destination[0]][destination[1]] == 0:
            return -1
        return maze[destination[0]][destination[1]]-2              
                    