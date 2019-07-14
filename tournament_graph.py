results = {'nasaji' : [ 'naft_masjed_soleiman' , 'saipa' , 'mashinsazi' , 'esteghlal_khoozestan' , 'sanat_naft' , 'peykan' ] ,
	'zobahan' : [ 'nasaji' , 'mashinsazi' , 'sanat_naft' , 'peykan' , 'foolad' ] ,
	'padideh' : [ 'esteghlal_khoozestan' , 'sanat_naft' , 'sepidrood' , 'peykan' , 'zobahan' , 'foolad' , 'naft_masjed_soleiman' , 'nasaji' , 'saipa' ] ,
	'perspolis' : [ 'esteghlal' , 'padideh' , 'foolad' , 'esteghlal_khoozestan' , 'naft_masjed_soleiman' , 'sanat_naft' , 'nasaji' , 'sepidrood' , 'peykan' , 'saipa' , 'zobahan' , 'sepahan' , 'teraktorsazi' , 'mashinsazi' , 'pars_jonoobi' ] ,
	'sepidrood' : [ 'mashinsazi' , 'sanat_naft' , 'zobahan' , 'pars_jonoobi' , 'foolad' , 'nasaji' ] ,
	'saipa' : [ 'sepidrood' , 'zobahan' , 'pars_jonoobi' , 'foolad' , 'naft_masjed_soleiman' ] ,
	'pars_jonoobi' : [ 'naft_masjed_soleiman' , 'nasaji' , 'esteghlal' , 'padideh' , 'esteghlal_khoozestan' , 'peykan' , 'zobahan' ] ,
	'foolad' : [ 'pars_jonoobi' , 'naft_masjed_soleiman' , 'nasaji' , 'mashinsazi' , 'peykan' , 'teraktorsazi' ] ,
	'esteghlal_khoozestan' : [ 'sanat_naft' , 'sepidrood' , 'zobahan' , 'foolad' , 'saipa' , 'sepahan' ] ,
	'mashinsazi' : [ 'esteghlal_khoozestan' , 'pars_jonoobi' , 'saipa' , 'sepahan' , 'padideh' ] ,
	'sanat_naft' : [ 'mashinsazi' , 'teraktorsazi' , 'pars_jonoobi' , 'foolad' , 'saipa' ] ,
	'sepahan' : [ 'sanat_naft' , 'sepidrood' , 'zobahan' , 'teraktorsazi' , 'pars_jonoobi' , 'foolad' , 'naft_masjed_soleiman' , 'nasaji' , 'esteghlal' , 'saipa' , 'padideh' ] ,
	'teraktorsazi' : [ 'nasaji' , 'saipa' , 'mashinsazi' , 'padideh' , 'esteghlal_khoozestan' , 'sepidrood' , 'peykan' , 'zobahan', 'pars_jonoobi' ] ,
	'naft_masjed_soleiman' : [ 'teraktorsazi' , 'mashinsazi' , 'esteghlal_khoozestan' , 'sanat_naft' , 'sepidrood' , 'peykan' , 'zobahan' ] ,
	'peykan' : [ 'saipa' , 'sepahan' , 'mashinsazi' , 'esteghlal_khoozestan' , 'sanat_naft' , 'sepidrood' ] ,
	'esteghlal' : [ 'peykan' , 'zobahan' , 'teraktorsazi' , 'foolad' , 'naft_masjed_soleiman' , 'nasaji' , 'saipa' , 'mashinsazi' , 'padideh' , 'esteghlal_khoozestan' , 'sanat_naft' , 'sepidrood' ]}

