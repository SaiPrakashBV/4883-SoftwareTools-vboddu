import json
import graphviz 
from  rich import print 

dot = graphviz.Digraph(comment='Test Family Tree')
with open('family_tree_data.json') as f:
  data = json.load(f)
  
  l=len(data)

  subgraphs= [] 
  for i in range(l):
    if data[i]['gender']=='Female':
      dot.node(str(data[i]['pid']),data[i]['name']+" "+data[i]['last_name'], shape='octagon')
    else:
      dot.node(str(data[i]['pid']),data[i]['name']+" "+data[i]['last_name'])
    
    if(data[i]['parent_id1']!=""):
      dot.edge(str(data[i]['parent_id1']),str(data[i]['pid']))


    if(data[i]['spouse_id']!=""):
      subgraph=graphviz.Digraph(name='spouses')
      subgraph.node(str(data[i]['pid']),data[i]['name']+" "+data[i]['last_name'])
      subgraph.node(str(data[i]['spouse_id']),data[i]['name']+" "+data[i]['last_name'] )
      dot.edge(str(data[i]['pid']),str(data[i]['spouse_id']))
      subgraph.attr(rank="same")
      subgraphs.append(subgraph)


with open('family_tree.dot', mode='w') as f:
    f.write(dot.source)