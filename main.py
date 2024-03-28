import json

"""  return False if Resource contains a single asterisk, True in any other case. """
def verify_json(input_data):
    if isinstance(input_data, dict):
        data = input_data
    else:
        data = json.loads(input_data)

    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'Resource':
                if value == '*':
                    return False
                if isinstance(value, list) and '*' in value:
                    return False
            else:
                if isinstance(value, (list, dict)):
                    if not verify_json(value):
                        return False


