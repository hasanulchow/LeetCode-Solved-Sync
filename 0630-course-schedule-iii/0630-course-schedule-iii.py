from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        if not courses:
		
			# Quick response for empty course list
            return 0
        
		# Constant defined for course duration and course deadline
        DURATION, DEADLINE = 0, 1
		
		# Constant defined for top index of heap
        TOP = 0
        
        # sort courses on deadline
        courses.sort(key=lambda c: c[DEADLINE])
        
        # create a heap to store course duration, and those courses who have larger duration on the top of heap
        min_heap = []
        elapsed_time = 0
        
        for course in courses:
            
            
            if elapsed_time + course[DURATION] <= course[DEADLINE]:
                # current course can be taken
                
                # update elapsed time with current course
                elapsed_time += course[DURATION]
                
                # flip the sign to save in min-heap
                heappush(min_heap, -course[DURATION])
                
            elif min_heap:
                # current course can not be taken
                # try to swap out larger course with current smaller one
                
                if course[DURATION] < abs(min_heap[TOP]):
                    
                    # update elapsed time
                    elapsed_time -= abs(heappop(min_heap))
                    elapsed_time += course[DURATION]
                    
                    # flip the sign to save in min-heap
                    heappush(min_heap, -course[DURATION])
        
        return len(min_heap)