class Job:
    def __init__(self, attributes):
        self.__dict__.update(**attributes)
        if not 'parent' in attributes.keys():
            self.__dict__.update({'parent': 'base'})

    def __repr__(self):
        return "Job: %s, parent: %s" % (self.name, self.parent)

    def asEdge(self):
        if self.__dict__.get('parent', None):
            return (self.name, self.parent), {}
        return None

    def asNode(self):
        return (self.name), {'label': self.name, 
                             'fillcolor': '#fffde0' if self.isBase() else '#ffffff',
                             'style': 'filled'}

    def isBase(self):
        return self.name.endswith('-base')
