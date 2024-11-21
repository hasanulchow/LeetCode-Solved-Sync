class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []  # Step 1: Initialize an empty list to store the final result (after all collisions).

        # Step 2: Iterate over each asteroid in the input list
        for a in asteroids:
            # Step 3: Check if there is any potential collision
            # A collision can only occur if:
            # 1. There's at least one asteroid in 'res'
            # 2. The current asteroid is moving left (a < 0)
            # 3. The last asteroid in 'res' is moving right (res[-1] > 0)
            while res and a < 0 < res[-1]:
                if -a > res[-1]:  # Step 4: The current asteroid is larger, so it destroys the one in 'res'
                    res.pop()  # Remove the last asteroid from 'res'
                    continue  # Check if the current asteroid can collide with the next one in 'res'
                elif -a == res[-1]:  # Step 5: Both asteroids are of the same size, so they both destroy each other
                    res.pop()  # Remove the last asteroid from 'res'
                break  # Step 6: Stop checking further collisions, as the current asteroid is either destroyed or it survived the collision

            else:  # Step 7: If no collision occurs, add the current asteroid to the result list 'res'
                res.append(a)

        # Step 8: Return the result list which contains the asteroids that survived after all collisions.
        return res
