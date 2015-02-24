import sys

import pygame
from pygame.locals import *

import simulator as sim
import morg_factory as mf
import morg_reader as mr

pygame.init()

WIDTH = 800
HEIGHT = 600

INPUT_FILE = 'input.txt'

# set up the pygame window
DISPLAY_SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Micro Organism Simulator')

simulator = sim.Simulator(WIDTH, HEIGHT, DISPLAY_SURFACE)
factory = mf.MorgFactory()
reader = mr.MorgReader(factory, INPUT_FILE)

clock = pygame.time.Clock()

morg_list = reader.read_morgs()
for morg in morg_list:
    simulator.add_morg(morg)

# run the event handle loop
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    simulator.simulate_one_step()
    pygame.display.update()

