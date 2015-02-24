import feeding_behavior as FB
import reproduction_behavior as RB

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


def str_to_color(color_str):
    if color_str.upper() == 'RED':
        return RED
    elif color_str.upper() == 'BLUE':
        return BLUE
    elif color_str.upper() == 'GREEN':
        return GREEN
    else:
        return BLACK


class MorgReader:
    def __init__(self, morg_factory, file_name):
        self.factory = morg_factory
        self.file = file_name

    def read_morgs(self):
        f = open(self.file, 'r')
        morg_list = []

        for line in f:
            parameters = line.split(',')

            stripped_params = []
            # strip newline from the string
            for param in parameters:
                if '\n' in param:
                    param = param[:-1]
                stripped_params.append(param)

            feed_list = stripped_params[5].split(' ')
            feed_behavior = None

            if feed_list[0].lower() == "envelops":
                feed_behavior = FB.Envelop()
            elif feed_list[0].lower() == "absorbs":
                feed_behavior = FB.Absorb()
            elif feed_list[0].lower() == "none":
                feed_behavior = None

            reproduction_behavior = None
            if stripped_params[6].lower() == 'divides':
                reproduction_behavior = RB.Divide()
            elif stripped_params[6].lower() == 'none':
                reproduction_behavior = None


            morg = self.factory.create_morg(stripped_params[0], int(stripped_params[1]), int(stripped_params[2]),
                                            str_to_color(stripped_params[3]), int(stripped_params[4]),
                                            feed_behavior, feed_list[1:], reproduction_behavior)
            morg_list.append(morg)

        f.close()
        return morg_list