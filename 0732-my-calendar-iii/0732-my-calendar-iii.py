class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.events, (start, 1))
        bisect.insort(self.events, (end, -1))
        cur_book = max_book = 0
        for event, t in self.events:
            cur_book += t
            max_book = max(max_book, cur_book)
        return max_book