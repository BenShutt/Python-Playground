# Garmin (WIP)

Fetch and log Garmin activities.

## Usage

### Activate Virtual Environment

From the project directory, create the `venv` virtual environment directory:

```bash
python3 -m venv ./venv
```

Activate the virtual environment:

```bash
source "./venv/bin/activate"
```

Install dependencies:

```bash
pip3 install -r ./requirements.txt
```

### Run

In an active virtual environment, run the python script passing the command-line arguments:

```bash
python ./src/main.py --tokens ./garmin_tokens
```

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
