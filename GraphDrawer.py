import graphviz as gv
from os.path import join as pathjoin


class GraphDrawer:
    def __init__(self, output_dir='_output', format='svg'):

        self.graph = gv.Digraph(format=format, graph_attr={'overlap':'scale',
                                                           'sep': '.1'})
        self.output_dir = output_dir

    def add_nodes(self, nodes):
        for n in nodes:
            if isinstance(n, tuple):
                self.graph.node(n[0], **n[1])
            else:
                self.graph.node(n)

    def add_edges(self, edges):
        for e in edges:
            if isinstance(e[0], tuple):
                self.graph.edge(*e[0], **e[1])
            else:
                self.graph.edge(*e)

    def render(self, filename, **kwargs):
        return self.graph.render(pathjoin(self.output_dir, filename), **kwargs)

