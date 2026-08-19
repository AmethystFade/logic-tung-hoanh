import pygame

import config
from scripts.core.scene import Scene
from scripts.systems import grid_layout
from scripts.ui.side_panel import SidePanel
from scripts.core.pattern_manager import PatternManager


class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.main_screen = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        self.font = pygame.font.SysFont(config.FONT_NAME, config.FONT_SIZE)
        self.large_font = pygame.font.SysFont(config.FONT_NAME, 60)

        self.pattern_manager = PatternManager()
        self.v_sequences, self.h_sequences, self.v_answers, self.h_answers = self.pattern_manager.generate_all_patterns()

        # Lấy danh sách entities từ system layout (chỉ tính 1 lần lúc khởi tạo)
        self.vertical_columns = grid_layout.build_vertical_columns(self.v_sequences, self.font)
        self.horizontal_rows = grid_layout.build_horizontal_rows(self.h_sequences, self.font)

        self.side_panel = SidePanel(self.font, self.on_submit, self.v_answers, self.h_answers)
        
        self.state = "START"
        self.countdown_timer = 3.0
        self.playing_timer = 0.0
        
        # Level system
        self.current_level = 0  # 0-4 for 5 levels
        self.total_score = 0
        self.current_speed_multiplier = config.LEVEL_SPEEDS[0]
        
        self.compile_state = 0
        self.compile_timer = 0.0
        self.compile_digit_idx = 0
        self.ans1_revealed = ""
        self.ans2_revealed = ""
        self.user_ans1 = 0
        self.correct_ans1 = 0
        self.user_ans2 = 0
        self.correct_ans2 = 0

        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(current_dir, "..", "..", "assets")
        self.correct_sound = pygame.mixer.Sound(os.path.join(assets_dir, "correct.ogg"))
        self.wrong_sound = pygame.mixer.Sound(os.path.join(assets_dir, "wrong.ogg"))
        
        btn_w, btn_h = 200, 80
        self.start_btn_rect = pygame.Rect(
            (config.SCREEN_WIDTH - btn_w) // 2,
            (config.SCREEN_HEIGHT - btn_h) // 2,
            btn_w, btn_h
        )

    def _draw_compile_screen(self):
        """Vẽ màn hình đáp án với 2 dãy đề bài và đáp án reveal trong ô"""
        # Get sequences based on which boxes were selected
        if self.compile_box1_is_vertical:
            seq1 = self.v_sequences[self.compile_box1_color]
            length1 = config.NUM_COLS
        else:
            seq1 = self.h_sequences[self.compile_box1_color]
            length1 = config.NUM_H_ROWS
            
        if self.compile_box2_is_vertical:
            seq2 = self.v_sequences[self.compile_box2_color]
            length2 = config.NUM_COLS
        else:
            seq2 = self.h_sequences[self.compile_box2_color]
            length2 = config.NUM_H_ROWS
        
        # Draw sequence 1 (upper half)
        y1 = config.SCREEN_HEIGHT // 4
        self._draw_sequence_row(seq1, length1, y1, self.compile_box1_color, 
                               self.compile_box1_is_vertical, self.ans1_revealed, 
                               self.user_ans1, self.correct_ans1)
        
        # Draw sequence 2 (lower half)
        y2 = config.SCREEN_HEIGHT * 3 // 4
        self._draw_sequence_row(seq2, length2, y2, self.compile_box2_color,
                               self.compile_box2_is_vertical, self.ans2_revealed,
                               self.user_ans2, self.correct_ans2)
        
        # Show score for this level
        score_text = self.large_font.render("Level {} Score: +{}".format(
            self.current_level + 1, self.level_score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(config.SCREEN_WIDTH//2, 50))
        self.main_screen.blit(score_text, score_rect)

    def _draw_sequence_row(self, sequence, length, center_y, color, is_vertical, 
                          revealed_answer, user_answer, correct_answer):
        """Vẽ một dãy số với ô trống ở giữa hiện đáp án"""
        # Determine box size
        if is_vertical:
            box_w, box_h = config.V_RECT_WIDTH, config.V_RECT_HEIGHT
        else:
            box_w, box_h = config.H_RECT_WIDTH, config.H_RECT_HEIGHT
        
        gap = 20
        total_width = length * box_w + (length - 1) * gap
        start_x = (config.SCREEN_WIDTH - total_width) // 2
        
        for i in range(length):
            x = start_x + i * (box_w + gap)
            y = center_y - box_h // 2
            rect = pygame.Rect(x, y, box_w, box_h)
            
            # Draw box
            pygame.draw.rect(self.main_screen, color, rect)
            pygame.draw.rect(self.main_screen, config.COLOR_RECT_BORDER, rect, 2)
            
            # Draw content
            val = sequence[i]
            if val == "?":
                # This is the answer box - show revealed answer
                if revealed_answer:
                    text_surf = self.font.render(revealed_answer, True, (255, 255, 255))
                else:
                    text_surf = self.font.render("?", True, (255, 255, 255))
                text_rect = text_surf.get_rect(center=rect.center)
                self.main_screen.blit(text_surf, text_rect)
                
                # Show user answer below the box
                if user_answer is not None:
                    user_text = self.font.render("User: {}".format(user_answer), True, (255, 255, 0))
                    user_rect = user_text.get_rect(center=(rect.centerx, rect.bottom + 30))
                    self.main_screen.blit(user_text, user_rect)
            else:
                # Regular number
                text_surf = self.font.render(str(val), True, (255, 255, 255))
                text_rect = text_surf.get_rect(center=rect.center)
                self.main_screen.blit(text_surf, text_rect)

    def on_submit(self, u1, c1, u2, c2):
        self.state = "COMPILE"
        self.user_ans1 = u1
        self.correct_ans1 = c1
        self.user_ans2 = u2
        self.correct_ans2 = c2
        self.compile_state = 1
        self.compile_timer = 0.0
        self.compile_digit_idx = 0
        self.ans1_revealed = ""
        self.ans2_revealed = ""
        
        # Store which sequences to show
        self.compile_box1_color = self.side_panel.box1_color
        self.compile_box1_is_vertical = self.side_panel.box1_is_vertical
        self.compile_box2_color = self.side_panel.box2_color
        self.compile_box2_is_vertical = self.side_panel.box2_is_vertical
        
        # Calculate score for this level
        correct_count = 0
        if u1 == c1:
            correct_count += 1
        if u2 == c2:
            correct_count += 1
        
        level_base_score = config.LEVEL_SCORES[self.current_level]
        if correct_count == 2:
            self.level_score = level_base_score
        elif correct_count == 1:
            self.level_score = level_base_score / 2.0
        else:
            self.level_score = 0
        
        self.total_score += self.level_score

    def handle_event(self, event):
        if self.state == "START":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                ms_x, ms_y = mx - config.SCREEN_X, my - config.SCREEN_Y
                if self.start_btn_rect.collidepoint((ms_x, ms_y)):
                    self.state = "COUNTDOWN"
            elif event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.state = "COUNTDOWN"
        elif self.state == "PLAYING":
            self.side_panel.handle_event(event)

    def update(self, dt):
        dt_ms = dt * 1000.0

        if self.state == "START":
            pass
        elif self.state == "COUNTDOWN":
            self.countdown_timer -= dt
            if self.countdown_timer <= 0:
                self.state = "PLAYING"
        elif self.state == "PLAYING":
            self.playing_timer += dt
            if self.playing_timer >= 10.0 and not self.side_panel.visible:
                self.side_panel.randomize_boxes()
                self.side_panel.visible = True

            v_speed = config.V_SPEED * self.current_speed_multiplier
            h_speed = config.H_SPEED * self.current_speed_multiplier
            
            for column in self.vertical_columns:
                column.update(dt, v_speed)

            for row in self.horizontal_rows:
                row.update(dt, h_speed)

            self.side_panel.update(dt_ms)
            
        elif self.state == "COMPILE":
            self.compile_timer += dt
            if self.compile_state == 1:
                ans_str = str(self.correct_ans1)
                if self.compile_timer >= 0.5:  # 0.5 giây mỗi digit
                    self.compile_timer = 0.0
                    self.ans1_revealed += ans_str[self.compile_digit_idx]
                    self.compile_digit_idx += 1
                    
                    if self.compile_digit_idx >= len(ans_str):
                        if int(self.ans1_revealed) == self.user_ans1:
                            self.correct_sound.play()
                        else:
                            self.wrong_sound.play()
                        self.compile_state = 2
                        self.compile_digit_idx = 0
                        self.compile_timer = -1.0
                        
            elif self.compile_state == 2:
                ans_str = str(self.correct_ans2)
                if self.compile_timer >= 0.5:  # 0.5 giây mỗi digit
                    self.compile_timer = 0.0
                    self.ans2_revealed += ans_str[self.compile_digit_idx]
                    self.compile_digit_idx += 1
                    
                    if self.compile_digit_idx >= len(ans_str):
                        if int(self.ans2_revealed) == self.user_ans2:
                            self.correct_sound.play()
                        else:
                            self.wrong_sound.play()
                        self.compile_state = 3
                        self.compile_timer = 0.0  # Reset về 0 để đếm lại từ đầu
                        
            elif self.compile_state == 3:
                # Wait 3 seconds then move to next level or end
                if self.compile_timer >= 3.0:
                    self.current_level += 1
                    if self.current_level >= len(config.LEVEL_SPEEDS):
                        # Game over
                        self.state = "GAME_OVER"
                    else:
                        # Next level
                        self.current_speed_multiplier = config.LEVEL_SPEEDS[self.current_level]
                        self.state = "COUNTDOWN"
                        self.countdown_timer = 3.0
                        self.playing_timer = 0.0
                        self.side_panel.visible = False
                        
                        # Reset input boxes
                        self.side_panel.red_input.text = ""
                        self.side_panel.green_input.text = ""
                        
                        # Generate new patterns
                        self.v_sequences, self.h_sequences, self.v_answers, self.h_answers = self.pattern_manager.generate_all_patterns()
                        self.side_panel.v_answers = self.v_answers
                        self.side_panel.h_answers = self.h_answers
                        
                        # Rebuild grid with new sequences
                        self.vertical_columns = grid_layout.build_vertical_columns(self.v_sequences, self.font)
                        self.horizontal_rows = grid_layout.build_horizontal_rows(self.h_sequences, self.font)

    def draw(self, window):
        self.main_screen.fill(config.COLOR_SCREEN_BG)

        if self.state == "START":
            pygame.draw.rect(self.main_screen, (100, 200, 100), self.start_btn_rect)
            text_surf = self.large_font.render("START", True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=self.start_btn_rect.center)
            self.main_screen.blit(text_surf, text_rect)
        elif self.state == "COUNTDOWN":
            text_surf = self.large_font.render(str(int(self.countdown_timer) + 1), True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2))
            self.main_screen.blit(text_surf, text_rect)
            
            # Show level and score
            level_text = self.font.render("Level: {}/5".format(self.current_level + 1), True, (255, 255, 255))
            self.main_screen.blit(level_text, (20, 20))
            score_text = self.font.render("Score: {}".format(self.total_score), True, (255, 255, 255))
            self.main_screen.blit(score_text, (20, 60))
            
        elif self.state == "PLAYING":
            # Vẽ hàng ngang trước (dưới cùng), cột dọc sau (đè lên nếu chồng nhau)
            for row in self.horizontal_rows:
                row.draw(self.main_screen, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

            for column in self.vertical_columns:
                column.draw(self.main_screen, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
            
            # Show level and score
            level_text = self.font.render("Level: {}/5".format(self.current_level + 1), True, (255, 255, 255))
            self.main_screen.blit(level_text, (20, 20))
            score_text = self.font.render("Score: {}".format(self.total_score), True, (255, 255, 255))
            self.main_screen.blit(score_text, (20, 60))
            
        elif self.state == "COMPILE":
            # Không vẽ các box di chuyển nữa, chỉ vẽ 2 dãy đề bài
            self._draw_compile_screen()
            
        elif self.state == "GAME_OVER":
            text_surf = self.large_font.render("GAME OVER", True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2 - 100))
            self.main_screen.blit(text_surf, text_rect)
            
            score_surf = self.large_font.render("Total Score: {}".format(self.total_score), True, (255, 255, 255))
            score_rect = score_surf.get_rect(center=(config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2))
            self.main_screen.blit(score_surf, score_rect)

        window.blit(self.main_screen, (config.SCREEN_X, config.SCREEN_Y))

        if self.state == "PLAYING":
            self.side_panel.draw(window)
