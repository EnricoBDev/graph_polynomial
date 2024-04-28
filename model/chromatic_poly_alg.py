import copy
import networkx as nx  # type: ignore
from sympy import symbols, sympify, Add
import random


class ChromaticPolyAlg:

    @staticmethod
    def calculate_poly(graph: nx.graph):
        x = symbols("x")
        if graph.number_of_edges() == 0:
            nodes = graph.number_of_nodes()
            expr = sympify(f"x^{str(nodes)}")
            return expr
        else:
            edge = list(graph.edges)[0]

            # by default the self_loops arg is True, this creates unnecessary
            # loops that break the algorithm

            contracted_graph = nx.contracted_edge(
                graph, edge, self_loops=False)

            # NOTE for future self
            # In python, when we use the assignment operator to create two copies
            # of a *mutable* object, they share the same id and the same memory space
            # so we need to do a copy of an object via the std library copy.deepcopy()

            removed_graph = copy.deepcopy(graph)
            removed_graph.remove_edge(*edge)
            return ChromaticPolyAlg.calculate_poly(removed_graph) - ChromaticPolyAlg.calculate_poly(contracted_graph)

    @staticmethod
    def get_random_edge(graph: nx.graph):

        edges_list = list(graph.edges)
        edge = random.choice(edges_list)

        return edge
