# .wav Sorter
This script sorts a file tree of only .wav files and sorts them by length into new directories

## Requirements

- scipy.io
```commandline
pip install scipy
```


## Usage
```commandline
python main.py [path to file tree containing .wav files]
```

## Possible improvements

- Add commandline arguments:
  - Verbose mode
  - Let user set sorting durations
  - Clean up mode to remove old file tree
- Handle other types of audio files