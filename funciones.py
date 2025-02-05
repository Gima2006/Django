
def checkio(num: int) -> str:
    
    if num%3 == 0: return "Fizz"
    else: return str(num)

def first_word(text: str) -> str:
    
    x = text.split(" ")
    return x[0]

def number_length(value: int) -> int:
    # your code here
    return len(str(value))

def checkio(num: int) -> str:
    # your code here
    if num%3 == 0 and num%5 == 0: return "Fizz Buzz"
    elif num%3 == 0: return "Fizz"
    elif num%5 ==  0: return "Buzz"
    else: return str(num)



print(checkio(15))
#print(number_length(123))
#print(first_word("Hola como estas"))
# assert checkio(15) == "Fizz"

