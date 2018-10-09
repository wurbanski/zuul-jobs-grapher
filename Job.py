from collections import defaultdict
from pprint import pformat

class Job:
    base_color = '#ccbe00'
    base_fill = '#fffde0'
    color = '#22d88c'
    fill = '#d0fff2'

    def __init__(self, attributes, source):
        self.__dict__.update(**attributes)
        self.__dict__['source'] = source
        if not 'parent' in attributes.keys():
            self.__dict__.update({'parent': 'base'})

    def __repr__(self):
        return "Job: %s, parent: %s" % (self.name, self.parent)

    def __getFillcolor(self):
        return self.base_fill if self.__isBase() else self.fill

    def __getColor(self):
        return self.base_color if self.__isBase() else self.color

    def __isBase(self):
        return 'base' in self.name

    def __renderTooltip(self):
        d = defaultdict(lambda: '-')
        d.update(self.__dict__)

        return """defined in: %(source)s

pre-run: %(pre-run)s
run: %(run)s
post-run: %(post-run)s

vars: %(vars)s
""" % d

    def asEdge(self):
        if self.__dict__.get('parent', None):
            return (self.name, self.parent), {'color': self.__getColor()}
        return None

    def asNode(self):
        return (self.name), {'label': self.name, 
                             'fillcolor': self.__getFillcolor(),
                             'color': self.__getColor(),
                             'tooltip': self.__renderTooltip(),
                             'style': 'filled'}

