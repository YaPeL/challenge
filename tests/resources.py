DEFAULT_JSON = '''
{
    "type": "bundle",
    "id": "bundle--bf3c8e50-62a0-440f-9936-279bf4ad34bb",
    "objects": [
        {
            "kill_chain_phases": [
                {
                    "kill_chain_name": "mitre-attack",
                    "phase_name": "defense-evasion"
                }
            ],
            "name": "Indicator Removal from Tools",
            "description": "If a malicious tool is detected and quarantined or otherwise curtailed",
            "id": "attack-pattern--00d0b012-8a03-410e-95de-5826bf542de6"
        }
    ]
}
'''
EMPTY_JSON = '{}'

DEFAULT_PROPS = ["id", "objects[0].name", "objects[0].kill_chain_phases[0].kill_chain_name"]
MISSING_VALUE_PROPS = ["id", "objects[0].name", "objects[10].name", "objects[0].kill_chain_phases.kill_chain_name"]
STRING_INSTEAD_OF_ARRAY_PROP = ["id", "objects[0].name[0]"]
DEFAULT_RESULT = {'id': 'bundle--bf3c8e50-62a0-440f-9936-279bf4ad34bb', 'objects[0].name': 'Indicator Removal from Tools', 'objects[0].kill_chain_phases[0].kill_chain_name': 'mitre-attack'}
MISSING_VALUE_RESULT = {'id': 'bundle--bf3c8e50-62a0-440f-9936-279bf4ad34bb', 'objects[0].name': 'Indicator Removal from Tools'}
MISSING_STRING_RESULT = {"id": "bundle--bf3c8e50-62a0-440f-9936-279bf4ad34bb"}
EMPTY_RESULT = {}