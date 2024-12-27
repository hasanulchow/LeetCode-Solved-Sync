class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:        
        result = [False for _ in requests]
        
        connected_components = [{i} for i in range(n)]
        
        connected_comp_dict = {}
        for i in range(n):
            connected_comp_dict[i] = i
        
        banned_by_comps = [set() for i in range(n)]
        for res in restrictions:
            banned_by_comps[res[0]].add(res[1])
            banned_by_comps[res[1]].add(res[0])
        for i,r in enumerate(requests):
            n1, n2 = r[0], r[1]
            c1, c2 = connected_comp_dict[n1], connected_comp_dict[n2]
            if c1 == c2:
                result[i] = True
            else:
                if not (connected_components[c1].intersection(banned_by_comps[c2]) or connected_components[c2].intersection(banned_by_comps[c1])):
                    connected_components[c1].update(connected_components[c2])
                    banned_by_comps[c1].update(banned_by_comps[c2])
                    for node in connected_components[c2]:
                        connected_comp_dict[node] = c1
                    result[i] = True
                
        return result