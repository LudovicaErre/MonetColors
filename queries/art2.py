from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()

g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")

query2 = prepareQuery('''
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xml: <http://www.w3.org/XML/1998/namespace>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?advances
    WHERE {
        ?event rdf:type moc:Event ;
               rdfs:label "Changes in the art field"@en ;
               moc:hasEvent ?advances .
        FILTER (?advances IN (moc:new_pigments, moc:metal_paint_tube, moc:new_equipment))
    }
    ''',
    initNs={"moc": moc})

results2 = g.query(query2)

for row in results2:
    print(row['advances'])
