"""
아무 키나 누르고 있으면 텍스트가 표시되지만 Q 혹은 ESC를 누르면 꺼지는 프로그램입니다.
"""

import pygame

pygame.init()

size = [600, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()


def runGame():
    global done

    bg = pygame.image.load("examples/Background.jpg")
    bg = pygame.transform.scale(bg, (600, 800))

    sysfont = pygame.font.SysFont("AppleSDGothicNeoSB00", 36)
    text = sysfont.render("고양이 귀엽다", True, (0, 0, 0))

    while not done:
        clock.tick(1000)
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key in {pygame.K_ESCAPE, pygame.K_q}:
                    done = True

        if True in pygame.key.get_pressed():
            screen.blit(text, (325, 300))

        pygame.display.update()


runGame()
pygame.quit()
