# Garmin

Fetch and log Garmin activities.

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

Open the virtual machine

```bash
source ./venv/bin/activate
```

and run

```python
python ./src/garmin.py --username email@domain.com --password password
```

## Packages

This project uses the [garminconnect](https://pypi.org/project/garminconnect) package that wraps the Garmin Connect API.

Python dependencies should be installed in a virtual environment.
The virtual machine can be set up using [venv](https://docs.python.org/3/library/venv.html).
Steps to set this up on MacOSX can be found [here](https://www.studytonight.com/post/python-virtual-environment-setup-on-mac-osx-easiest-way).

```bash
python3 -m venv path/to/venv
source path/to/venv/bin/activate
pip3 install garminconnect
```