# Logic Tung Hoành

Game giáo dục về logic và dãy số được xây dựng bằng Pygame, giúp người chơi rèn luyện tư duy logic và khả năng nhận diện các quy luật số học.

## 📋 Mô tả

Logic Tung Hoành là một game puzzle thú vị với giao diện trực quan, nơi người chơi phải tìm ra quy luật của các dãy số và điền vào ô trống. Game bao gồm:

- **5 cột dọc** với các ô màu sắc khác nhau, mỗi cột chứa một dãy số theo quy luật riêng
- **8 hàng ngang** với các ô màu sắc, mỗi hàng cũng tuân theo một quy luật số học
- Các ô sẽ di chuyển (scroll) liên tục để tạo hiệu ứng động
- Người chơi có 10 giây để quan sát trước khi được yêu cầu trả lời
- Hệ thống phản hồi âm thanh khi trả lời đúng/sai

## 🎮 Cách chơi

1. Nhấn nút **START** để bắt đầu game
2. Đếm ngược 3 giây
3. Quan sát các dãy số đang di chuyển trên màn hình trong 10 giây
4. Sau 10 giây, bảng điều khiển bên phải sẽ xuất hiện với 2 ô màu:
   - Ô thứ nhất (có thể là dọc hoặc ngang)
   - Ô thứ hai (có thể là dọc hoặc ngang)
5. Nhập số thích hợp vào ô trống (dấu `?`) tương ứng với màu và hướng của ô
6. Nhấn Enter để xác nhận câu trả lời
7. Xem kết quả với hiệu ứng "compile" - từng chữ số sẽ được hiển thị dần

## 🎯 Các loại dãy số

Game hỗ trợ nhiều loại quy luật số học:

### Dãy cơ bản
- **Cấp số cộng (Arithmetic)**: Dãy số tăng/giảm đều (VD: 100, 150, 200, 250...)
- **Cấp số nhân (Geometric)**: Dãy số nhân với tỉ số cố định (VD: 2, 8, 32, 128...)

### Dãy đặc biệt
- **Fibonacci**: Mỗi số là tổng của hai số trước đó (VD: 1, 1, 2, 3, 5, 8, 13...)
- **Lucas**: Tương tự Fibonacci nhưng bắt đầu từ 2, 1 (VD: 2, 1, 3, 4, 7, 11...)
- **Số nguyên tố (Prime)**: Các số chỉ chia hết cho 1 và chính nó (VD: 2, 3, 5, 7, 11...)

### Dãy hình học
- **Số chính phương (Square)**: n² (VD: 1, 4, 9, 16, 25...)
- **Số lập phương (Cubic)**: n³ (VD: 1, 8, 27, 64, 125...)
- **Số tam giác (Triangular)**: n(n+1)/2 (VD: 1, 3, 6, 10, 15...)

### Dãy nâng cao
- **Số Bell**: Số cách phân hoạch một tập hợp
- **Giai thừa (Factorial)**: n × n!
- **Dãy số đôi (Double Arithmetic)**: Hai cấp số cộng xen kẽ nhau (chỉ dùng cho hàng ngang)

## 🚀 Cài đặt

### Yêu cầu hệ thống
- Python 3.7+
- Pygame

### Cài đặt thư viện

```bash
pip install pygame
```

### Chạy game

```bash
cd logic_tung_hoanh
python main.py
```

## 🎨 Cấu trúc dự án

```
logic_tung_hoanh/
├── main.py                 # Entry point của game
├── config.py               # Cấu hình game (màu sắc, kích thước, FPS...)
├── assets/                 # Tài nguyên âm thanh
│   ├── correct.ogg        # Âm thanh khi trả lời đúng
│   └── wrong.ogg          # Âm thanh khi trả lời sai
└── scripts/
    ├── core/              # Logic game chính
    │   ├── game.py        # Game loop và window management
    │   ├── main_scene.py  # Scene chính của game
    │   ├── pattern_manager.py  # Quản lý sinh dãy số ngẫu nhiên
    │   └── scene.py       # Abstract scene class
    ├── data/              # Dữ liệu và patterns
    │   ├── number_pattern.py      # Abstract pattern class
    │   └── patterns/              # Các loại dãy số cụ thể
    │       ├── arithmetic.py      # Cấp số cộng
    │       ├── geometric.py       # Cấp số nhân
    │       ├── fibonacci.py       # Dãy Fibonacci
    │       ├── lucas.py           # Dãy Lucas
    │       ├── prime.py           # Số nguyên tố
    │       ├── square.py          # Số chính phương
    │       ├── cubic.py           # Số lập phương
    │       ├── triangle.py        # Số tam giác
    │       ├── bell.py            # Số Bell
    │       ├── factorial.py       # Giai thừa
    │       ├── double_arithmetic.py  # Dãy số đôi
    │       └── prime_progression.py
    ├── entities/          # Các thực thể game
    │   ├── grid_cells.py  # Ô lưới di chuyển
    │   └── input_box.py   # Ô nhập liệu
    ├── systems/           # Các hệ thống layout
    │   └── grid_layout.py # Tính toán vị trí lưới
    └── ui/                # Giao diện người dùng
        └── side_panel.py  # Bảng điều khiển bên phải
```

## 🔧 Cấu hình

Có thể tùy chỉnh game thông qua file `config.py`:

- **Cửa sổ**: Kích thước 1920x1080, FPS 60
- **Màn hình game**: 1600x1000 (vùng chính)
- **Tốc độ cuộn**: 
  - Dọc: 120 px/s
  - Ngang: 150 px/s
- **Số lượng ô**:
  - 5 cột dọc, mỗi cột 9 ô
  - 8 hàng ngang, mỗi hàng 8 ô
- **Màu sắc**: 9 màu cho dọc, 8 màu cho ngang

## 🎓 Mở rộng

### Thêm pattern mới

Để thêm một loại dãy số mới:

1. Tạo file mới trong `scripts/data/patterns/`
2. Kế thừa từ class `NumberPattern`
3. Implement các method:
   - `generate(count)`: Sinh ra `count` số trong dãy
   - `describe()`: Mô tả dãy số
   - `random_instance()`: Tạo instance ngẫu nhiên với tham số ngẫu nhiên

Ví dụ:

```python
import random
from scripts.data.number_pattern import NumberPattern

class MyPattern(NumberPattern):
    def __init__(self, param):
        self.param = param

    def generate(self, count):
        return [i * self.param for i in range(count)]

    def describe(self):
        return 'My Pattern (param: {})'.format(self.param)

    @classmethod
    def random_instance(cls):
        param = random.randint(1, 10)
        return cls(param=param)
```

Pattern sẽ tự động được load và sử dụng trong game!

## 📝 Ghi chú kỹ thuật

- **Architecture**: ECS-inspired (Entity-Component-System)
- **Game States**: START → COUNTDOWN → PLAYING → COMPILE
- **Scroll Logic**: Sử dụng modulo để tạo hiệu ứng cuộn vô hạn
- **Layout System**: Tính toán động vị trí các ô dựa trên config
- **Pattern Loading**: Dynamic loading sử dụng `importlib` và `inspect`

## 📄 License

Dự án mã nguồn mở, tự do sử dụng và chỉnh sửa.

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo Pull Request hoặc Issue nếu bạn có ý tưởng cải thiện game.

---

**Chúc bạn chơi game vui vẻ và rèn luyện tư duy logic hiệu quả! 🧠✨**
