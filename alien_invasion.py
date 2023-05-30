import pygame
import sys

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion")

        # Set the background colour.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch the keyboard and mouse events.
            # Event loop, that listens for events and performs appropriate tasks.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.update()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()