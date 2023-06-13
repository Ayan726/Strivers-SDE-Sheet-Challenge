class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        l = []
        for i in range(n):
            l.append([start[i], end[i]])
        data = sorted(l, key=lambda x: x[1])
        maxi = data[0][1]
        res, i = 1, 1
        
        while i<n:
            if data[i][0] > maxi:
                res += 1
                maxi = data[i][1]
            i += 1
        return res

