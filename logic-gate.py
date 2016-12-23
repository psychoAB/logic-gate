#!/usr/bin/python3

import arcade
from gate import INPUT_GATE, OUTPUT_GATE, NOT_GATE, AND_GATE, OR_GATE, IMAGE_FILENAME, InputGateSprite, OutputGateSprite, NotGateSprite, AndGateSprite, OrGateSprite

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
        main_or_gate = OrGateSprite(x = 350, y = 89, world = self)

        self.main_gate_sprites = [None, None, None, None, None]
        self.main_gate_sprites[INPUT_GATE] = main_input_gate
        self.main_gate_sprites[OUTPUT_GATE] = main_output_gate
        self.main_gate_sprites[NOT_GATE] = main_not_gate
        self.main_gate_sprites[AND_GATE] = main_and_gate
        self.main_gate_sprites[OR_GATE] = main_or_gate

        self.dragging = False

    def on_draw(self):
        arcade.start_render()

        for main_gate_sprite in self.main_gate_sprites:
            if main_gate_sprite != None:
                main_gate_sprite.draw()

        for gate_sprite in self.gate_sprites:
            gate_sprite.update()
            gate_sprite.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        #print(str(x) + " " + str(y))
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragging:
            for gate_sprite in self.gate_sprites:
                if gate_sprite.is_mouse_on(x, y):
                    gate_sprite.set_position(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging = True

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

            for gate_sprite in self.gate_sprites:
                if gate_sprite.gate_type == INPUT_GATE and gate_sprite.is_mouse_on(x, y):
                    gate_sprite.output = not gate_sprite.output

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging = False

if __name__ == '__main__':
    window = LogicGateGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
