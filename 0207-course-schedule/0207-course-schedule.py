class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determine if it is possible to finish all courses given the prerequisites.
        :param numCourses: int - Total number of courses
        :param prerequisites: List[List[int]] - Prerequisite pairs [course, prerequisite]
        :return: bool - True if all courses can be finished, False otherwise
        """
        # Dictionary to store prerequisites for each course
        pre = defaultdict(list)

        # Build the adjacency list (course -> list of prerequisites)
        for course, p in prerequisites:
            pre[course].append(p)
        
        # Set to keep track of courses in the current DFS path (to detect cycles)
        taken = set()

        # Helper function to perform DFS on a course
        def dfs(course):
            # If the course has no prerequisites, it's already complete
            if not pre[course]:
                return True
            
            # If the course is already in the current DFS path, a cycle is detected
            if course in taken:
                return False
            
            # Mark the course as being processed
            taken.add(course)

            # Recursively check all prerequisites
            for p in pre[course]:
                if not dfs(p):
                    return False
            
            # Clear the prerequisites for this course to mark it as processed
            pre[course] = []
            return True
        
        # Check all courses using DFS
        for course in range(numCourses):
            if not dfs(course):
                return False  # If any course cannot be completed, return False

        # If all courses are processed without detecting a cycle, return True
        return True
