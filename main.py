from typing import List
def addStrNums(num1: str, num2: str) -> str:
    try:
        a=int(num1)
        b=int(num2)
        sum=a+b
        sumf=str(sum)
        return sumf
    except:
        return "-1"
    print('the program is finished
