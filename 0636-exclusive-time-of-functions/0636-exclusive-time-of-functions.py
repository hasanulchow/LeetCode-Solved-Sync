class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ## RC ##
		## APPROACH : STACK ##
        stack, res = [], [0] * n
        for log in logs:
            id, func, curr_time = log.split(":")
            id, curr_time = int(id), int(curr_time)
            if func == "start":
                stack.append((id, curr_time))
            elif func == "end" and id == stack[-1][0]:
                pop_id, insert_time = stack.pop()
                time_taken = curr_time - insert_time + 1
                res[pop_id] += time_taken
                
                # gist, we have remove overlap time, if a process is in the stack indicates there is overlap with the last process
                if stack:
                    res[stack[-1][0]] -= time_taken # time taken by this process is the overlap time for prev process in stack
        return res
        