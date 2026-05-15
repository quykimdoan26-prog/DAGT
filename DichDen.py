class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        # Bước 1: Thu thập tất cả các thành phố có đường đi XUẤT PHÁT từ đó
        start_cities = set()
        for path in paths:
            start_cities.add(path[0])
            
        # Bước 2: Duyệt qua các thành phố ĐẾN, thành phố nào không nằm trong start_cities thì đó là đích
        for path in paths:
            destination = path[1]
            if destination not in start_cities:
                return destination