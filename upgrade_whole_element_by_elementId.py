import json


def upgrade_whole_element_by_elementId(json_obj, search_element_id, update_element):
    update_element["elementId"] = search_element_id
    if "elementId" in json_obj and json_obj["elementId"] == search_element_id:
        json_obj.update(update_element)
        return True

    if "children" in json_obj:
        for child in json_obj["children"]:
            if upgrade_whole_element_by_elementId(child, search_element_id, update_element):
                return True

    return False

if __name__ == '__main__':
    with open('json.json', 'r') as json_file:
        json_obj = json.load(json_file)
        update_element = {
            "tag": "span",
            "text": "Updated **********"
        }
        upgrade_whole_element_by_elementId(json_obj, -8242187003519717687, update_element)
        # write to removed.json
        with open('updated.json', 'w') as removed_file:
            json.dump(json_obj, removed_file, indent=4, ensure_ascii=False)