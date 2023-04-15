from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()

g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")

query3 = prepareQuery('''
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xml: <http://www.w3.org/XML/1998/namespace>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?french_prop ?cobalt_prop
WHERE {
  ?french a moc:SpecificColor ;
          rdfs:label "French ultramarine"@en ;
          moc:hasProperty ?french_prop .
  ?cobalt a moc:SpecificColor ;
          rdfs:label "Cobalt blue"@en ;
          moc:hasProperty ?cobalt_prop .
}
    ''',
    initNs={"moc": moc})

results3 = g.query(query3)

for row in results3:
    print("French ultramarine is typically", row['french_prop'], "; Cobalt blue appears", row['cobalt_prop'])
