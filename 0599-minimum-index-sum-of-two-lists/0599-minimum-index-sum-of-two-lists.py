class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = inf
        list3 = set(list2)
        for i, word in enumerate(list1):
            if word in list3:
                if (i_sum := i + list2.index(word)) < index_sum:
                    result = [word]
                    index_sum = i_sum
                elif i_sum == index_sum:
                    result.append(word)
        return result
    