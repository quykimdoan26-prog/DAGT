
def plusOne(digits):
    result = int("".join(str(x) for x in digits )) #1,2,3
    result+=1 # 124
    digits.clear()
    for i in str(result):
       digits.append(int(i))
    return digits

print(plusOne([1,2,3]))