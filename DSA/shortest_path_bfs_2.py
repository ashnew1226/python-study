from collections import deque
def add_node(v):
    if v in graph:
        print(v," is allready present in graph")
    else:
        graph[v] = []
def add_edge(v1,v2):         # weighted undirected graph
    if v1 not in graph:
        print(v1,"not preset in graph")
    elif v2 not in graph:
        print(v2,"not present in graph")
    else:
        # list1 = [v2,cost]         # weighted undirected graph
        # list2 = [v1,cost]
        # graph[v1].append(list1)
        # graph[v2].append(list2)

        graph[v1].append(v2)  #| unweighted undirected graph
        graph[v2].append(v1)  #|

        # list1 = [v2,cost]       # weighted directed graph
        # graph[v1].append(list1)

def shortest_path(graph,node,target):
    if node not in graph:
        print(node,"not in graph")
    elif target not in graph:
        print(target,"not in graph")
    else:
        visited = {}
        queue = deque()
        visited[node] = None   # starting node is not having parent so it is none
        queue.append(node)
        while queue:
            current = queue.popleft()
            if current == target:
                path = []
                while current:
                    path.append(current)
                    current = visited[current]
                return path[::-1]
            for i in graph[current]:
                if i not in visited:
                    visited[i] = current
                    queue.append(i)





graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_node("H")
add_node("I")
# add_edge("A","B",10)   #weighted undirected graph 
# add_edge("B","E",3)  
# add_edge("A","C",5)
# add_edge("A","D",4)
# add_edge("B","D",7)
# add_edge("C","D",1)
# add_edge("E","D",2)

# add_edge("A","B")   #unweighted undirected graph 
# add_edge("A","C")
# add_edge("B","D")
# add_edge("C","D")
# add_edge("F","E")  
# add_edge("F","G")


add_edge("A","B")   #unweighted undirected graph 
add_edge("A","D")
add_edge("A","F")
add_edge("B","C")
add_edge("C","D")  
add_edge("C","E")
add_edge("C","H")
add_edge("D","I")
add_edge("D","G")
add_edge("H","G")
# add_edge("C","H")

# add_edge("A","B")   #disconnected graph 
# add_edge("A","C")
# add_edge("B","D")
# add_edge("C","D")
# add_edge("F","E")  
# add_edge("F","G")

# add_edge("A","B")     #strongly connected graph
# add_edge("C","A")
# add_edge("B","D")
# add_edge("B","C")
# add_edge("D","C")
# add_edge("E","D")

# add_edge("A","B")   #check connected disconnected 
# add_edge("A","C")
# add_edge("B","C")  
# add_edge("C","D")
# add_edge("E","F")
# add_edge("E","G")

# add_edge("A","B")   #check disconnected 
# add_edge("A","C")
# add_edge("A","D")  
# add_edge("B","E")
# add_edge("D","E")
# add_edge("C","D")
# add_edge("C","F")
# add_edge("E","F")
# add_edge("E","G")

# add_edge("A","B")     #unweifgted directed graph
# add_edge("B","E")
# add_edge("A","C")
# add_edge("A","D")
# add_edge("B","D")
# add_edge("F","C")
# add_edge("F","G")
# add_edge("G","D")
print(graph)
result = shortest_path(graph,"A","G")
print(f"shortest_path is - {result}")
# BFS("C",graph,visited1)
# for i in list(graph):
#     if i not in visited1:
#         print("disconnected graph")
#         break
# else:
#     BFS("A",graph1,visited_t)
#     if visited1 == visited_t:
#         print("strongly connected graph")
#     else:
#         print("weakly connected graph")
# delete_edge("C","D",1)
# DFS("A",visited,graph)
# print(graph)

# for i in list(graph):                           #|
#     if i not in visited:                        #|
#         print("the graph is disconnected")      #| undirected graph
#         break                                   #|
# else:                                           #|
#     print("this is connected graph")            #|

# for i in list(graph):
#     if i not in visited:
#         print("the graph is disconnected")
#         break
# else:
#     DFS("A",visited1,graph1)
#     if visited == visited1:
#         print("strongly connected graph")
#     else:
#         print("this is weakly connected graph")

# delete_edge , add_edge using adjacency matrix for multiple edges in weighted directed undirected graph remaining have to learn self chatgpt or something 