# zuul-jobs-grapher
Simple application to graph jobs dependency in Zuul CI.

## Requirements

1. graphviz binaries available in `$PATH`
2. python libraries from `requirements.txt`

## Usage

`python run.py -f path/to/zuul.yaml -o filename` renders graph based on file `path/to/zuul.yaml` to `_output/filename.png` and `.gv` file to `_output/filename`.

## TODO

- [ ] Feed a config directory to the application
- [ ] Select output format
- [ ] Make graph prettier
- [ ] You tell me

## Kudos

[Lukasz Lukasiewicz](https://github.com/Diabelko) for initial idea and work.
