def add_node(v):
    global node_count
    if v in nodes:
        print(v,"node is allready present")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:                 # column of graph
            n.append(0)
        temp = []
        for i in range(node_count):     # row of graph 
            temp.append(0)
        graph.append(temp)
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"given node is not present")
    elif v2 not in nodes:
        print(v2,"given node is not present")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"can't delete Node, node is not present ")
    else:
        index1 = nodes.index(v)
        node_count = node_count - 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
        
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not present in graph")
    if v2 not in nodes:
        print(v2,"not present in graph")
    else:
        index1 = nodes.index(v1)        #|
        index2 = nodes.index(v2)        #| weighted ,unweighted directed graph
        graph[index1][index2] = 0       #|
        graph[index2][index1] = 0       #|

        # graph[index1][index2] = 0       #| for directed graph

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j]), "<3", end=" ")
        print()


nodes = []
graph = []
node_count = 0
# print("Before adding nodes")
# print(nodes)
# print(graph)
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",9)
print("Before deleting")
print_graph()
# delete_node("C")
print("After deleting")
delete_edge("A","C")
print(nodes)
print_graph()