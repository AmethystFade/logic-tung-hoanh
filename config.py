WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
WINDOW_TITLE = "Logic Tung Hoanh"

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 1000
SCREEN_X = 20   # cách biên trái window 20px
SCREEN_Y = 40   # cách biên trên window 40px

FPS = 60

V_RECT_WIDTH, V_RECT_HEIGHT = 90, 180
NUM_COLS = 5
NUM_V_RECTS_PER_COL = 9

SIDE_MARGIN = 35     # cách biên trái/phải của screen
COL_GAP = 270        # khoảng cách giữa các cột (edge-to-edge)
V_ROW_GAP = 20        # khoảng cách giữa các ô trong 1 cột (edge-to-edge)

# V_SPEED sẽ thay đổi theo màn chơi, mặc định cho màn 1
V_SPEED = 120         # tốc độ cuộn dọc (px/giây)

# ============================================================
# Level system - 5 màn chơi với tốc độ tăng dần
# ============================================================
LEVEL_SPEEDS = [0.75, 1.25, 1.75, 2.5, 3.0]  # Multiplier cho tốc độ mỗi màn
LEVEL_SCORES = [1, 2, 3, 4, 5]  # Điểm số mỗi màn (đúng cả 2), đúng 1 nửa = một nửa điểm

# Vùng dọc "cũ" (5 ô, dùng làm mốc căn giữa cho layout & cho khối ô ngang fit-to)
OLD_NUM_ROWS = 5
OLD_TOTAL_COL_HEIGHT = (OLD_NUM_ROWS * V_RECT_HEIGHT) + ((OLD_NUM_ROWS - 1) * V_ROW_GAP)  # 980

# ============================================================
# Hàng ngang (horizontal rects) — nằm trong các khoảng trống giữa cột dọc
# ============================================================
H_RECT_WIDTH, H_RECT_HEIGHT = 180, 90
NUM_H_RECTS_PER_ROW = 8
NUM_H_ROWS = 8

H_SIDE_MARGIN = 45    # cách đều 2 cột dọc bên cạnh (dùng khi tính layout ban đầu)
H_GAP_X = 20          # khoảng cách ngang giữa các ô khi cycle
H_SPEED = 150         # tốc độ cuộn ngang (px/giây)

# ============================================================
# Khu vực bên phải (ngoài main_screen): ô đỏ dọc + ô xanh lá ngang
# ============================================================
TEXTBOX_WIDTH, TEXTBOX_HEIGHT = 120, 40
GAP_BELOW_RECT = 20   # khoảng cách giữa ô hình chữ nhật và text box bên dưới nó

# ============================================================
# Màu sắc
# ============================================================
COLOR_WINDOW_BG = (30, 30, 30)
COLOR_SCREEN_BG = (60, 120, 200)

COLOR_V_RECT_FILL = (240, 240, 240)
COLOR_H_RECT_FILL = (255, 200, 80)
COLOR_RECT_BORDER = (10, 10, 10)

V_COLORS = [
    (255, 0, 0), (0, 0, 255), (0, 191, 0),
    (255, 128, 0), (0, 191, 191), (128,128,128),
    (128,0,128), (0,0,128),  (200,200,0)
]

H_COLORS = [
    (255, 0, 0),   (0, 0, 255),   (0, 191, 0),
    (255, 128, 0),  (0, 191, 191),  (128,128,128),
    (128,0,128), (0,0,128)
]

COLOR_RED_RECT = (200, 40, 40)
COLOR_GREEN_RECT = (40, 180, 80)

COLOR_INPUT_BG = (20, 20, 20)
COLOR_INPUT_INACTIVE = (200, 200, 200)
COLOR_INPUT_ACTIVE = (255, 255, 255)
COLOR_INPUT_TEXT = (255, 255, 255)

# ============================================================
# Font
# ============================================================
FONT_NAME = None   # None = dùng font hệ thống mặc định (pygame.font.SysFont)
FONT_SIZE = 28
