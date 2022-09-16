import math

def Dijkstra(graph,source,target):
    
    # These are all the nodes which have not been visited yet
    unvisited_nodes = graph

    # It will store the shortest distance from one node to another
    shortest_distance = {}

    # This will store the Shortest path between source and target node
    route = []

    # It will store the predecessors of the nodes
    predecessor = {}
    
    # Iterating through all the unvisited nodes
    for current_node, next_nodes in unvisited_nodes.items():

    # Initializing the shortest_distance of all nodes
        shortest_distance[current_node] = math.inf
        
    # The distance of a point to itself is 0.
    shortest_distance[source] = 0
    
    # Running the loop while all the nodes have not been visited
    while unvisited_nodes:

        # min_node will be the variable containing the node with the current
        # shortest path from source to one of the unvisited nodes (in unvisited_nodes).
        # setting the value of min_node as None
        min_Node = None
        
        # iterating through all the unvisited node
        for current_node, values in unvisited_nodes.items():
            
        # For the very first time that loop runs this will be called
            if min_Node is None:
            
                # Setting the value of min_Node as the current node
                min_Node = current_node
                
            elif shortest_distance[min_Node] > shortest_distance[current_node]:
                
                # If the value of min_Node is more than that of current_node, set
                # min_Node as current_node
                min_Node = current_node
                
        # Iterating through the connected nodes of min_Node (for
        # example, a is connected with b and c having values 10 and 3
        # respectively) and the weight of the edges
        for connected_nodes, weight in unvisited_nodes[min_Node].items():

            # checking if the value of min_Node + value of the edge
            # that connects this neighbor node with current_node
            # is less than the value of current_node
            if (shortest_distance[min_Node] + weight) < shortest_distance[connected_nodes]:
                
                # If true set the new value as the minimum distance of that connection
                shortest_distance[connected_nodes] = shortest_distance[min_Node] + weight
                
                # Adding the current node (min_Node) as the predecessor of the child node
                predecessor[connected_nodes] = min_Node
        
        # After the node has been visited, remove it from unvisited node
        del unvisited_nodes[min_Node]
        
    # Till now the shortest distance between the source node and target node
    # has been found. Now the shortest path is retrieved from predecessor in route.
    # Set the current node as the target node
    node = target
    
    # Starting from the goal node, we will go back to the source node and
    # see what path we followed to get the smallest distance using a while loop
    while node != source:
        
        # As it is not necessary that the target node can be reached from
        # the source node, we must enclose it in a try block
        try:
            route.append(node)
            node = predecessor[node]
        except Exception:
            print('Path not reachable')
            break

    # Including the source in the path
    route.append(source)
    
    # If the node has been visited,
    if node not in unvisited_nodes:

        # print the shortest distance and the path taken
        print(shortest_distance, route)

    # Remove the below comment if you want to show the the shortest distance
    # from source to every other node
    # print(shortest_distance)

# definition of a graph for the function Dijkstra to work :
graph = {'a':{'b':5,'c':2},'b':{'c':1,'d':3},'c':{'b':3,'d':7},'d':{'e':7},'e':{'d':9}}
#Calling the function with source as 'a' and target as 'e'.
Dijkstra(graph,'a','e')
