from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()
g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")
query = prepareQuery('''
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
    SELECT ?palette ?SpecificColor
    WHERE {
        {
        moc:palette1906 moc:hasColor ?specificColor .
        ?specificColor rdfs:label ?SpecificColor .
        moc:palette1906 rdfs:label ?palette .
        }
    UNION
        {
        moc:palette1916 moc:hasColor ?specificColor .
        ?specificColor rdfs:label ?SpecificColor .
        moc:palette1916 rdfs:label ?palette .
        }
            } 
       ''',
    initNs={"moc": moc})

results = g.query(query)

for row in results:
    print(row.palette)
    print(row.SpecificColor)