import argparse
from ConfigParser import ConfigParser
from GraphDrawer import GraphDrawer

def argumentParser():
    parser = argparse.ArgumentParser(description='Display job dependency graph')
    parser.add_argument('-f', '--file', action='append', required=True,
                        dest='jobfile',
                        help='filename (can be called multiple times for' +
                        ' multiple files)')
    parser.add_argument('-o', '--out', action='store', required=True,
                        dest='outfile',
                        help='outfile name (.png format)')
    return parser.parse_args()

def main():
    args = argumentParser()
    config = ConfigParser(*args.jobfile)
    gd = GraphDrawer(format='svg')
    gd.add_nodes([job.asNode() for job in config.getJobs()])
    gd.add_edges([job.asEdge() for job in config.getJobs() if job.asEdge()])

    gd.render(args.outfile)

if __name__ == "__main__":
    main()
