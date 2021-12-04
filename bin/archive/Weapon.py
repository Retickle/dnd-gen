class Weapon:
    adjective = ''
    type = ''
    stat = ''

    # optional weapon bonus
    bonus = ''

    # preposition used to indicate weapon stat
    preposition = 'of'

    def __init__(self, adjective, type, stat='', bonus=''):
        """Constructor"""
        self.adjective = adjective
        self.type = type
        self.stat = stat
        self.bonus = bonus

    def __str__(self):
        """Weapon to string. Weapon in text format"""
        first = f'{self.adjective} {self.type}'
        if(self.stat == ''):
            return f'{first}'

        second = f'{self.stat}'
        if self.bonus != '':
            second = f'{self.bonus} {self.stat}'

        return f'{first} {self.preposition} {second}'

    def __eq__(self, other):
        """Are the values of this weapon equal to another"""
        if isinstance(other, Weapon):
            return (
                self.adjective == other.adjective and
                self.type == other.type and
                self.stat == other.stat and
                self.bonus == other.bonus
            )
        return False

    def set_stat(self, stat):
        """Set stat of this weapon."""
        if self.stat != '':
            return
        self.stat = stat

    def set_bonus(self, bonus):
        """Set bonus of this weapon. Requires the weapon to have a stat."""
        if self.bonus != '' or self.stat == '':
            return
        self.bonus = bonus
