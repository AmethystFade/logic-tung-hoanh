import config
from scripts.entities.grid_cells import GridCell


def compute_column_x_positions():
    """Tính vị trí x của từng cột dọc (top-left x của mỗi ô trong cột)."""
    return [
        config.SIDE_MARGIN + col * (config.V_RECT_WIDTH + config.COL_GAP)
        for col in range(config.NUM_COLS)
    ]


def compute_row_y_positions():
    """
    Tính vị trí y của từng 'hàng ngang' (8 hàng, fit vừa trong
    OLD_TOTAL_COL_HEIGHT — logic giữ nguyên như bản gốc 5 ô dọc).
    """
    start_y = (config.SCREEN_HEIGHT - config.OLD_TOTAL_COL_HEIGHT) // 2

    total_h_block_height = config.NUM_H_ROWS * config.H_RECT_HEIGHT
    remaining_space = config.OLD_TOTAL_COL_HEIGHT - total_h_block_height
    h_row_gap = remaining_space / (config.NUM_H_ROWS - 1)

    return [
        start_y + round(i * (config.H_RECT_HEIGHT + h_row_gap))
        for i in range(config.NUM_H_ROWS)
    ], start_y


def build_vertical_columns(v_sequences, font):
    """Tạo danh sách GridCell cho các cột dọc, mỗi cột 1 GridCell (axis='vertical')."""
    col_x_positions = compute_column_x_positions()
    columns = []

    for col_idx, x in enumerate(col_x_positions):
        # Cột 1,3,5 (index 0,2,4) = lẻ = đi xuống (+1); cột 2,4 (index 1,3) = chẵn = đi lên (-1)
        direction = 1 if (col_idx % 2 == 0) else -1

        cell = GridCell(
            axis="vertical",
            fixed_pos=x,
            rect_size=(config.V_RECT_WIDTH, config.V_RECT_HEIGHT),
            gap=config.V_ROW_GAP,
            direction=direction,
            colors=config.V_COLORS,
            index=col_idx,
            sequences=v_sequences,
            font=font
        )
        cell.set_period_count(config.NUM_V_RECTS_PER_COL)
        columns.append(cell)

    return columns


def build_horizontal_rows(h_sequences, font):
    """Tạo danh sách GridCell cho các hàng ngang, mỗi hàng 1 GridCell (axis='horizontal')."""
    row_y_positions, _ = compute_row_y_positions()
    rows = []

    for row_idx, y in enumerate(row_y_positions):
        # Hàng 1,3,5,7 (index 0,2,4,6) = lẻ = đi phải (+1); hàng 2,4,6,8 = chẵn = đi trái (-1)
        direction = 1 if (row_idx % 2 == 0) else -1

        cell = GridCell(
            axis="horizontal",
            fixed_pos=y,
            rect_size=(config.H_RECT_WIDTH, config.H_RECT_HEIGHT),
            gap=config.H_GAP_X,
            direction=direction,
            colors=config.H_COLORS,
            index=row_idx,
            sequences=h_sequences,
            font=font
        )
        cell.set_period_count(config.NUM_H_RECTS_PER_ROW)
        rows.append(cell)

    return rows