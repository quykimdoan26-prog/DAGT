def countEven(self, num):
        numsum = sum(int(digit) for digit in str(num))

        if numsum % 2 == 0:
            return num // 2
        else:
            return (num-1) // 2