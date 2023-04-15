from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()

g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")

query = prepareQuery('''
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>

    SELECT ?artworkTitle
    WHERE {
      ?artwork moc:heldIn moc:The_Art_Institute_of_Chicago ;
               moc:hasTitle ?artworkTitle .
    }
    ''',
    initNs={"moc": moc})

results = g.query(query)

for row in results:
    print(row.artworkTitle)