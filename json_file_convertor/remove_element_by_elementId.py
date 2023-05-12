import json

def remove_element_by_elementId(json_obj, element_id):
    if 'children' not in json_obj:
        return None

    for index, child in enumerate(json_obj['children']):
        if 'elementId' in child and child['elementId'] == element_id:
            json_obj['children'].pop(index)
            return json_obj

        updated_json = remove_element_by_elementId(child, element_id)
        if updated_json is not None:
            return updated_json

    return {}

# if run in main
if __name__ == '__main__':
    # read json from json.json
    with open('../json.json', 'r') as json_file:
        json_obj = json.load(json_file)
        new = remove_element_by_elementId(json_obj, 9220435663088187748)
        # write to removed.json
        with open('removed.json', 'w') as removed_file:
            json.dump(new, removed_file, indent=4, ensure_ascii=False)


        
