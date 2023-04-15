from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()

g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")

query = prepareQuery("""
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xml: <http://www.w3.org/XML/1998/namespace>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?color1 ?color2
    WHERE {
      ?waterlilies rdf:type moc:ArtWorkTitle ;
                   moc:hasArtist moc:Monet ;
                   moc:hasDetail ?redflowers .
      ?redflowers rdf:type moc:ArtDetail ;
                  moc:hasColor ?color1, ?color2 .
      FILTER (?color1 = moc:Vermillion && ?color2 = moc:Red_lake)
    }
""", initNs={"moc": moc})

results = g.query(query)

for row in results:
    print(row["color1"])
    print(row["color2"])









