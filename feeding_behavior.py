class Absorb:
    def consume(self, morg_mortality, morg, prey):
        # for debugging
        #print_info(morg, prey)
        #morg.print_info()
        if morg.location.distance(prey.location) <= morg.radius + prey.radius:
            morg_mortality.kill(prey.id)
            morg.radius += 1

    def __str__(self):
        return 'Absorb'


class Envelop:
    def consume(self, morg_mortality, morg, prey):
        # for debugging
        #print_info(morg, prey)
        #morg.print_info()
        if morg.location.distance(prey.location) + prey.radius < morg.radius:
            morg_mortality.kill(prey.id)
            morg.radius += 1

    def __str__(self):
        return 'Envelop'


def print_info(morg, prey):
    print("Distance: " + str(morg.location.distance(prey.location)))
    print("Radius: " + str(morg.radius))
    print("Prey radius: " + str(prey.radius) + '\n')