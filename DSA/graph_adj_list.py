def add_node(v):
    if v in graph:
        print(v," is allready present in graph")
    else:
        graph[v] = []
def add_edge(v1,v2,cost):         # weighted undirected graph
    if v1 not in graph:
        print(v1,"not preset in graph")
    elif v2 not in graph:
        print(v2,"not present in graph")
    else:
        list1 = [v2,cost]         # weighted undirected graph
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

        # graph[v1].append(v2)  #| unweighted undirected graph
        # graph[v2].append(v1)  #|

        list1 = [v2,cost]       # weighted directed graph
        graph[v1].append(list1)

        graph[v1].append(v2)      # unweighted directed graph
def delete_node(v):
    if v not in v:
        print(v,"is not present in graph")
    else:
        # graph.pop(v)                    #|
        # for i in graph:                 #|
        #     list1 = graph[i]            #| unweighted directed,undirected graph 
        #     if v in list1:              #|
        #         list1.remove(v)         #|

        graph.pop(v)                    #|
        for i in graph:                 #|
            list1 = graph[i]            #| weighted undirected graph
            for j in list1:             #|
                if v == j[0]:           #|
                    list1.remove(j)     #|
                            
def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"not present in graph")
    elif v2 not in graph:
        print(v2,"not present in graph")
    else:
        # if v2 in graph[v1]:             #|
        #     graph[v1].remove(v2)        #| unweighted undirected graph
        #     graph[v2].remove(v1)        #|

        # if v2 in graph[v1]:               #|
        #     graph[v1].remove(v2)          #| unweighted directed graph
        
        temp = [v2,cost]                    #|
        temp1 = [v1,cost]                   #|
        if temp1 in graph[v1]:              #| weighted undirected graph
            graph[v1].remove(temp1)         #|
            graph[v1].remove(temp)          #|

graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_edge("A","B",10)   #weighted undirected graph 
add_edge("B","E",3)  
add_edge("A","C",5)
add_edge("A","D",4)
add_edge("B","D",7)
add_edge("C","D",1)
add_edge("E","D",2)

# add_edge("A","B")     #unweifgted directed graph
# add_edge("B","E")
# add_edge("A","C")
# add_edge("A","D")
# add_edge("B","D")
# add_edge("F","C")
# add_edge("F","G")
# add_edge("G","D")
print(graph)
delete_edge("C","D",1)
print(graph)

# delete_edge , add_edge using adjacency matrix for multiple edges in weighted directed undirected graph remaining have to learn self chatgpt or something 