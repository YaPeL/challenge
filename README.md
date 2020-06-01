[![Build Status - GitHub](https://github.com/YaPeL/challenge/workflows/test/badge.svg)](https://github.com/YaPeL/challenge/actions?query=workflow%3Atest)
[![](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/release/python-383/)

# challenge
challenge for TruSTAR

### Install
```bash
$ virtualenv -p python3 venv 
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### How to run the tests
```bash
$ source venv/bin/activate 
$ pip3 install -r test-requirements.txt
$ pytest tests/
```

### Usage
Using the example of the challenge (give it a few seconds, the lib I've used for navigating through github has to clone the repo to a temp directory):
```bash
$ python3 cli.py --repo 'https://github.com/mitre/cti' --folder 'enterprise-attack/attack-pattern' --props "id" "objects[0].name" "objects[0].kill_chain_phases"
```

### alternative usage
we could build a python package instead, by doing
```bash
$ rm -rf dist build */*.egg-info *.egg-info # optional unnecessary the first time
$ python3 setup_package.py clean bdist_wheel
$ pip3 install dist/apptim_cli-0.0.1-py2.py3-none-any.whl
```
After that, it can be used in other projects as follows:
```python
from challenge.challenge import GitExtractor
ge = GitExtractor(repo='https://github.com/mitre/cti',
                  folder='enterprise-attack/attack-pattern',
                  props=["id", "objects[0].name", "objects[0].kill_chain_phases"])
for file, result in ge.files():
    print(f"For the file {file} extracted:")
    print(result)
```

### Question 5 "how would you change it to make it less error prone"
The basic issue is that the list of properties doesn't give much information about the chain of properties,
as stated on the challenge, it is just a string, so we need to interpret it (spliting it, finding hints to see if we need to access an array and so on)
alternatively we could use a markup language (json, xml, yaml) to define a schema:


this
```python
["id", "objects[0].name", "objects[0].kill_chain_phases"]
```
becomes this:
```javscript
{
  "properties": {
    "id": {
      "type": "string"
    },
    "objects": {
      "type": "array",
      "access": 0,
      "items": {
        "anyOf": [
          {
            "properties": {
              "kill_chain_phases": {
                "type": "array",
                "index": 0
              },
              "name": {
                "type": "string",
                "index": 0
              }
            }
          }
        ]
      }
    }
  }
}
```

Pros: all the info and the data types are set on the json

Cons: its obviously more verbose, and sadly, we don't know from where does the property list comes from, so maybe its something out of our control,
finally, there may be limitations to what the schema can represent
(for example, the index key is made up by me, I didn't find how to represent a "give me the first element of an array")
 meaning we may need to implement extra logic somewhere