import pyautogui

from settings import *


def dot_in_rectangle(rect: pg.Rect, dot: tuple) -> bool:
    x_rect, y_rect, w, h = rect
    x_mouse, y_mouse = dot
    if x_rect < x_mouse < x_rect + w and y_rect < y_mouse < y_rect + h:
        return True
    return False


class Button:
    def __init__(self, position, text, action, color=(255, 0, 0), width=0, height=0, font_size=25, border=2, **kwargs):
        self.position = position
        self._border = border
        self.text = text
        self.color = color
        self._font_color = color
        self.font_size = font_size
        self._font = pg.font.Font(None, font_size)
        self._txt_surface = self._font.render(text, True, self._font_color)
        self.width = width
        self.height = height
        if width < self._txt_surface.get_width() + 10:
            self.width = self._txt_surface.get_width() + 10
        if height < self._txt_surface.get_height() + 10:
            self.height = self._txt_surface.get_height() + 10
        self.action = action
        self.kwargs = kwargs

    def draw(self, surface: pg.surface):
        rect = pg.Rect(*self.position, self.width, self.height)
        x, y = pyautogui.position()
        if dot_in_rectangle(rect, (x, y)):
            self._font_color = (0, 0, 0)
            self._txt_surface = self._font.render(self.text, True, self._font_color)
            pg.draw.rect(surface, rect=rect, color=self.color, width=0)
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    left, _, _ = pg.mouse.get_pressed()
                    if left:
                        self.action(**self.kwargs)
        else:
            self._font_color = self.color
            self._txt_surface = self._font.render(self.text, True, self._font_color)
            pg.draw.rect(surface, rect=rect, color=self.color, width=2)
        surface.blit(self._txt_surface, (rect.x + (self.width - self._txt_surface.get_width()) / 2,
                                         rect.y + (self.height - self._txt_surface.get_height()) / 2))


class ColouredText:
    def __init__(self, position, text, color, font_size, width_center=False, height_center=False):
        self.position = position
        self.text = text
        self.color = color
        self.font_size = font_size
        self._font = pg.font.Font(None, font_size)
        self.width = self._font.render(text, True, (0, 0, 0)).get_width()
        self.height = self._font.render(text, True, (0, 0, 0)).get_height()
        if width_center:
            self.position = ((WIDTH - self.width) // 2, self.position[1])
        if height_center:
            self.position = (self.position[0], (HEIGHT - self.height) // 2)

    def draw(self, surface: pg.surface):
        if type(self.color[0]) == tuple:
            last_width = 0
            for idx, symbol in enumerate(self.text):
                txt_surface = self._font.render(symbol, True, self.color[idx])
                surface.blit(txt_surface, (self.position[0] + last_width, self.position[1]))
                last_width += txt_surface.get_width()
        else:
            txt_surface = self._font.render(self.text, True, self.color)
            surface.blit(txt_surface, self.position)
