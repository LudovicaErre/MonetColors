from rdflib import Graph, Namespace
from rdflib.plugins.sparql.processor import prepareQuery

g = Graph()
g.parse("monetcolors.ttl", format="ttl")

moc = Namespace("http://www.semanticweb.org/ontologies/2023/1/moc#")
query = prepareQuery('''
    PREFIX moc: <http://www.semanticweb.org/ontologies/2023/1/moc#>
    SELECT ?title ?typegoal
    WHERE {
        ?title rdf:type moc:TitleObject ;
        rdfs:label ?label ;
        moc:hasTypeGoal ?typegoal .
  
    FILTER(regex(str(?label), "Color, Chemistry, and Creativity in Monet's Water Lilies|Monet's Palette in the Twentieth Century: Water-lilies and Irises"))
        } 
       ''',
    initNs={"moc": moc})

results = g.query(query)

for row in results:
    print(row.title)
    print(row.typegoal)