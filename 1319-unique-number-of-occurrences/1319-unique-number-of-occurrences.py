class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            if arr[i] in dic.keys():
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1

        lst=list(dic.values())
        lst2=list(set(lst))
        if len(lst)==len(lst2):
            return True

        return False
        