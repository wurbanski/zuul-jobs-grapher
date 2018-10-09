import os
import yaml
from glob import glob
from Job import Job

class ConfigParser:
    def __init__(self, *args):
        def parse_file(config_file):
            with open(config_file) as cfile:
                try:
                    config_contents = yaml.safe_load(cfile)
                except yaml.constructor.ConstructorError as e:
                    print "Error! %s\n skipping file..." % (e,)
                    config_contents = []
                for entry in config_contents:
                    if 'job' in entry.keys():
                        entry['source'] = config_file
                        yield entry

        self.__config = []
        for arg in args:
            if os.path.exists(arg):
                if os.path.isdir(arg):
                    for yaml_file in glob('%s/*.yaml' % arg):
                        for entry in parse_file(yaml_file):
                            self.__config.append(entry)
                else:
                    for entry in parse_file(arg):
                        self.__config.append(entry)
            else:
                print "File or directory %s does not exist, skipping." % arg

    def getJobs(self):
        for entry in self.__config:
            yield Job(entry['job'], source=entry['source'])

