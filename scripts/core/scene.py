from abc import ABC, abstractmethod

class Scene(ABC):
    """Lớp cha cho mọi scene. Mỗi scene tự quản lý entities/systems của mình."""

    def __init__(self, game):
        self.game = game  # tham chiếu ngược tới Game, để truy cập window, dt, v.v.

    @abstractmethod
    def handle_event(self, event):
        """Xử lý 1 pygame event (bàn phím, chuột, ...)."""
        raise NotImplementedError

    @abstractmethod
    def update(self, dt):
        """Cập nhật state của scene. dt tính bằng giây."""
        raise NotImplementedError

    @abstractmethod
    def draw(self, window):
        """Vẽ scene lên cửa sổ chính (pygame.Surface của window)."""
        raise NotImplementedError