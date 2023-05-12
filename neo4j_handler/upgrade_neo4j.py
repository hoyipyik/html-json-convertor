import time
from py2neo import Graph
import os
from dotenv import load_dotenv

load_dotenv()
password = os.environ.get("NEO4J_PASSWORD")
# Connect to the Neo4j server
graph = Graph("bolt://localhost:7687", auth=("neo4j", password))

def upgrade_property_by_element_id(element_id, key, value):
    query = f"""
    MATCH (node:Node {{elementId: {element_id}}})
    SET node.`{key}` = '{value}'
    """
    graph.run(query)

def upgrade_whole_by_element_id(element_id, data):
    tag = data["tag"]
    elementId = data["elementId"] if "elementId" in data else hash(time.time())
    attributes = data["attributes"] if "attributes" in data else {}
    text = data["text"] if "text" in data else ""

    query = f"""
    MATCH (node:Node {{elementId: {element_id}}})
    SET node.tag = $tag
    SET node.elementId = $elementId
    SET node.text = $text
    SET node += $attributes
    """
    graph.run(query, tag=tag, elementId=elementId, text=text, attributes=attributes).evaluate()

if __name__ == "__main__":
    element_id = 5336551053627291776
    json_data = {
        "text": "Hello Worldsssssss",
        "tag": "iframe",
        "elementId": element_id
    }
    upgrade_whole_by_element_id(element_id, json_data)
    # upgrade_property_by_element_id(element_id=element_id, key="text", value="Hello World *****")
    
