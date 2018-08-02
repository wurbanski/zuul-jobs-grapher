import os
import yaml
from Job import Job

class ConfigParser:
    def __init__(self, *args):
        self.__config = []
        for arg in args:
            if os.path.exists(arg):
                with open(arg) as cfile:
                    self.__config += yaml.load(cfile)
            else:
                print "File %s does not exist, skipping." % arg

    def getJobs(self):
        for entry in self.__config:
            if 'job' in entry.keys():
                yield Job(entry['job'])

