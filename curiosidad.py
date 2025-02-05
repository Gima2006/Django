def is_even(num: int) -> bool:
    # your code here
    if num == 0 or num == 2:
        print("si")
        return True
    elif num/2 > 1:
        print("iterando")
        return is_even(num%2)
    else: 
        return False
    
    
    
print(is_even())

def determine_sign(num: int) -> str:
    # your code here
    if num > 0:
        return "positive"
    elif num == 0:
        return "zero"
    else: 
        return "negative"


def determine_sign(num: int) -> str:
    return "zero" * int(num == 0) + "positive" * int(num > 0) + "negative" * int(num < 0)


print("Example:")
print(determine_sign(11))


