from collections import defaultdict
def groupAnagrams(strs):
        groups = defaultdict(list)
        for s in strs:
        # Sắp xếp ký tự trong chuỗi để tạo key
            key = ''.join(sorted(s)) # sắp xếp tạo key trùng nhau với các chữ cái là lộn xộn
            groups[key].append(s) # thêm chuỗi "s" vào danh sách của key. 
    
        return list(groups.values()) #trả về một list value của các key là từng phần tử trong list


thu=['aet','tea','bat','bta','tan','nan']
print(groupAnagrams(thu))

