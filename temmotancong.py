def findPoisonedDuration(timeSeries, duration):
    if not timeSeries:
        return 0
    
    total = 0
    for i in range(len(timeSeries) - 1):
        # Khoảng thời gian Ashe bị độc giữa hai lần tấn công liên tiếp
        total += min(timeSeries[i+1] - timeSeries[i], duration)
    
    # Cộng thêm cho lần tấn công cuối cùng
    total += duration
    
    return total
