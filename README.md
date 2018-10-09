# zuul-jobs-grapher
Simple application to graph jobs dependency in Zuul CI.

## Requirements

1. graphviz binaries available in `$PATH`
2. python libraries from `requirements.txt`

## Usage

`python grapher.py -c path/to/zuul.yaml -c path/to/config_directory -o
filename` renders graph based on file `path/to/zuul.yaml` and directory
`path/to/config_directory` to `_output/filename.png` and graphviz dot-file file to `_output/filename`.

## TODO

- [x] Feed a config directory to the application
- [x] Select output format (if it is SVG)
- [x] Make graph prettier
- [ ] You tell me

## Kudos

[Lukasz Lukasiewicz](https://github.com/Diabelko) for initial idea and work.
