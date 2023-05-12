from neo4j import GraphDatabase

# Define the connection URI and credentials
uri = "neo4j://localhost:7687"
user = "neo4j"
password = "3190021410"

# Initialize the driver object
driver = GraphDatabase.driver(uri, auth=(user, password))

# Function to create a sample graph
def create_sample_graph(tx):
    tx.run("MERGE (a:Person {name: 'Alice'})")
    tx.run("MERGE (b:Person {name: 'Bob'})")
    tx.run("MERGE (c:Person {name: 'Charlie'})")
    tx.run("MERGE (a)-[r:KNOWS]->(b)")
    tx.run("MERGE (b)-[r:KNOWS]->(c)")
    tx.run("MERGE (c)-[r:KNOWS]->(b)")

# Function to find all persons who know a specific person, e.g. 'Bob'
def find_persons_knowing(tx, person_name):
    result = tx.run("MATCH (a:Person)-[:KNOWS]->(b:Person {name: $name}) RETURN a.name", name=person_name)
    return [record["a.name"] for record in result]

# Create the graph
with driver.session() as session:
    session.execute_write(create_sample_graph)
# Query the graph
with driver.session() as session:
    persons_knowing_bob = session.execute_read(find_persons_knowing, 'Bob')
    print("People who know Bob:")
    for person in persons_knowing_bob:
        print(person)

# Close the driver object
driver.close()
