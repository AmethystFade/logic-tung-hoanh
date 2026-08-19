import pygame
import config


class GridCell:
    """
    Một dải ô cycle theo 1 trục (dọc hoặc ngang).

    axis: "vertical"   -> dải ô xếp dọc tại 1 vị trí x cố định, cuộn theo y
          "horizontal" -> dải ô xếp ngang tại 1 vị trí y cố định, cuộn theo x
    """

    def __init__(self, axis, fixed_pos, rect_size, gap, direction, colors, index, sequences, font):
        self.axis = axis
        self.fixed_pos = fixed_pos      # x cố định (nếu vertical) hoặc y cố định (nếu horizontal)
        self.rect_width, self.rect_height = rect_size
        self.gap = gap
        self.direction = direction      # +1 hoặc -1
        self.colors = colors
        self.index = index              # col_index for vertical, row_index for horizontal
        self.sequences = sequences
        self.font = font

        self.scroll_offset = 0.0

        if axis == "vertical":
            self.period = self.rect_height + self.gap
        else:
            self.period = self.rect_width + self.gap

    def set_period_count(self, count):
        """Đặt số lượng ô trong 1 chu kỳ, dùng để tính period tổng (cho cycle mượt)."""
        if self.axis == "vertical":
            self.period = count * (self.rect_height + self.gap)
        else:
            self.period = count * (self.rect_width + self.gap)

    def update(self, dt, speed):
        self.scroll_offset = (self.scroll_offset + speed * dt) % self.period

    def draw(self, surface, visible_width, visible_height):
        """Vẽ tất cả các bản sao của ô cần thiết để phủ kín vùng hiển thị."""
        offset = (self.scroll_offset * self.direction) % self.period

        if self.axis == "vertical":
            self._draw_vertical(surface, visible_height, offset)
        else:
            self._draw_horizontal(surface, visible_width, offset)

    def _draw_vertical(self, surface, visible_height, offset):
        base_y = -offset
        y = base_y - self.period
        k = -int(self.period // (self.rect_height + self.gap))
        while y < visible_height + self.rect_height:
            rect = pygame.Rect(self.fixed_pos, round(y), self.rect_width, self.rect_height)
            if rect.bottom > 0 and rect.top < visible_height:
                color = self.colors[k % len(self.colors)]
                self._draw_rect(surface, rect, color)
            y += self.rect_height + self.gap
            k += 1

    def _draw_horizontal(self, surface, visible_width, offset):
        base_x = -offset
        x = base_x - self.period
        k = -int(self.period // (self.rect_width + self.gap))
        while x < visible_width + self.rect_width:
            rect = pygame.Rect(round(x), self.fixed_pos, self.rect_width, self.rect_height)
            if rect.right > 0 and rect.left < visible_width:
                color = self.colors[k % len(self.colors)]
                self._draw_rect(surface, rect, color)
            x += self.rect_width + self.gap
            k += 1

    def _draw_rect(self, surface, rect, color):
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, config.COLOR_RECT_BORDER, rect, 2)
        
        # Lấy giá trị tương ứng từ sequence
        val = self.sequences[color][self.index]
        text_surf = self.font.render(str(val), True, (255, 255, 255))  # Vẽ chữ màu trắng
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)
