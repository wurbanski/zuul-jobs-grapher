import os
import yaml
from Job import Job

class ConfigParser:
    def __init__(self, *args):
        self.__config = []
        for arg in args:
            if os.path.exists(arg):
                with open(arg) as cfile:
                    config_contents = yaml.load(cfile)
                    for entry in config_contents:
                        entry['source'] = arg
                        self.__config.append(entry)

            else:
                print "File %s does not exist, skipping." % arg

    def getJobs(self):
        for entry in self.__config:
            if 'job' in entry.keys():
                yield Job(entry['job'], source=entry['source'])

