import pygame
import static.colors as colors
import static.events as events
from settings import Settings
from controls.keys import Keys
from controls.mouse import Mouse

class Game:
    def __init__(self) -> None:
        self.settings = Settings()
        self.running = True
        self.paused = False
        self.keys = Keys()
        self.mouse = Mouse()
        self.surface = pygame.display.set_mode(
            self.settings.win_size,
            pygame.RESIZABLE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()

    def on_init(self) -> None:
        pass

    def on_execute(self) -> None:
        self.on_init()

        while self.running:
            dt = self.clock.tick_busy_loop(self.settings.frame_rate)
            for event in pygame.event.get():
                self.handle_event(event)
            if not self.paused: self.update(dt)
            self.render()

        self.on_cleanup()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            self.keys.handle_down(event.key)
            self.handle_key(event.key)
        elif event.type == pygame.KEYUP:
            self.keys.handle_up(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse.handle_down(event.button)
            self.handle_mouse_buttons()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouse.handle_up(event.button)
        elif event.type == pygame.WINDOWRESIZED:
            self.settings.win_size = (event.x, event.y)
        else:
            self._handle_custom_event(event)

    def _handle_custom_event(self, event: pygame.event.Event):
        pass

    def handle_key(self, key: int) -> None:
        if key == pygame.K_ESCAPE:
            self.running = False
        elif key == pygame.K_SPACE:
            self.paused = not self.paused

    def handle_mouse_buttons(self) -> None:
        # mouse buttons: 0 == left, 1 == middle, 2 == right
        buttons = pygame.mouse.get_pressed()
        pass

    def update(self, dt: int) -> None:
        pass

    def render(self) -> None:
        self.surface.fill(colors.BLACK)
        pygame.display.flip()

    def on_cleanup(self) -> None:
        pass
