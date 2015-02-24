import sys

import pygame

import morg_factory as mf

DEFAULT_WIDTH = 50
DEFAULT_HEIGHT = 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Simulator:
    '''Simulates micro-organisms'''
    def __init__(self, width, height, display_surface):
        self.step = 0
        if width < 1 or height < 1:
            print('The dimensions must be greater than zero.')
            print('Using default values.')
            self.field_width = DEFAULT_WIDTH
            self.field_height = DEFAULT_HEIGHT
        else:
            self.field_width = width
            self.field_height = height

        self.surface = display_surface
        self.morg_list = []

    def simulate_one_step(self):
        self.step += 1
        self.surface.fill(WHITE)

        for morg in self.morg_list:
            if not morg.alive:
                self.morg_list.remove(morg)
            else:
                #if not morg.subject:
                morg.set_subject(self.nearest_morg(morg))

                morg.act(self)
                self.draw_morg(morg)

    def nearest_morg(self, morg):
        nearest = None
        current_min = sys.maxsize
        for morg2 in self.morg_list:
            if morg2.type in morg.feed_list and morg2.alive:
                distance = morg.location.distance(morg2.location)
                if distance < current_min:
                    current_min = distance
                    nearest = morg2
        return nearest

    def add_morg(self, morg):
        self.morg_list.append(morg)

    def kill(self, prey_id):
        for morg in self.morg_list:
            if morg.id == prey_id:
                morg.alive = False
                morg.remove_all_obs()

    def birth(self, morg_type, location, color, radius, feed_behavior, feed_list, reproduction):
        factory = mf.MorgFactory()
        morg = factory.create_morg(morg_type, location.x + 4, location.y + 4, color, radius, feed_behavior, feed_list,
                                   reproduction)
        self.morg_list.append(morg)


    def draw_morg(self, morg):
        pygame.draw.circle(self.surface, morg.color, (morg.location.x, morg.location.y), morg.radius)




