#!/usr/bin/python3

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class LogicGateGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE) 

        self.or_gate_sprite = arcade.Sprite('images/or_gate.png')
        self.or_gate_sprite.set_position(100, 100)

        self.dragging = False

    def on_draw(self):
        arcade.start_render()

        self.or_gate_sprite.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        print(str(x) + " " + str(y))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragging:
            self.or_gate_sprite.set_position(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        or_gate_texture = self.or_gate_sprite.textures[0]

        if button == arcade.MOUSE_BUTTON_LEFT:
            if x >= self.or_gate_sprite.center_x - or_gate_texture.width / 2 and x <= self.or_gate_sprite.center_x + or_gate_texture.width / 2:
                if y >= self.or_gate_sprite.center_y - or_gate_texture.height / 2 and y <= self.or_gate_sprite.center_y + or_gate_texture.height / 2:
                    self.dragging = True

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging = False

if __name__ == '__main__':
    window = LogicGateGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
