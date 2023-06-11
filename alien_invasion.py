import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.clock = pygame.time.Clock()

    def _check_keydown_events(self, event):
        """Respond to keyPresses"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.update()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch the keyboard and mouse events.
            # Event loop, that listens for events and performs appropriate tasks.
            self._check_events()

            self.ship.update()
            # Redraw the screen and fill it with background colour
            # during each pass through the loop
            self._update_screen()
            self.clock.tick(60)



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()