nresults = {1 : [ 14 , 6 , 10 , 9 , 11 , 15 ] ,
	2 : [ 1 , 10 , 11 , 15 , 8 ] ,
	3 : [ 9 , 11 , 5 , 15 , 2 , 8 , 14 , 1 , 6 ] ,
	4 : [ 16 , 3 , 8 , 9 , 14 , 11 , 1 , 5 , 15 , 6 , 2 , 12 , 13 , 10 , 7 ] ,
	5 : [ 10 , 11 , 2 , 7 , 8 , 1 ] ,
	6 : [ 5 , 2 , 7 , 8 , 14 ] ,
	7 : [ 14 , 1 , 16 , 3 , 9 , 15 , 2 ] ,
	8 : [ 7 , 14 , 1 , 10 , 15 , 13 ] ,
	9 : [ 11 , 5 , 2 , 8 , 6 , 12 ] ,
	10 : [ 9 , 7 , 6 , 12 , 3 ] ,
	11 : [ 10 , 13 , 7 , 8 , 6 ] ,
	12 : [ 11 , 5 , 2 , 13 , 7 , 8 , 14 , 1 , 16 , 6 , 3 ] ,
	13 : [ 1 , 6 , 10 , 3 , 9 , 5 , 15 , 2, 7 ] ,
	14 : [ 13 , 10 , 9 , 11 , 5 , 15 , 2 ] ,
	15 : [ 6 , 12 , 10 , 9 , 11 , 5 ] ,
	16 : [ 15 , 2 , 13 , 8 , 14 , 1 , 6 , 10 , 3 , 9 , 11 , 5 ]}


graph = {'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']}

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def find_longest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    longest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_longest_path(graph, node, end, path)
            if newpath:
                if not longest or len(newpath) > len(longest):
                    longest = newpath
    return longest

def check_tournament_rule(graph):
    count = len(graph)*(len(graph) - 1)/2
    for node1 in graph:
        for node2 in graph[node1]:
            count = count - 1
            if node2 in graph:
                for node3 in graph[node2]:
                    if node3 == node1:
                        return 0
            n = 0
            for node4 in graph[node1]:
                if node2 == node4:
                    n = n + 1
                    if n == 2:
                        return 0
    if count == 0:
        return 1
    return 0

def find_hamiltonian_path(graph):
    if check_tournament_rule(graph) == 0:
        return "Not A Tournament"
    index = 1
    max_count = 0
    max_index = 1
    for node3 in graph:
        if len(graph[node3]) > max_count:
            max_count = len(graph[node3])
            max_index = index
        index = index + 1
    index = 1
    index2 = 1
    min_count = len(graph)
    min_index = 1
    for node4 in graph:
        if index == max_index:
            for node5 in graph[node4]:
               if len(graph[node5]) < min_count:
                   min_count = len(graph[node5])
                   min_index = index2 
               index2 = index2 + 1
        index = index + 1
    index = 1
    index2 = 1
    for node1 in graph:
        if index == max_index:
            for node2 in graph[node1]:
                if index2 == min_index:
                    path = find_longest_path(graph, node1, node2)
                    if len(path) == len(graph):
                        return path
                index2 = index2 + 1
        index = index + 1

def prove_hamiltonian_path():
    return "This can be proven using strong induction. Let n be the number of vertices. When n≤2, a hamiltonian path clearly exists. Now, for any given n>2, pick any arbitrary vertex v. Partition all other vertices other than v into the sets V(out) and V(in). V(out) contains all other vertices u such that the edge (v,u) exists, while V(in) contains all other vertices u such that the edge (u,v) exists. Clearly |V(out)|<n and |V(in)|<n, so by the inductive hypothesis, there is a hamiltonian path in both sets. Let H(out) be any hamiltonian path in V(out) and H(in) be any hamiltonian path in V(in). You can then form a hamiltonian path for all vertices by concatenating H(in), v, and H(out)."

def find_hamiltonian_path2(graph, area):
	if check_tournament_rule(graph) == 0:
        return "Not A Tournament"
    if area == []:
        return []
    n = 1
    s_node = 0
    a_area = []
    b_area = []
    for node in area:
        if n == 1:
            s_node = node
            for node2 in graph[node]:
            	if node2 in area:
            		a_area.append(node2)
        if not n == 1:
        	if node not in a_area:
        		b_area.append(node)
        n = n + 1
    return find_hamiltonian_path2(graph, b_area) + [s_node] + find_hamiltonian_path2(graph, a_area)

print(find_hamiltonian_path2(results, results))