'''class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        # we will create a node
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return node
    def printList(self):
        copy = self.head
        while copy is not None:
            print(copy.data,end='->')
            copy = copy.next
    
    def InsertAtEnd(self, ref):
        copy = self.head
        while copy.next is not None:
            copy = copy.next
        copy.next = ref 
    
    def FindCyclePresentOrNot(self):
        ptr1 = self.head
        ptr2 = self.head
        
        while ptr2.next.next is not None:
            ptr2 = ptr2.next.next
            ptr1 = ptr1.next
            if(ptr2 == ptr1):
                print("Cycle found at", ptr1.data)
                return ptr1
        return None
    
    def findMeetingPoint(self, ptr):
        if(ptr == None):
            print("No cycle Found!")
            return
        start = self.head
        while start!=ptr:
            ptr = ptr.next
            start = start.next
        print("Cycle started At", ptr.data)
        
    def removeCycle(self, ptr):
        if(ptr == None):
            print("No cycle Found!")
            return
        start = self.head
        while start.next!=ptr.next:
            ptr = ptr.next
            start = start.next
        ptr.next = None
        print("Cycle Removed!")
x = LinkedList()
x.insertAtBeginning(6)
x.insertAtBeginning(7)
x.insertAtBeginning(8)
x.insertAtBeginning(5)
x.insertAtBeginning(4)

copyNode = x.insertAtBeginning(3)

x.insertAtBeginning(2)
x.insertAtBeginning(1)

x.InsertAtEnd(copyNode)
# x.printList()
ptr = x.FindCyclePresentOrNot()
x.findMeetingPoint(ptr)
print()
x.removeCycle(ptr)
print()
x.printList()'''

'''def kruskal_algo(self):
    result = []
    i, e = 0, 0
    self.graph = sorted(self.graph, key=lambda item: item[2]) # Sorting edges in non-decreasing order
    
    parent = []
    rank = []
    
    for node in range(self.V):
        parent.append(node)
        rank.append(0)
        
    while e < self.V - 1: # Because MST should have n-1 edges
        u, v, w = self.graph[i]
        i = i + 1
        
        x = self.find(parent, u)
        y = self.find(parent, v)
        
        if x != y:
            e = e + 1
            result.append([u, v, w])
            self.union(parent, rank, x, y)
    
    return result'''
'''class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

        #search function

    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot]  > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Applying Krushkal algorithm
    def krushkal_algo(self):
        result = []
        i,e = 0,0
        self.graph = sorted(self.graph, key = lambda item: item[2])
        #item[2] means --- taking edges..sorting

        parent = []
        rank = []
        for node in range(self.v):
            parent.append(node)
            rank.append(0)
        while e < self.v - 1:
            u, v, w = self.graph[i]
            i = i+1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x!= y:
                e =e +1
                result.append([u,v,w])
                self.apply_union(parent,rank,x,y)
        for u,v,weight in result:
            print("%d - %d: %d" %(u,v,weight))
g = Graph(6)
g.add_edge(0,1,4)
g.add_edge(0,2,4)
g.add_edge(1,2,2)
g.add_edge(1,0,4)
g.add_edge(2,0,4)
g.add_edge(2,1,2)
g.add_edge(2,3,3)
g.add_edge(2,5,2)
g.add_edge(2,4,4)
g.add_edge(3,2,3)
g.add_edge(3,4,3)
g.add_edge(4,2,4)
g.add_edge(4,3,3)
g.add_edge(5,2,2)
g.add_edge(5,4,3)
g.krushkal_algo()'''

# Prim's Algorithm in Python


INF = 9999999
# number of vertices in graph
V = 5
# create a 2d array of size 5x5
# for adjacency matrix to represent graph
G = [[0, 19, 5, 0, 0],
     [9, 0, 5, 19, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]
# create a array to track selected vertex
# selected will become true otherwise false
selected = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight\n")
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1

