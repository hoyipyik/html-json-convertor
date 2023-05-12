from py2neo import Graph
from dotenv import load_dotenv
import os

load_dotenv()
password = os.environ.get("NEO4J_PASSWORD")
# Connect to the Neo4j server
graph = Graph("bolt://localhost:7687", auth=("neo4j", password))


def delete_by_element_id(element_id):
    query = f"""
    MATCH (parent:Node {{elementId: {element_id}}})-[r*]->(child)
    DETACH DELETE child, parent
    """
    graph.run(query)

def delete_by_property(property_name, property_value):
    query = f"""
    MATCH (parent:Node {{ {property_name}: {property_value} }})-[r*]->(child)
    DETACH DELETE child, parent
    """
    graph.run(query)

if __name__ == "__main__":
    element_id = -1274039742488620801
    # delete_by_element_id(element_id)
    delete_by_property("elementId", element_id)