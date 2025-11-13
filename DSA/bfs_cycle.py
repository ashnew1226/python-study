def add_node(v):
    if v in graph:
        print(v," is allready present in graph")
    else:
        graph[v] = []
        graph1[v] = []       # added to check graph is strongly or weakly connected BFS/DFS
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

        graph[v1].append(v2)      # unweighted directed graph
        # print(f"graph1- {graph1}")
        graph1[v2].append(v1)     # directed graph to check strongly connected or weakly connected BFS/DFS
def DFS(node,visited,graph):
    if node not in graph:
        print("node is not present in graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)        # unweighted undirected graph
            # DFS(i[0],visited,graph)     # weighted undirected graph

visited = set()
visited1 = set()
visited_t = set()      # to check weakly and strongly for BFS

# def DFSiterative(node,graph):
#     visited = set()
#     if node not in graph:
#         print("node is not present in graph")
#         return
#     stack = []
#     stack.append(node)
#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             print(current)
#             visited.add(current)
#             for i in graph[current]:
#                 stack.append(i)

def BFS(node,graph,visited1):
    if node not in graph:
        print(node,"not in the graph")
        return
    Queue = []
    visited1 = {node:None}
    Queue.append(node)
    visited1.add(node)
    while Queue:
        current = Queue.pop(0)
        print(current)
        for i in graph[current]:
            if i not in visited1:
                parent[i] = current
                Queue.append(i)
                visited1.add(i)
            elif parent[current] != i:
                return True
    return False
graph = {}
graph1 = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
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
# add_edge("B","E")  
# add_edge("E","D")
# add_edge("A","D")

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

add_edge("A","B")   #check disconnected 
add_edge("A","C")
add_edge("A","D")  
add_edge("B","E")
add_edge("D","E")
add_edge("C","D")
add_edge("C","F")
add_edge("E","F")
add_edge("E","G")

# add_edge("A","B")     #unweifgted directed graph
# add_edge("B","E")
# add_edge("A","C")
# add_edge("A","D")
# add_edge("B","D")
# add_edge("F","C")
# add_edge("F","G")
# add_edge("G","D")
print(graph)
if BFS("A",visited1,graph):
    print("cycle is detected")
else:
    print("cycle is not detected")
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