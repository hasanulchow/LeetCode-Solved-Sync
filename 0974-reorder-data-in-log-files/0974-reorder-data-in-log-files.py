class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = [log for log in logs if log.split()[1].isdigit()]
        letter = [log for log in logs if log.split()[1].isalpha()]

        letter.sort(key = lambda x: (x.split()[1:],x.split()[0]))
        return letter + digit
        