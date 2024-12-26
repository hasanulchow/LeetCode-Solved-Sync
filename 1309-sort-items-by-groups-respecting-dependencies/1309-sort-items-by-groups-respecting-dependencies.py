from collections import defaultdict
class Cyclic(object):
	def __init__(self,n,g):
		super(Cyclic,self).__init__()
		self.vertices=n
		self.isCylicAns=False
		self.g=g
	def isCylic(self):
		used=[0 for i in range(self.vertices)]
		for i in range(0,self.vertices):
			if used[i]==0:
				self.dfs(i,used)
				if self.isCylicAns==True:
					return True
		return False
	def dfs(self,v,used):
		used[v]=1
		for i in self.g[v]:
			if used[i]==1:
				self.isCylicAns=True
				return
			elif used[i]==0:
				self.dfs(i,used)
		used[v]=2
class TopoSort(object):
	def __init__(self, n,g):
		super(TopoSort, self).__init__()
		self.vertices=n
		self.g=g
	def Sort(self):
		used={}
		res=[]
		for i in range(self.vertices):
			if i not in used:
				self.dfs(i,used,res)
		res.reverse()
		return res
	def dfs(self,v,used,res):
		used[v]=1
		for u in self.g[v]:
			if u not in used:
				self.dfs(u,used,res)
		res.append(v)
class TopoSortInGroup(object):
	def __init__(self, listVertices,graph,groupId,group):
		super(TopoSortInGroup, self).__init__()
		self.vertices=listVertices
		self.groupId=groupId
		self.g=graph
		self.group=group
		self.isCylicAns=False
	def Sort(self):
		used={}
		res=[]
		for i in self.vertices:
			if i not in used:
				self.dfs(i,used,res)
		res.reverse()
		return res
	def dfs(self,v,used,res):
		used[v]=1
		for u in self.g[v]:
			if u not in used and self.group[u]==self.groupId:
				self.dfs(u,used,res)
		res.append(v)
	def isCylic(self):
		used={}
		for i in self.vertices:
			if i not in used:
				# print(used)
				self.dfsCyclic(i,used)
				if self.isCylicAns==True:
					return True
		return False
	def dfsCyclic(self,v,used):
		used[v]=1
		for u in self.g[v]:
			if u in used and self.group[u]==self.groupId and used[u]==1:
				self.isCylicAns=True
				return
			elif u not in used and self.group[u]==self.groupId:
				self.dfsCyclic(u,used)
		used[v]=2
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
    	graph=[[]for i in range(n)]
    	idx_group=defaultdict(list)
    	graph_group=defaultdict(list)
    	for v in range(n):
    		for u in beforeItems[v]:
    			graph[u].append(v)
    	for i in range(n):
    		if group[i]==-1:
    			group[i]=m
    			idx_group[m].append(i)
    			m+=1
    		else:
    			idx_group[group[i]].append(i)
    	for idgroup in range(m):
    		for idtask in idx_group[idgroup]:
    			for neighbortask in graph[idtask]:
    				if group[neighbortask]!=idgroup:
    					graph_group[idgroup].append(group[neighbortask])
    	callCycleFinding = Cyclic(m,graph_group)
    	ans=[]
    	if callCycleFinding.isCylic() == False:
    		callTopo = TopoSort(m,graph_group)
    		topoGroup = callTopo.Sort()
    		for idgroup in topoGroup:
    			calTopoInsideGroup = TopoSortInGroup(idx_group[idgroup],graph,idgroup,group)
    			if calTopoInsideGroup.isCylic() == False:
    				ans.extend(calTopoInsideGroup.Sort())
    			else:
    				ans=[]
    				return ans
    	return ans
		