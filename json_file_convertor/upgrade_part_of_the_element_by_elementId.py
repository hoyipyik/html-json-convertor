import json


def upgrade_part_of_the_element_by_elementId(json_obj, search_element_id, property_name, new_value):
    if "elementId" in json_obj and json_obj["elementId"] == search_element_id:
        json_obj[property_name] = new_value
        return True

    if "children" in json_obj:
        for child in json_obj["children"]:
            if upgrade_part_of_the_element_by_elementId(child, search_element_id, property_name, new_value):
                return True

    return False


if __name__ == '__main__':
    with open('../json.json', 'r') as json_file:
        json_obj = json.load(json_file)
        upgrade_part_of_the_element_by_elementId(json_obj, -8242187003519717687, "tag", "iframe")
        upgrade_part_of_the_element_by_elementId(json_obj, -8242187003519717687, "text", "Google ))))))")
        # write to removed.json
        with open('updated_part.json', 'w') as removed_file:
            json.dump(json_obj, removed_file, indent=4, ensure_ascii=False)