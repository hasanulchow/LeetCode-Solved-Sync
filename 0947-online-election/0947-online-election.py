class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons=[]
        self.times=[]
        self.d=defaultdict(int)
        self.mx=0
        for person,time in zip(persons,times):
            self.times.append(time)
            self.d[person]+=1
            if self.d[person]>=self.mx:
                self.persons.append(person)
                self.mx=self.d[person]
            else: self.persons.append(self.persons[-1])

    def q(self, t: int) -> int:
        return self.persons[bisect.bisect_right(self.times,t)-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)