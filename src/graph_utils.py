import networkx as nx

def draw_graph(graph, ax, canvas):
    ax.clear()
    pos = nx.spring_layout(graph, k=0.5, iterations=50)

    # Separate edges into request (P → R) and allocation (R → P)
    request_edges = [(u, v) for u, v in graph.edges if graph.nodes[u].get('type') == 'process']
    allocation_edges = [(u, v) for u, v in graph.edges if graph.nodes[u].get('type') == 'resource']

    # Draw nodes
    process_nodes = [n for n, d in graph.nodes(data=True) if d.get('type') == 'process']
    resource_nodes = [n for n, d in graph.nodes(data=True) if d.get('type') == 'resource']
    
    nx.draw_networkx_nodes(graph, pos, nodelist=process_nodes, node_color='lightblue', node_size=1000)
    nx.draw_networkx_nodes(graph, pos, nodelist=resource_nodes, node_color='palegreen', node_size=1000, node_shape='s')

    # Draw edges with different styles
    nx.draw_networkx_edges(graph, pos, edgelist=request_edges, edge_color='red', style='dashed', width=2)
    nx.draw_networkx_edges(graph, pos, edgelist=allocation_edges, edge_color='blue', style='solid', width=2)

    # Draw labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_weight="bold")

    ax.set_title("Resource Allocation Graph")
    ax.axis('off')
    canvas.draw()