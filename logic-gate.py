#!/usr/bin/python3

import sys
import arcade
from gate import INPUT_GATE, OUTPUT_GATE, NOT_GATE, AND_GATE, OR_GATE, IMAGE_FILENAME, InputGateSprite, OutputGateSprite, NotGateSprite, AndGateSprite, OrGateSprite, SpriteModel

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class LogicGateGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE) 

        self.gate_sprites = []

        main_input_gate = InputGateSprite(x = 50, y = 100, world = self)
        main_output_gate = OutputGateSprite(x = 125, y = 89, world = self)
        main_not_gate = NotGateSprite(x = 200, y = 100, world = self)
        main_and_gate = AndGateSprite(x = 275, y = 100, world = self)
        main_or_gate = OrGateSprite(x = 350, y = 100, world = self)

        self.how_to_play_button = SpriteModel('images/how_to_play_button.png', x = 490, y = 100, world = self)
        self.how_to_play = SpriteModel('images/how_to_play.png', x = 300, y = 400, world = self)

        self.main_gate_sprites = [None, None, None, None, None]
        self.main_gate_sprites[INPUT_GATE] = main_input_gate
        self.main_gate_sprites[OUTPUT_GATE] = main_output_gate
        self.main_gate_sprites[NOT_GATE] = main_not_gate
        self.main_gate_sprites[AND_GATE] = main_and_gate
        self.main_gate_sprites[OR_GATE] = main_or_gate

        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.dragging = False

    def on_draw(self):
        arcade.start_render()

        for main_gate_sprite in self.main_gate_sprites:
            if main_gate_sprite != None:
                main_gate_sprite.draw()

        for gate_sprite in self.gate_sprites:
            gate_sprite.update()
            gate_sprite.draw()
            if gate_sprite.gate_type == INPUT_GATE:
                arcade.draw_text(str(gate_sprite.output), gate_sprite.center_x - 20, gate_sprite.center_y - 50, arcade.color.BLACK)
            if gate_sprite.gate_type == OUTPUT_GATE:
                arcade.draw_text(str(gate_sprite.down_input), gate_sprite.center_x - 20, gate_sprite.center_y + 40, arcade.color.BLACK)

        self.how_to_play_button.draw()
        if self.how_to_play_button.is_mouse_on(self.x, self.y):
            self.how_to_play.draw()
                
        arcade.draw_text('input', 30, 35, arcade.color.BLACK)
        arcade.draw_text('output', 105, 35, arcade.color.BLACK)
        arcade.draw_text('not', 190, 35, arcade.color.BLACK)
        arcade.draw_text('and', 265, 35, arcade.color.BLACK)
        arcade.draw_text('or', 340, 35, arcade.color.BLACK)
        arcade.draw_text('tools', 180, 10, arcade.color.BLACK)

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y

        if DEBUG:
            print(str(x) + " " + str(y))
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == arcade.MOUSE_BUTTON_LEFT:
            self.dragging = False

            for gate_sprite in self.gate_sprites:
                if gate_sprite.is_mouse_on(x, y) and not self.dragging:
                    gate_sprite.set_position(x, y)
                    self.dragging = True

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for main_gate_sprite in self.main_gate_sprites:
                if main_gate_sprite != None:
                    if main_gate_sprite.is_mouse_on(x, y):
                        if main_gate_sprite.gate_type == INPUT_GATE:
                            new_gate = InputGateSprite(x = x , y = y, world = self)
                        if main_gate_sprite.gate_type == OUTPUT_GATE:
                            new_gate = OutputGateSprite(x = x, y = y, world = self)
                        if main_gate_sprite.gate_type == NOT_GATE:
                            new_gate = NotGateSprite(x = x, y = y, world = self)
                        if main_gate_sprite.gate_type == AND_GATE:
                            new_gate = AndGateSprite(x = x, y = y, world = self)
                        if main_gate_sprite.gate_type == OR_GATE:
                            new_gate = OrGateSprite(x = x , y = y, world = self)
                        self.gate_sprites.append(new_gate)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            for gate_sprite in self.gate_sprites:
                if gate_sprite.is_mouse_on(x, y):
                    self.gate_sprites.remove(gate_sprite)

        if button == arcade.MOUSE_BUTTON_MIDDLE:
            for gate_sprite in self.gate_sprites:
                if gate_sprite.gate_type == INPUT_GATE and gate_sprite.is_mouse_on(x, y):
                    gate_sprite.output = not gate_sprite.output

    def on_mouse_release(self, x, y, button, modifiers):
        pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        DEBUG = sys.argv[1]
    else:
        DEBUG = False

    window = LogicGateGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
