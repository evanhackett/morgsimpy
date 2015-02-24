import morg as m


class MorgFactory:
    def create_morg(self, morg_type, x_cord, y_cord, color, radius, feed_behavior, feed_list, reproduction_behavior):
        morg = m.Morg()
        morg.type = morg_type
        morg.location.x = x_cord
        morg.location.y = y_cord
        morg.color = color
        morg.feed_behavior = feed_behavior
        morg.reproduction_behavior = reproduction_behavior
        morg.feed_list = feed_list
        morg.destination = morg.location
        morg.radius = radius

        return morg