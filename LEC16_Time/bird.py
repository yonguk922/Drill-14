from pico2d import load_image

import game_framework


PIXEL_PER_METER = (10.0 / 0.3)

# A typical eagle's level-flight speed is about 50 km/h.
FLIGHT_SPEED_KMPH = 50.0
FLIGHT_SPEED_MPS = (FLIGHT_SPEED_KMPH * 1000.0 / 3600.0)
FLIGHT_SPEED_PPS = (FLIGHT_SPEED_MPS * PIXEL_PER_METER)

SPRITE_FRAME_COUNT = 14
WINGBEAT_DISTANCE_M = 2.5
FRAMES_PER_SECOND = (
    FLIGHT_SPEED_MPS / WINGBEAT_DISTANCE_M * SPRITE_FRAME_COUNT
)

FRAME_WIDTH = 183
FRAME_HEIGHT = 168
DRAW_WIDTH = 110
DRAW_HEIGHT = 101
FRAMES_PER_ROW = 5
SCREEN_WIDTH = 1600


class Bird:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0.0
        self.dir = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (
            self.frame + FRAMES_PER_SECOND * game_framework.frame_time
        ) % SPRITE_FRAME_COUNT
        self.x += self.dir * FLIGHT_SPEED_PPS * game_framework.frame_time

        edge = DRAW_WIDTH / 2
        if self.x >= SCREEN_WIDTH - edge:
            self.x = SCREEN_WIDTH - edge
            self.dir = -1
        elif self.x <= edge:
            self.x = edge
            self.dir = 1

    def draw(self):
        frame = int(self.frame)
        column = frame % FRAMES_PER_ROW
        row = frame // FRAMES_PER_ROW
        source_y = 506 - (row + 1) * FRAME_HEIGHT
        flip = '' if self.dir == 1 else 'h'
        self.image.clip_composite_draw(
            column * FRAME_WIDTH,
            source_y,
            FRAME_WIDTH,
            FRAME_HEIGHT,
            0,
            flip,
            self.x,
            self.y,
            DRAW_WIDTH,
            DRAW_HEIGHT,
        )
