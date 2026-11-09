import math
import random
import sys
import pygame


class Game:

    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ghost: Shadows and Souls")

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.is_running = True
        self.font = pygame.font.Font(None, 28)

        # Состояние призрака
        self.ghost = pygame.Rect(370, 270, 60, 60)
        self.speed = 6
        self.facing_right = True
        self.hp = 100
        self.max_hp = 100
        self.float_timer = 0

        # Способности
        self.dash_cd = 0
        self.freeze_timer = 0
        self.freeze_cd = 0

        # Прожектор (опасный свет)
        self.light_x = 100
        self.light_y = 150
        self.light_speed = 3.5
        self.light_radius = 110

        # Души для сбора
        self.souls = []
        self.score = 0
        self._spawn_souls(5)

        # Партиклы (эффекты)
        self.particles = []

    def _spawn_souls(self, count):
        for _ in range(count):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            self.souls.append(pygame.Rect(x, y, 16, 16))

    def run(self):
        while self.is_running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

                # Рывок на Shift
                if (
                    event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT)
                    and self.dash_cd == 0
                ):
                    dash_dist = 130
                    self.ghost.x += dash_dist if self.facing_right else -dash_dist
                    self.dash_cd = 60
                    self._add_dash_particles()

                # Заморозка на Q
                elif event.key == pygame.K_q and self.freeze_cd == 0:
                    self.freeze_timer = 150
                    self.freeze_cd = 360

    def _add_dash_particles(self):
        for _ in range(12):
            self.particles.append(
                [
                    self.ghost.centerx + random.randint(-15, 15),
                    self.ghost.centery + random.randint(-15, 15),
                    random.randint(4, 8),
                    255,
                    (180, 220, 255),
                ]
            )

    def _update(self):
        # Движение призрака
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.ghost.x -= self.speed
            self.facing_right = False
            moved = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.ghost.x += self.speed
            self.facing_right = True
            moved = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.ghost.y -= self.speed
            moved = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.ghost.y += self.speed
            moved = True

        self.ghost.clamp_ip(pygame.Rect(0, 0, self.width, self.height))

        # Перезарядка таймеров
        self.dash_cd = max(0, self.dash_cd - 1)
        self.freeze_cd = max(0, self.freeze_cd - 1)
        self.freeze_timer = max(0, self.freeze_timer - 1)
        self.float_timer += 0.08

        # Движение прожектора
        if self.freeze_timer == 0:
            self.light_x += self.light_speed
            if self.light_x > self.width - 100 or self.light_x < 100:
                self.light_speed *= -1

        # Проверка нахождения в луче света
        dist = math.hypot(
            self.ghost.centerx - self.light_x, self.ghost.centery - self.light_y
        )
        in_light = dist < self.light_radius

        if in_light and self.freeze_timer == 0:
            self.hp = max(0, self.hp - 0.7)
        else:
            self.hp = min(self.max_hp, self.hp + 0.15)

        # Сбор душ
        for soul in self.souls[:]:
            if self.ghost.colliderect(soul):
                self.souls.remove(soul)
                self.score += 1
                self._spawn_souls(1)

        # След при движении
        if moved:
            self.particles.append(
                [
                    self.ghost.centerx,
                    self.ghost.centery + 10,
                    random.randint(3, 6),
                    200,
                    (200, 230, 255),
                ]
            )

        # Обновление партиклов
        for p in self.particles[:]:
            p[2] -= 0.1
            p[3] -= 6
            if p[2] <= 0 or p[3] <= 0:
                self.particles.remove(p)

    def _draw_ghost(self):
        surf = pygame.Surface((self.ghost.w, self.ghost.h), pygame.SRCALPHA)
        dist = math.hypot(
            self.ghost.centerx - self.light_x, self.ghost.centery - self.light_y
        )
        in_light = dist < self.light_radius and self.freeze_timer == 0

        g_color = (255, 80, 80, 220) if in_light else (235, 240, 255, 220)

        pygame.draw.circle(surf, g_color, (30, 25), 22)
        pygame.draw.ellipse(surf, g_color, (8, 25, 44, 30))

        eye_x = 5 if self.facing_right else -5
        pygame.draw.circle(surf, (20, 20, 60), (25 + eye_x, 20), 4)
        pygame.draw.circle(surf, (20, 20, 60), (40 + eye_x, 20), 4)

        fy = self.ghost.y + math.sin(self.float_timer) * 5
        self.screen.blit(surf, (self.ghost.x, fy))

    def _draw(self):
        self.screen.fill((10, 12, 22))

        # Отрисовка луча света
        l_color = (100, 200, 255) if self.freeze_timer > 0 else (255, 255, 180)
        pygame.draw.circle(
            self.screen, l_color, (int(self.light_x), int(self.light_y)), self.light_radius
        )

        # Отрисовка душ
        for soul in self.souls:
            pygame.draw.ellipse(self.screen, (150, 230, 255), soul)

        # Отрисовка партиклов
        for p in self.particles:
            surf = pygame.Surface((int(p[2] * 2), int(p[2] * 2)), pygame.SRCALPHA)
            pygame.draw.circle(
                surf, (*p[4], int(p[3])), (int(p[2]), int(p[2])), int(p[2])
            )
            self.screen.blit(surf, (p[0] - p[2], p[1] - p[2]))

        # Отрисовка призрака
        self._draw_ghost()

        # Интерфейс (HP, Очки, Навыки)
        pygame.draw.rect(self.screen, (40, 40, 40), (20, 20, 200, 16), border_radius=4)
        pygame.draw.rect(
            self.screen, (150, 100, 255), (20, 20, self.hp * 2, 16), border_radius=4
        )

        d_txt = "Shift: Готов" if self.dash_cd == 0 else f"Shift: {self.dash_cd//60 + 1}s"
        f_txt = "Q: Готова" if self.freeze_cd == 0 else f"Q: {self.freeze_cd//60 + 1}s"

        self.screen.blit(
            self.font.render(
                f"Души: {self.score} | {d_txt} | {f_txt}", True, (255, 255, 255)
            ),
            (20, 45),
        )

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()