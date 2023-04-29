"""
Write a script that prints the multiples of 7 between 0 and 100. 
Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
Remember that 0 is also a multiple of 7.
"""

def multiple(valor,multiple):
    if valor % multiple == 0:
        return True
    else:
        return False

print("Multiples of 7 between 0 and 100")
for i in range(0,101):
    if multiple(i,7):
        print(i)
    
