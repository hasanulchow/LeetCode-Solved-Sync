class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # Check if password contains at least one digit, one lowercase letter, and one uppercase letter.
        # If any of these categories are missing, increment the 'ans' by 1.
        ans = 0 if any([password[i].isdigit() for i in range(len(password))]) else 1
        ans += 0 if any([password[i].islower() for i in range(len(password))]) else 1
        ans += 0 if any([password[i].isupper() for i in range(len(password))]) else 1

        # If the length of the password is less than 6, return the number of characters
        # needed to make it at least 6 long, ensuring it also satisfies the character type requirements.
        if len(password) < 6:
            return max(6 - len(password), ans)

        # Group consecutive repeating characters (e.g., 'aaa' becomes [3])
        g = [len(list(g)) for _, g in groupby(password)]
        # Filter out groups where the length of the repeated characters is <= 2
        g = [r for r in g if r > 2]

        # If the length of the password is greater than 20, shorten it
        if len(password) > 20:
            # Modify group lengths to avoid sequences larger than 3 by taking modulo 3
            g = [(r % 3, r) for r in g]
            # Heapify the list to efficiently process the longest sequences first
            heapify(g)
            for i in range(len(password) - 20):
                if not g:
                    break
                _, r = heappop(g)  # Get the largest group
                if r > 3:
                    # Reduce the size of the group by 1 and push it back to the heap
                    heappush(g, ((r - 1) % 3, r - 1))
            g = [r for _, r in g]

        # The final answer is the maximum of:
        # - the 'ans' (character type requirements),
        # - the sum of groups divided by 3 (for replacements),
        # - the number of characters to remove if the length is greater than 20.
        return max(ans, sum(r // 3 for r in g)) + max(0, len(password) - 20)
