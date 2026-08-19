import pygame

import config
from scripts.entities.input_box import NumberInputBox


class SidePanel:
    def __init__(self, font, on_submit, v_answers, h_answers):
        self.font = font
        self.on_submit = on_submit
        self.v_answers = v_answers
        self.h_answers = h_answers
        self.box1_color = config.COLOR_RED_RECT
        self.box1_is_vertical = True
        self.box2_color = config.COLOR_GREEN_RECT
        self.box2_is_vertical = False
        self.visible = False
        
        self._layout_boxes()

    def _layout_boxes(self):
        right_area_x = config.SCREEN_X + config.SCREEN_WIDTH
        right_area_width = config.WINDOW_WIDTH - right_area_x
        right_area_y = config.SCREEN_Y
        right_area_height = config.SCREEN_HEIGHT

        upper_half_y = right_area_y
        lower_half_y = right_area_y + right_area_height // 2
        half_height = right_area_height // 2

        # ---- Ô đỏ dọc (upper half) ----
        b1_w = config.V_RECT_WIDTH if self.box1_is_vertical else config.H_RECT_WIDTH
        b1_h = config.V_RECT_HEIGHT if self.box1_is_vertical else config.H_RECT_HEIGHT

        red_rect_x = right_area_x + (right_area_width - b1_w) // 2
        red_rect_y = upper_half_y + (
            half_height - b1_h - config.GAP_BELOW_RECT - config.TEXTBOX_HEIGHT
        ) // 2
        self.red_rect = pygame.Rect(red_rect_x, red_rect_y, b1_w, b1_h)

        red_textbox_x = right_area_x + (right_area_width - config.TEXTBOX_WIDTH) // 2
        red_textbox_y = red_rect_y + b1_h + config.GAP_BELOW_RECT
        red_textbox_rect = pygame.Rect(
            red_textbox_x, red_textbox_y, config.TEXTBOX_WIDTH, config.TEXTBOX_HEIGHT
        )
        self.red_input = NumberInputBox(red_textbox_rect, self.font, on_enter=self._check_submit)

        # ---- Ô xanh lá ngang (lower half) ----
        b2_w = config.V_RECT_WIDTH if self.box2_is_vertical else config.H_RECT_WIDTH
        b2_h = config.V_RECT_HEIGHT if self.box2_is_vertical else config.H_RECT_HEIGHT

        green_rect_x = right_area_x + (right_area_width - b2_w) // 2
        green_rect_y = lower_half_y + (
            half_height - b2_h - config.GAP_BELOW_RECT - config.TEXTBOX_HEIGHT
        ) // 2
        self.green_rect = pygame.Rect(green_rect_x, green_rect_y, b2_w, b2_h)

        green_textbox_x = right_area_x + (right_area_width - config.TEXTBOX_WIDTH) // 2
        green_textbox_y = green_rect_y + b2_h + config.GAP_BELOW_RECT
        green_textbox_rect = pygame.Rect(
            green_textbox_x, green_textbox_y, config.TEXTBOX_WIDTH, config.TEXTBOX_HEIGHT
        )
        self.green_input = NumberInputBox(green_textbox_rect, self.font, on_enter=self._check_submit)

    def randomize_boxes(self):
        import random
        while True:
            self.box1_is_vertical = random.choice([True, False])
            self.box2_is_vertical = random.choice([True, False])
            
            c1_pool = config.V_COLORS if self.box1_is_vertical else config.H_COLORS
            c2_pool = config.V_COLORS if self.box2_is_vertical else config.H_COLORS
            
            self.box1_color = random.choice(c1_pool)
            self.box2_color = random.choice(c2_pool)
            
            same_dir = (self.box1_is_vertical == self.box2_is_vertical)
            same_color = (self.box1_color == self.box2_color)
            
            if not (same_dir and same_color):
                break
        
        self._layout_boxes()

    def _check_submit(self):
        v1 = self.red_input.get_value()
        v2 = self.green_input.get_value()
        if v1 is not None and v2 is not None:
            ans1 = self.v_answers[self.box1_color] if self.box1_is_vertical else self.h_answers[self.box1_color]
            ans2 = self.v_answers[self.box2_color] if self.box2_is_vertical else self.h_answers[self.box2_color]
            if self.on_submit:
                self.on_submit(v1, ans1, v2, ans2)

    def handle_event(self, event):
        if not self.visible:
            return
        
        # Xử lý Tab để chuyển đổi giữa các ô input
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            if self.red_input.active:
                self.red_input.active = False
                self.red_input.color = self.red_input.color_inactive
                self.green_input.active = True
                self.green_input.color = self.green_input.color_active
            elif self.green_input.active:
                self.green_input.active = False
                self.green_input.color = self.green_input.color_inactive
                self.red_input.active = True
                self.red_input.color = self.red_input.color_active
            else:
                # Nếu không có ô nào active, activate ô đầu tiên
                self.red_input.active = True
                self.red_input.color = self.red_input.color_active
            return
        
        self.red_input.handle_event(event)
        self.green_input.handle_event(event)

    def update(self, dt_ms):
        if not self.visible:
            return
        self.red_input.update(dt_ms)
        self.green_input.update(dt_ms)

    def draw(self, window):
        if not self.visible:
            return
        pygame.draw.rect(window, self.box1_color, self.red_rect)
        pygame.draw.rect(window, config.COLOR_RECT_BORDER, self.red_rect, 2)
        self.red_input.draw(window)

        pygame.draw.rect(window, self.box2_color, self.green_rect)
        pygame.draw.rect(window, config.COLOR_RECT_BORDER, self.green_rect, 2)
        self.green_input.draw(window)
