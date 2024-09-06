# Garmin

Fetch and log Garmin activities.

## Usage

### Activate Virtual Environment

From the project directory, create the `venv` virtual environment directory:

```bash
python3 -m venv ./venv
```

Activate the virtual environment:

```bash
source ./venv/bin/activate
```

In the active virtual environment, install dependencies:

```bash
pip3 install -r ./requirements.txt
```

### Run

In the active virtual environment, run the python script passing the command-line arguments:

```bash
python ./src/main.py --tokens ./garmin_tokens --days 3 --laps
```

#### Arguments

- `--tokens` [Option, Required] Directory to store OAuth tokens
- `--days` [Option, Required] Days before now to fetch activities
- `--laps` [Flag, Optional] Show splits for swimming activities. True when provided and false when omitted

### Deactivate Virtual Environment

Once done, deactivate the virtual machine:

```bash
deactivate
```

### Interpreter

Note, the interpreter path is:

```bash
./venv/bin/python
```

## Packages

This project uses the [garminconnect](https://pypi.org/project/garminconnect) package that wraps the Garmin Connect API.

Python dependencies should be installed in a virtual environment.
The virtual environment is set up using [venv](https://docs.python.org/3/library/venv.html).
Set up steps can be found [here](https://www.studytonight.com/post/python-virtual-environment-setup-on-mac-osx-easiest-way).
