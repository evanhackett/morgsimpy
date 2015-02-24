from math import sqrt


class Morg:
    def __init__(self):
        self.alive = True
        self.age = 0
        self.type = 'none'
        self.location = Location(None, None)
        self.direction = [0, 0]
        self.destination = Location(None, None)
        self.color = (0, 0, 0)
        self.observer_list = []
        self.subject = None
        self.id = id(self)
        self.feed_list = []
        self.mate_list = []
        self.radius = 4
        self.feed_behavior = None
        self.reproduction_behavior = None

    def destination_direction(self):
        x, y = 0, 0
        if self.destination.x > self.location.x:
            x = 1
        elif self.destination.x < self.location.x:
            x = -1

        if self.destination.y > self.location.y:
            y = 1
        elif self.destination.y < self.location.y:
            y = -1

        return [x, y]

    def move(self, direction):
        if direction[0] < 0:
            x = self.location.x - 1
        elif self.direction[0] == 0:
            x = self.location.x
        else:
            x = self.location.x + 1

        if direction[1] < 0:
            y = self.location.y - 1
        elif self.direction[1] == 0:
            y = self.location.y
        else:
            y = self.location.y + 1
        self.location = Location(x, y)

    def register_obs(self, obs):
        self.observer_list.append(obs)

    def remove_obs(self, obs):
        self.observer_list.remove(obs)

    def remove_all_obs(self):
        for obs in self.observer_list:
            obs.update(None)
        self.observer_list[:] = []

    def notify_observers(self, location):
        for obs in self.observer_list:
            obs.update(location)

    def update(self, location):
        if location:
            self.destination = location
        else:
            self.destination = self.location
            self.subject = None

    def set_subject(self, new_subject):
        if self.subject:
            self.subject.observer_list.remove(self)
        self.subject = new_subject
        if self.subject:
            new_subject.register_obs(self)
            self.destination = new_subject.location

    def act(self, morg_mortality):
        self.direction = self.destination_direction()
        self.move(self.direction)

        # debug purposes
        self.print_info()

        if self.subject:
            if self.subject.alive:
                if self.feed_behavior:
                    self.feed_behavior.consume(morg_mortality, self, self.subject)

        if self.reproduction_behavior:
            self.reproduction_behavior.reproduce(morg_mortality, self)

        self.notify_observers(self.location)
        self.age += 1

    # For debugging purposes
    def print_info(self):
        print('Morg ID: ' + str(hex(self.id)) + ', Type: ' + self.type + ', Alive: ' + str(self.alive) + '\n' +
              'Direction: ' + str(self.direction) +
              ', Destination: ' + str(self.destination) +
              ', Destination direction: ' + str(self.destination_direction()) +
              ', Location: ' + str(self.location) + '\nFeed List: ' + str(self.feed_list) +
              ', Feeding Behavior: ' + str(self.feed_behavior) + ', Subject: ' + str(self.subject) + '\n' +
              'Reproduction Behavior: ' + str(self.reproduction_behavior) + '\n')


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, location):
        x = abs(self.x - location.x)
        y = abs(self.y - location.y)
        return sqrt(x*x + y*y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'