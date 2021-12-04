class Item:
    def __init__(self, components=[]):
        self.components = list(components)

    def __str__(self):
        """Returns the data of the item in string format."""
        raise NotImplementedError("Please implement item method.")

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.components == other.components

    def get_component(self, key):
        """Gets the value of component {key}."""
        for c in self.components:
            if c['key'] == key:
                return c['value']
        return ''

    def set_component(self, key, value):
        """Sets the values of component {key}."""
        for c in self.components:
            if c['key'] == key:
                c['value'] == value
        print('Bruh that component aint even exist. ' + str(key))

    def add_component(self, key, value):
        """Adds a component to this item."""
        self.components.append({"key": key, "value": value})

    def remove_component(self, key):
        """Removes a component from this item."""
        for c in self.componenets:
            if c['key'] == key:
                self.components.remove(c)
