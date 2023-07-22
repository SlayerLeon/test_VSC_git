name = str(input("How you name: \n"))
print(f"Hi, {name}")
try:
    quest = str(input(f"My name is {name} \nYou like eat fish?"))
except Exception as e:
    print(f"Error type data: {e}")
if quest != ("yes" | "y" | "n" | "no"):
    print("Fail")
else:
    print("Nice")

