from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()
g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")
query = prepareQuery('''
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
    SELECT ?ArtTool ?isSimilarTo
    WHERE {
        moc:sample moc:isTestedFor ?ArtTool .
        moc:sample moc:isSimilarTo ?isSimilarTo .
            }
       ''',
    initNs={"moc": moc})

results = g.query(query)

for row in results:
    print(row.ArtTool)
    print(row.isSimilarTo)