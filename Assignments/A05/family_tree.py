import json
import graphviz
from rich import print

dot = graphviz.Digraph(comment='Family Tree')
with open('family_tree_data.json') as f:
    data = json.load(f)
dot.attr('graph', {'ranksep': '1.5', 'nodesep': '0.5', 'minlen': '2'})

generations = set(person['generation'] for person in data)

# Create subgraphs for each generation
subgraphs = {}
for generation in generations:
    subgraph = graphviz.Digraph(name=f'gen_{generation}')
    subgraph.attr(rank='same')
    subgraphs[generation] = subgraph

# Add nodes to subgraphs
for person in data:
    node_id = str(person['pid'])
    gender = person['gender']
    generation = person['generation']
    first_name = person['name']
    last_name = person['last_name']
    birth_year = str(person['byear'])
    death_year = str(person['dyear'])
    clan_name = person['clan']
    node_label = f'<<TABLE BORDER="0" CELLBORDER="0.5" CELLSPACING="0">'
    node_label += f'<TR><TD>Name</TD><TD>{first_name} {last_name}</TD></TR>'
    node_label += f'<TR><TD>Years</TD><TD>{birth_year}-{death_year}</TD></TR>'
    node_label += f'<TR><TD>Clan</TD><TD COLSPAN="2">{clan_name}</TD></TR>'
    node_label += f'<TR><TD>ID</TD><TD COLSPAN="2">{node_id}</TD></TR>'
    node_label += '</TABLE>>'


    # Set shape based on gender
    if gender == 'Male':
        shape = "octagon"
        node_fill_color = 'lightblue'
    else:
        node_fill_color = 'pink'
        shape = "ellipse"

    # Add node to the corresponding subgraph
    subgraphs[generation].node(node_id, label=node_label, shape=shape,style='filled',fillcolor=node_fill_color)

    # Add spouse relationship
    if 'spouse_id' in person:
        spouse_id = str(person['spouse_id'])
        dot.edge(node_id, spouse_id, style='dashed')

# Add parent-child relationship
for person in data:
    node_id = str(person['pid'])
    parent1_id = str(person.get('parent_id1'))
    parent2_id = str(person.get('parent_id2'))

    #print(f"Node: {node_id}, Parent1: {parent1_id}, Parent2: {parent2_id}")

    if parent1_id and parent1_id != 'None':
        dot.edge(parent1_id, node_id, style='solid')
    if parent2_id and parent2_id != 'None':
        dot.edge(parent2_id, node_id, style='solid')

# Combine subgraphs into the main graph
for subgraph in subgraphs.values():
    dot.subgraph(subgraph)

with open('family_tree.dot', mode='w') as f:
    f.write(dot.source)
