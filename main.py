import pygame as pg

WIDTH = 600
HEIGHT = 600
FPS = 35
DELAY = 20
RED = (255, 0, 0)
OUTLINE = 1
LENGTH = 512
CENTER = (WIDTH/2, HEIGHT/2)
A = (CENTER[0] - LENGTH/2, CENTER[1] + LENGTH/2)
B = (CENTER[0] + LENGTH/2, A[1])
C = (CENTER[0], CENTER[1] - LENGTH/2)
BASE_CASE = LENGTH / 128

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
run = True


def draw(points):
    pg.draw.polygon(screen, RED, points, OUTLINE)
    pg.display.update()


def sierpinski(points, length):
    if length <= BASE_CASE:
        return

    pa, pb, pc = points

    a = ((pa[0]+pc[0])/2, (pa[1]+pc[1])/2)
    b = (a[0] + length, a[1])
    c = ((pa[0]+pb[0])/2, pa[1])

    # mid
    sierpinski((a, b, pc), length/2)
    # left
    sierpinski((pa, c, a), length/2)
    # right
    sierpinski((c, pb, b), length/2)

    draw((a, b, c))


if __name__ == '__main__':
    draw((A, B, C))
    sierpinski((A, B, C), LENGTH/2)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
