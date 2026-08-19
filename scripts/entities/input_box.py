import pygame
import config

class NumberInputBox:
    def __init__(self, rect, font, on_enter=None):
        self.rect = rect
        self.font = font
        self.text = ""
        self.active = False
        self.on_enter = on_enter

        self.color_inactive = config.COLOR_INPUT_INACTIVE
        self.color_active = config.COLOR_INPUT_ACTIVE
        self.color = self.color_inactive

        self.cursor_visible = True
        self.cursor_timer = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive

        elif event.type == pygame.KEYDOWN and self.active:
            # Bỏ qua Tab vì đã xử lý ở side_panel
            if event.key == pygame.K_TAB:
                return
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if self.on_enter:
                    self.on_enter()
            elif event.unicode.isdigit():
                self.text += event.unicode

    def update(self, dt_ms):
        self.cursor_timer += dt_ms
        if self.cursor_timer >= 500:
            self.cursor_timer = 0
            self.cursor_visible = not self.cursor_visible

    def draw(self, surface):
        pygame.draw.rect(surface, config.COLOR_INPUT_BG, self.rect)
        pygame.draw.rect(surface, self.color, self.rect, 2)

        text_surf = self.font.render(self.text, True, config.COLOR_INPUT_TEXT)
        surface.blit(
            text_surf,
            (self.rect.x + 8, self.rect.y + (self.rect.height - text_surf.get_height()) // 2),
        )

        if self.active and self.cursor_visible:
            cursor_x = self.rect.x + 8 + text_surf.get_width() + 2
            cursor_y1 = self.rect.y + 6
            cursor_y2 = self.rect.y + self.rect.height - 6
            pygame.draw.line(surface, config.COLOR_INPUT_TEXT, (cursor_x, cursor_y1), (cursor_x, cursor_y2), 2)

    def get_value(self):
        """Trả về giá trị số (int) hoặc None nếu ô đang trống."""
        return int(self.text) if self.text else None
