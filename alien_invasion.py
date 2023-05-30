import pygame
import sys

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion")
        # Initialize other game-related attributes here

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Other game logic and rendering here

            pygame.display.update()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()