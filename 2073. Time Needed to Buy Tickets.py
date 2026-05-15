class Solution(object):
    def timeRequiredToBuy(self, tickets, k): # Thêm self ở đây
        seconds = 0
        target_tickets = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                # Người đứng trước hoặc chính là k
                seconds += min(tickets[i], target_tickets)
            else:
                # Người đứng sau k
                seconds += min(tickets[i], target_tickets - 1)
                
        return seconds
        