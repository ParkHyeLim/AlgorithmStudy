T = int(input())    

for _ in range(T):
    M, N, K = map(int, input().split())
    send = [[0]*N for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    num = 0
    
    for i in range(K):
        X, Y = map(int, input().split())
        send[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if (send[i][j] == 1 and not visited[i][j]):
                stack = [(i, j)]
                print(stack)
                visited[i][j] = True
                num +=1
                
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and send[nx][ny] == 1:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                    
    print(num)
