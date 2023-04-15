from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()
g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")
query = prepareQuery('''
        PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
        SELECT ?ArtDetail
        WHERE {
            {
            moc:Irises moc:hasDetail ?ArtDetail .
            }
        UNION
            {
            moc:WaterLilies moc:hasDetail ?ArtDetail .
            }
                }
       ''',
    initNs={"moc": moc})

results = g.query(query)

for row in results:
    print(row.ArtDetail)