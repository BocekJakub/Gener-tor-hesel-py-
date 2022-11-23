import random

lower = ("abcdefghijklmnopqrstuvwxyz")
upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
number = ("1234567890")
special = ("-_?#&@.!/()%=*+§")

print("GENERÁTOR HESLA")
print("---------------")
count_symbols = int(input("Zadejte kolik znaků má mít heslo: "))
lower_in = input("Chcete aby obsahovalo malá písmena? (A/N): ").lower()
upper_in = input("Chcete aby obsahovalo velká písmena? (A/N): ").lower()
number_in = input("Chcete aby obsahovalo číslice? (A/N): ").lower()
special_in = input("Chcete aby obsahovalo speciální znaky? (A/N): ").lower()

symbols = ""

if lower_in == "a":
    symbols += lower
if upper_in == "a":
    symbols += upper
if number_in == "a":
    symbols += number
if special_in == "a":
    symbols += special


def generator(num, sym):
    heslo = ""
    length_symbols = len(sym)
    for i in range(num):
        ran_num = random.randrange(0, length_symbols)
        heslo += sym[ran_num]
    return heslo

print("_______________")
pokracovat = "a"
if len(symbols) != 0:
    while(pokracovat == "a"):
        generovane_heslo = generator(count_symbols, symbols)
        print("Generované heslo: " + generovane_heslo)
        pokracovat = input("Chcete generovat nové heslo? (A/N)" ).lower()
else: 
    print("Nevybrány žádné znaky!!!")
