import pygame.mouse as mouse
import static.inp_codes as inp_codes

class Mouse:
    def __init__(self) -> None:
        self.down: dict[int, bool] = {}
        self.wheel: tuple[bool, bool] = (False, False) # (up, down)

    def get_pos(self) -> tuple[int, int]:
        return mouse.get_pos()

    def is_down(self, button: int) -> None:
        return self.down.get(button)

    def handle_down(self, button: int) -> None:
        if button == inp_codes.WHEEL_UP:
            self.set_wheel_up(True)
        elif button == inp_codes.WHEEL_DOWN:
            self.set_wheel_down(True)
        if not self.down.get(button) or not self.down[button]:
            self.down[button] = True

    def handle_up(self, button: int) -> None:
        if not self.down.get(button) or self.down[button]:
            self.down[button] = False

    def set_wheel_up(self, active: bool) -> None:
        self.wheel = (active, self.wheel[1])

    def set_wheel_down(self, active: bool) -> None:
        self.wheel = (self.wheel[0], active)

    def consume_wheel_up(self) -> bool:
        ret = self.wheel[0]
        self.set_wheel_up(False)
        return ret

    def consume_wheel_down(self) -> bool:
        ret = self.wheel[1]
        self.set_wheel_down(False)
        return ret
