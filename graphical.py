# Print out realtime audio volume as ascii bars

import sounddevice as sd
import numpy as np
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

duration = 100  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print('|' * int(volume_norm))

    sound_level = int(volume_norm)
    print(sound_level*5)

    screen.fill((200, 200, 200))
    pygame.draw.circle(screen, (0,0,0), (200,200), sound_level)

    # redraw the screen with the new calculations
    pygame.display.update()


with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)

