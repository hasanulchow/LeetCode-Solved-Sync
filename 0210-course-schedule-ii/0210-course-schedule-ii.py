from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Determine the order in which courses should be taken to complete all courses.
        :param numCourses: int - Total number of courses
        :param prerequisites: List[List[int]] - List of prerequisite pairs [course, prerequisite]
        :return: List[int] - A list representing the course order, or an empty list if it's not possible
        """
        # Step 1: Build the graph (adjacency list representation)
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # Add an edge from prereq to course
        
        # Step 2: Calculate the in-degree of each node
        # In-degree is the number of edges pointing to a node
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            in_degree[course] += 1  # Increment in-degree for courses that have prerequisites
        
        # Step 3: Initialize a queue with nodes that have in-degree 0
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:  # Courses with no prerequisites
                queue.append(i)
        
        # List to store the topological order of courses
        result = []
        
        # Perform topological sort using BFS
        while queue:
            # Remove a course from the queue
            node = queue.popleft()
            result.append(node)  # Add it to the result (it's safe to take this course)
            
            # Decrease the in-degree of its neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                # If a neighbor's in-degree becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check for a cycle
        # If the result list contains fewer courses than numCourses, there's a cycle
        if len(result) < numCourses:
            return []
        
        # Return the topological order of courses
        return result
