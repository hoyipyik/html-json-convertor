import json


def add_child_by_elementId(json_obj, parent_element_id, new_child):
    if 'children' not in json_obj:
        return False

    for child in json_obj['children']:
        if 'elementId' in child and child['elementId'] == parent_element_id:
            if 'children' not in child:
                child['children'] = []
            child['children'].append(new_child)
            return True

        if add_child_by_elementId(child, parent_element_id, new_child):
            return True

    return False

if __name__ == '__main__':
    with open('json.json', 'r') as json_file:
        json_obj = json.load(json_file)
        new_element = {
            "tag": "span",
           "text": "New child span element"
        }
        add_child_by_elementId(json_obj, -1400270133389665487, new_element)
        # write to removed.json
        with open('added.json', 'w') as removed_file:
            json.dump(json_obj, removed_file, indent=4, ensure_ascii=False)
