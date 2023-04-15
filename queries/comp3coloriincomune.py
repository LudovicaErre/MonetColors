from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()

g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc/")

query = prepareQuery('''
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xml: <http://www.w3.org/XML/1998/namespace>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?color
    WHERE {
      ?palette1 rdf:type moc:ArtTool .
      ?palette2 rdf:type moc:ArtTool .
      ?palette1 moc:hasColor ?color .
      ?palette2 moc:hasColor ?color .
      FILTER (?palette1 != ?palette2) 
    }
    GROUP BY ?color
    HAVING (COUNT(DISTINCT ?palette1) > 1)
''',
    initNs={"moc": moc})

results = g.query(query)

for result in results:
    print("Color in common: {}".format(result['color']))