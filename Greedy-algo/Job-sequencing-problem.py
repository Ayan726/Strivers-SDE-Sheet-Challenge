class Solution:
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
        jobs.sort(key= lambda x: x.profit, reverse=True)
        sz = max(jobs, key= lambda x: x.deadline).deadline
        track = [-1]*(sz+1)
        prof, cnt = 0, 0
        for el in jobs:
            if track[el.deadline] == -1:
                track[el.deadline] = 1
                prof += el.profit
                cnt += 1
            else:
                i = el.deadline
                while i>0:
                    if track[i] == -1:
                        track[i] = 1
                        prof += el.profit
                        cnt += 1
                        break
                    i -= 1
        
        return (cnt, prof)
            
