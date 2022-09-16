import math

def Bellman_Ford(graph,source,target):
    
    # Initialiser les tableaux
    shortest_distance = {}
    pred = {}
    route = []

    for current_node, next_nodes in graph.items():
        shortest_distance[current_node] = math.inf
    shortest_distance[source] = 0
    
    # jusqu'à vérification de la condition d'arrêt
    for k in range (1, len(graph)-1):

        # pour tout sommet
        for node, nextNodes in graph.items():
            
            # calculer les meilleurs coûts associés à l'itération k et stocker les prédécesseurs correspondants
            for node2, weight in nextNodes.items():
                if (shortest_distance[node] + weight) < shortest_distance[node2]:
                    shortest_distance[node2] = shortest_distance[node] + weight
                    pred[node2] = node

    temp = shortest_distance
    print(temp)


    # BONUS DE VERIFICATION DE NEGATIF
    for node, nextNodes in graph.items():
        
        # calculer les meilleurs coûts associés à l'itération k et stocker les prédécesseurs correspondants
        for node2, weight in nextNodes.items():
            if (shortest_distance[node] + weight) < shortest_distance[node2]:
                shortest_distance[node2] = shortest_distance[node] + weight
                pred[node2] = node
        
    temp2 = shortest_distance
    print(temp2)

    # Comparaison
    for node, value in temp.items():
        print(temp[node], temp2[node])
        if temp[node] != temp2[node]:
            print("Diff")



    node = target
    while node != source:
        
        # As it is not necessary that the target node can be reached from
        # the source node, we must enclose it in a try block
        try:
            route.append(node)
            node = pred[node]
        except Exception:
            print('Path not reachable')
            break

    # Including the source in the path
    route.append(source)
    route.reverse()
        
    # Procedure d'affichage de la solution obtenue
    print(route, shortest_distance)


# Définition du graphe :
graph = {'a':{'b':-5,'c':2},'b':{'c':1,'d':3},'c':{'b':3,'d':7},'d':{'e':7},'e':{'d':9}}
# Calling the function with source as 'a' and target as 'e'.
Bellman_Ford(graph,'a','e')
