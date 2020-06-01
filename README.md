# challenge
challenge for TruSTAR

### Install
```bash
$ virtualenv -p python3 venv 
$ pip3 install -r requirements.txt
```

### How to run the tests
```bash
$ source venv/bin/activate 
$ pip3 install -r test-requirements.txt
$ pytest tests/
```

### Usage
Using the example of the challenge:
```bash
$ python3 cli.py --repo 'https://github.com/mitre/cti' --folder 'enterprise-attack/attack-pattern' --props "id" "objects[0].name" "objects[0].kill_chain_phases"
```

### alternative usage
we could build a python package instead, by doing
```bash
$ rm -rf dist build */*.egg-info *.egg-info # optional unnesessary the first time
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
