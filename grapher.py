import argparse
from ConfigParser import ConfigParser
from GraphDrawer import GraphDrawer

def argumentParser():
    parser = argparse.ArgumentParser(description='Display job dependency graph')
    parser.add_argument('-c', '--config', action='append', required=True,
                        dest='config',
                        help='config file or directory (can be called multiple times for' +
                        ' multiple entries)')
    parser.add_argument('-o', '--out', action='store', required=True,
                        dest='outfile',
                        help='outfile name (.svg format implicit)')
    return parser.parse_args()

def main():
    args = argumentParser()
    config = ConfigParser(*args.config)
    gd = GraphDrawer(format='svg')
    gd.add_nodes([job.asNode() for job in config.getJobs()])
    gd.add_edges([job.asEdge() for job in config.getJobs() if job.asEdge()])

    gd.render(args.outfile)

if __name__ == "__main__":
    main()
