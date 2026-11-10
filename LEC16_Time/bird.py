from pico2d import load_image

import game_framework


PIXEL_PER_METER = (10.0 / 0.3)

# Typical level-flight speed is about 32-48 km/h, so use the midpoint.
FLIGHT_SPEED_KMPH = 40.0
FLIGHT_SPEED_MPS = (FLIGHT_SPEED_KMPH * 1000.0 / 3600.0)
FLIGHT_SPEED_PPS = (FLIGHT_SPEED_MPS * PIXEL_PER_METER)

SPRITE_FRAME_COUNT = 14
WINGBEAT_DISTANCE_M = 2.5
FRAMES_PER_SECOND = (
    FLIGHT_SPEED_MPS / WINGBEAT_DISTANCE_M * SPRITE_FRAME_COUNT
)

FRAME_WIDTH = 183
FRAME_HEIGHT = 168
FRAMES_PER_ROW = 5


class Bird:
    def __init__(self):
        self.x, self.y = 1200, 400
        self.frame = 0.0
        self.dir = -1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (
            self.frame + FRAMES_PER_SECOND * game_framework.frame_time
        ) % SPRITE_FRAME_COUNT
        self.x += self.dir * FLIGHT_SPEED_PPS * game_framework.frame_time

        if self.x < -FRAME_WIDTH:
            self.x = 1600 + FRAME_WIDTH

    def draw(self):
        frame = int(self.frame)
        column = frame % FRAMES_PER_ROW
        row = frame // FRAMES_PER_ROW
        source_y = 506 - (row + 1) * FRAME_HEIGHT
        self.image.clip_draw(
            column * FRAME_WIDTH,
            source_y,
            FRAME_WIDTH,
            FRAME_HEIGHT,
            self.x,
            self.y,
        )
