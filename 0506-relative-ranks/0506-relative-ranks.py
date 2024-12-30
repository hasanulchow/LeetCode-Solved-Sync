class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Step 1: Create a copy of the scores array and sort it in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Step 2: Create a dictionary to map scores to ranks
        rank_map = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
        
        # Step 3: Assign ranks to each athlete based on their scores
        answer = [rank_map[score[i]] for i in range(len(score))]
        
        return answer
        