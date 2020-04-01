import pandas as pd
import base64


def recursive_flatten(d):
    flattened = {}
    for key, val in d.items():
        if type(val) == dict:
            for k, v in recursive_flatten(val).items():
                flattened[f'{key}.{k}'] = v
        else:
            flattened[key] = val
    return flattened


def dict_list_to_csv_b64(d):
    csv_string = pd.DataFrame(d).to_csv()
    return base64.b64encode(bytes(csv_string, 'utf-8'))


if __name__ == '__main__':
    # Test flattening and CSV
    d_list = [
        {'annotationId': 1032342, 'results': {'he': {'H': {'mean': -0.5635769737555945, 'std': 0.02122798821969583},
                                                     'E': {'mean': 0.1829766529298919, 'std': 0.025926053403379126}},
                                              'hsv': {'H': {'mean': 0.2735736547061177, 'std': 0.35832885537693954},
                                                      'S': {'mean': 0.07352886078390428, 'std': 0.11487906391723712},
                                                      'V': {'mean': 0.9059728814010616, 'std': 0.09972652323568698}}}},

        {'annotationId': 1032341, 'results': {'he': {'H': {'mean': -0.5635769737555945, 'std': 0.02122798821969583},
                                                     'E': {'mean': 0.18297665292919, 'std': 0.025926053403379126}},
                                              'hsv': {'H': {'mean': 0.2735736547061177, 'std': 0.3585537693954},
                                                      'S': {'mean': 0.07352886078390428, 'std': 0.11487906391723712},
                                                      'V': {'mean': 0.9059728814010616, 'std': 0.09972652323568698}}}},
    ]
    d_list = [recursive_flatten(d) for d in d_list]
    print(pd.DataFrame(d_list))

    encoded = dict_list_to_csv_b64(d_list)
    print(encoded)
    print(base64.b64decode(encoded))
