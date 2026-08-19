import sys
import pygame

import config


class Game:
    def __init__(self, initial_scene_factory):
        pygame.init()

        self.window = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption(config.WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.scene = initial_scene_factory(self)

    def run(self):
        while self.running:
            dt_ms = self.clock.tick(config.FPS)
            dt = dt_ms / 1000.0  # đổi sang giây cho dễ tính toán vận tốc (px/giây)

            self._handle_events()
            self.scene.update(dt)
            self._draw()

        self._quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.scene.handle_event(event)

    def _draw(self):
        self.window.fill(config.COLOR_WINDOW_BG)
        self.scene.draw(self.window)
        pygame.display.flip()

    def _quit(self):
        pygame.quit()
        sys.exit()
