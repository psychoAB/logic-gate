#!/usr/bin/python3

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class LogicGateGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE) 

        self.orGate = arcade.Sprite('images/or_gate.png')
        self.orGate.set_position(100, 100)

    def on_draw(self):
        arcade.start_render()

        self.orGate.draw()

if __name__ == '__main__':
    window = LogicGateGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
