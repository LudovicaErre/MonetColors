from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()
g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")
query = prepareQuery('''
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
    SELECT ?SpecificColor
    WHERE {
        ?SpecificColor moc:mainElementOf moc:WaterLilies .
        ?SpecificColor rdf:type moc:SpecificColor .
        }
       ''',
    initNs={"moc": moc})

results = g.query(query)

for row in results:
    print(row.SpecificColor)