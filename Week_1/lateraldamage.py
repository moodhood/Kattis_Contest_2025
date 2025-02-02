import random

n, k = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]

def shoot(x, y):
    print(x, y, flush=True)

def aim():
    while True:
        x = random.randint(1, n)
        y = random.randint(1, n)
        if matrix[y - 1][x - 1] == 0:
            return x, y

def main():
    global k
    ammunition = 0
    while k > 0 and ammunition < 2500:
        x, y = aim()
        shoot(x, y)
        ammunition += 1
        response = input().strip()
        if response == "miss":
            matrix[y - 1][x - 1] = 2
        elif response == "hit":
            matrix[y - 1][x - 1] = 1
        elif response == "sunk":
            matrix[y - 1][x - 1] = 1
            k -= 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x - 1 + dx, y - 1 + dy
                if 0 <= nx < n and 0 <= ny < n and matrix[ny][nx] == 1:
                    matrix[ny][nx] = 3
        else:
            break

main()