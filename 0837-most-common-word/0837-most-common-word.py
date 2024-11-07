class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())

        banned_set = set(banned)

        word_count = Counter(word for word in words if word not in banned_set)

        most_common_word, _ = word_count.most_common(1)[0]

        return most_common_word
        