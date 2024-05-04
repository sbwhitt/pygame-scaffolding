import static.colors as colors
from pygame.surface import Surface
from pygame.font import Font
from pygame.color import Color


class Text:
    def __init__(self, font: Font, font_size: int, color: Color=colors.WHITE):
        self.font = font
        self.font_size = font_size
        self.color = color
    
    def render(self, surface: Surface, text: str, pos: tuple) -> None:
        surface.blit(self.font.render(text, True, self.color), pos)
