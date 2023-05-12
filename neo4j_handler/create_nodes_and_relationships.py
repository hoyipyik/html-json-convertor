import json
from py2neo import Graph

# Connect to the Neo4j server
graph = Graph("bolt://localhost:7687", auth=("neo4j", "3190021410"))

# Recursively create nodes and relationships from JSON
def create_nodes_and_relationships(parent, data):
    tag = data["tag"]
    elementId = data["elementId"]
    attributes = data["attributes"]
    children = data["children"]
    text = data["text"]
    
    query = f"""
    MERGE (n:Node {{tag: $tag, elementId: $elementId, text: $text}})
    SET n += $attributes
    RETURN n
    """
    node = graph.run(query, tag=tag, elementId=elementId, text=text, attributes=attributes).evaluate()
    
    if parent:
        query = f"""
        MATCH (parent:Node {{elementId: $parent_elementId}}),
              (child:Node {{elementId: $child_elementId}})
        MERGE (parent)-[:HAS_CHILD]->(child)
        """
        graph.run(query, parent_elementId=parent["elementId"], child_elementId=elementId)
    
    for child in children:
        create_nodes_and_relationships(node, child)


if __name__ == "__main__":
    json_data = {}
    with open('../json.json') as json_file:
        json_data = json.load(json_file)
    create_nodes_and_relationships(None, json_data)
