# graph.py
import networkx as nx

class ResourceAllocationGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_process(self, process):
        # Add a process node to the graph if it doesn't already exist
        if process and not self.graph.has_node(process):
            self.graph.add_node(process, type='process')

    def remove_process(self, process):
        # Remove a process node from the graph if it exists
        if process in self.graph:
            self.graph.remove_node(process)

    def add_resource(self, resource):
        # Add a resource node to the graph if it doesn't already exist
        if resource and not self.graph.has_node(resource):
            self.graph.add_node(resource, type='resource')

    def remove_resource(self, resource):
        # Remove a resource node from the graph if it exists
        if resource in self.graph:
            self.graph.remove_node(resource)

    def request_resource(self, process, resource):
        # Add a red directed edge from a process to a resource to represent a request
        if process and resource and self.graph.has_node(process) and self.graph.has_node(resource):
            self.graph.add_edge(process, resource, color='red')

    def allocate_resource(self, resource, process):
        if resource and process and self.graph.has_node(resource) and self.graph.has_node(process):
            self.graph.add_edge(resource, process, color='blue')

    def clear_graph(self):
         # Remove all nodes and edges from the graph
        self.graph.clear()

    def check_deadlock(self):
        # Check the graph for cycles which indicate a potential deadlock
        try:
            cycle = list(nx.find_cycle(self.graph, orientation='original'))
            return cycle
        except nx.NetworkXNoCycle:
            return None

    def get_graph(self):
        # Return the internal graph object for external access or visualization
        return self.graph
