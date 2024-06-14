def graphColoring(graph, k, V):
    colour=[-1]*V
    def possible(col,V,graph):
        for i in range(V):
            if(graph[V][i]==1):
                if(col==colour[i]):
                    return False
        return True
    def solve(graph,k,v,V):
        if(v==V):
            return True
        for i in range(k):
            if(possible(i,v,graph)):
                colour[v]=i
                if(solve(graph,k,v+1,V)):
                    return True
                colour[v]=-1
        return False
    return solve(graph,k,0,V)
