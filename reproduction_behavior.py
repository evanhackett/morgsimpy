class Divide:
    def reproduce(self, morg_mortality, morg):
        if morg.radius >= 7:
            morg_mortality.birth(morg.type, morg.location, morg.color, 4, morg.feed_behavior,
                                 morg.feed_list, morg.reproduction_behavior)
            morg.radius = 4

    def __str__(self):
        return 'Divide'

# currently this code is using hardcoded values for the radii.