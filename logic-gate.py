#!/usr/bin/python3

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SpriteModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)

        self.set_position(kwargs['x'], kwargs['y'])

        sprite_texture = self.textures[0]

        self.update()

    def update(self):
        super().update()

        sprite_texture = self.textures[0]

        self.texture_left_margin = self.center_x - sprite_texture.width / 2
        self.texture_right_margin = self.center_x + sprite_texture.width / 2
        self.texture_down_margin = self.center_y - sprite_texture.height / 2
        self.texture_up_margin = self.center_y + sprite_texture.height / 2
        
    def is_mouse_on(self, x, y):
        self.update()
        return x >= self.texture_left_margin and x <= self.texture_right_margin and y >= self.texture_down_margin and y <= self.texture_up_margin

class LogicGateGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE) 

        self.main_or_gate = SpriteModel('images/or_gate.png', x = 100, y = 100)

        self.or_gate_sprites = []
        self.dragging = False

    def on_draw(self):
        arcade.start_render()

        self.main_or_gate.draw()

        for or_gate_sprite in self.or_gate_sprites:
            or_gate_sprite.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        #print(str(x) + " " + str(y))
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragging:
            for or_gate_sprite in self.or_gate_sprites:
                if or_gate_sprite.is_mouse_on(x, y):
                    or_gate_sprite.set_position(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging = True

            if self.main_or_gate.is_mouse_on(x, y):
                new_or_gate = SpriteModel('images/or_gate.png', x = x , y = y)
                self.or_gate_sprites.append(new_or_gate)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging = False

if __name__ == '__main__':
    window = LogicGateGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
