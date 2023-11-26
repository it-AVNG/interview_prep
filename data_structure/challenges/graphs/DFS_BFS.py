import queue
import matplotlib.pyplot as plt
import networkx as nx
import time

def order_bfs(graph, start_node):
    '''A Breadth first search method for graphs'''

    # initialize internal parameters
    visited = set() # keep track of visited node
    q = queue.Queue() # a queue to know which node to visit next
    q.put(start_node) # put the start node to the queue
    order = [] # order of search list to return

    # run untill the queue is depleted
    while not q.empty():
        # take the node from the queue, called vertex
        vertex = q.get()
        #if the vertex is not visited yet
        if vertex not in visited:
            # append the vertex in search order list and visited set
            order.append(vertex)
            visited.add(vertex)

            # look around the vertex neighbors
            for node in graph[vertex]:
                # Check if the neighbor is visited
                if node not in visited:
                    # if not, put it to the queue to visit later
                    q.put(node)

    return order

def order_dfs(graph, start_node, visited=None):
    '''Depth First Search method for graphs'''

    # initialize the visited set when first run
    if visited is None:
        visited = set()

    # initialize the search order list
    order = []

    # if the node is not yet visited
    if start_node not in visited:
        # add them to the order search list and visited set
        order.append(start_node)
        visited.add(start_node)
        # look for the next vertex in the node adjacent
        for node in graph[start_node]:
            # if have not visited yet
            if node not in visited:
                # travel to the node and add to the oredered list by extend()
                # parse also the current graph and the visited to the call
                order.extend(order_dfs(graph, node, visited))

    return order

def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos,
                with_labels=True,
                node_color=['r' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(0.5)

    plt.show()
    time.sleep(1.5)

def generate_connected_random_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G

G = generate_connected_random_graph(n=20,m=30)
pos = nx.spring_layout(G)

visualize_search(order_dfs(G, start_node=0), title='BFS visualization', G=G, pos=pos)