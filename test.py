from typing import List
def filp_even_odd(numbers: List[int]) -> List[int]:
    a=len(numbers)
    for i in range(a):
        if numbers[i] %2!=0:
            numbers[i]-=1
        elif numbers[i] %2==0:
            numbers[i]+=1
    return numbers