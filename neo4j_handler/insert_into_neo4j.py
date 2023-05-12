import json
import time
from py2neo import Graph
import os
from dotenv import load_dotenv

load_dotenv()
password = os.environ.get("NEO4J_PASSWORD")
# Connect to the Neo4j server
graph = Graph("bolt://localhost:7687", auth=("neo4j", password))

def insert_into_neo4j_by_element_id(element_id, data):
    tag = data["tag"]
    elementId = data["elementId"] if "elementId" in data else hash(time.time())
    attributes = data["attributes"] if "attributes" in data else {}
    text = data["text"] if "text" in data else ""

    query = f"""
    MATCH (parent:Node {{elementId: {element_id}}})
    CREATE (child:Node {{tag: $tag, elementId: $elementId, text: $text}})
    SET child += $attributes
    CREATE (parent)-[:HAS_CHILD]->(child)
    """
    graph.run(query, tag=tag, elementId=elementId, text=text, attributes=attributes).evaluate()

if __name__ == "__main__":
    element_id = 5336551053627291776
    json_data = {
        "text": "Hello World",
        "tag": "div",
        "elementId": hash(time.time()),
    }
    insert_into_neo4j_by_element_id(element_id, json_data)
