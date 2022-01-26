import pygame

WINDOW_SIZE = [1024, 1024]

pygame.init()
font = pygame.font.SysFont('arial', 15, True)
X = font.render('X', True, (226, 0, 0))
Y = font.render('O', True, (0, 0, 0))
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

def getNei(y, x):
    dy = [0, 0, 1, -1]
    dx = [-1, 1, 0, 0]
    licz = 0
    for k in range(len(dx)):
        kx = (x + dx[k]) % width
        ky = (y + dy[k]) % height
        licz = licz + grid[ky][kx]
    return licz


def getTabNei():
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            grid[y][x] = getNei(y, x)
    return grid


def init():
    tab = [[0 for _ in range(width)] for _ in range(height)]
    tab[25][25] = 1
    return tab


def spread(grid):
    sasiedzi = getTabNei()
    for y in range(height):
        for x in range(width):
            print(grid[y][x])
            if grid[y][x] == 0:
                if sasiedzi[y][x] == 1:
                    grid[y][x] = 1


n = 50
width, height = n, n
grid = init()
time = 0


def write():
    while True:
        spread(grid)
        screen.fill((225, 225, 225))
        for row in range(50):
            for column in range(50):
                if grid[row][column] == 1:
                    screen.blit(X, [column * 21, row * 21])
                else:
                    screen.blit(Y, [column * 21, row * 21])
        clock.tick(5)
        pygame.display.flip()
    pygame.quit()

write()