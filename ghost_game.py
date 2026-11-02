import math
import random
import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("My Game")

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.is_running = True

        self.image = pygame.image.load("game.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()
        self.rect.center = (self.screen_width // 2, self.screen_height // 2)
        self.speed = 6

        self.alpha = 255
        self.alpha_speed = -4

        self.float_timer = 0
        self.particles = []
        self.bg_hue = 0

    def run(self):
        while self.is_running:
            self._check_events()
            self._update()
            self._draw()

            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def _update(self):
        keys = pygame.key.get_pressed()
        moved = False

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.speed
            moved = True
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < self.screen_width:
            self.rect.x += self.speed
            moved = True
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.top > 0:
            self.rect.y -= self.speed
            moved = True
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.bottom < self.screen_height:
            self.rect.y += self.speed
            moved = True

        self.alpha += self.alpha_speed
        if self.alpha <= 90 or self.alpha >= 255:
            self.alpha_speed *= -1

        self.float_timer += 0.1
        self.float_offset = math.sin(self.float_timer) * 5

        self.bg_hue = (self.bg_hue + 1) % 360

        if moved:
            self.particles.append([
                self.rect.centerx + random.randint(-10, 10),
                self.rect.centery + random.randint(-10, 10),
                random.randint(4, 7),
                255
            ])

        for p in self.particles:
            p[2] -= 0.15
            p[3] -= 8

        self.particles = [p for p in self.particles if p[2] > 0 and p[3] > 0]

    def _draw(self):
        bg_color = pygame.Color(0)
        bg_color.hsva = (self.bg_hue, 50, 20, 100)
        self.screen.fill(bg_color)

        for p in self.particles:
            particle_surface = pygame.Surface((int(p[2] * 2), int(p[2] * 2)), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, (200, 230, 255, int(p[3])), (int(p[2]), int(p[2])), int(p[2]))
            self.screen.blit(particle_surface, (p[0] - p[2], p[1] - p[2]))

        self.image.set_alpha(self.alpha)
        render_pos = (self.rect.x, self.rect.y + self.float_offset)
        self.screen.blit(self.image, render_pos)

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()