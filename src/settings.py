class Settings:
    def __init__(self) -> None:
        self.win_size: tuple[int, int] = (1080, 720)
        self.frame_rate: int = 60
        self.font_size = 16

    def get_win_size(self) -> tuple[int, int]:
        return self.win_size

    def get_win_width(self) -> int:
        return self.win_size[0]

    def get_win_height(self) -> int:
        return self.win_size[1]

    def get_font_size(self) -> int:
        return self.font_size
