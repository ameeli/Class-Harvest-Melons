############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []

        self.my_code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.new_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for item in melon_types:
        print '{} pairs with\n- {}'.format(item.name, '\n- '.join(item.pairings[0:]))

melon_types = make_melon_types()
print_pairing_info(melon_types)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons = {}

    for item in melon_types:
        melons[item.code] = item

    return melons

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



