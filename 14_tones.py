import math
#method to calculate hertz
def hertz(octave,pitch):
    n=12*(octave+1)+pitch
    frequency=440*(math.pow(2,(n-69)/12))
    return frequency

#user input 
print("This program can convert octave/ pitchciass pairs into their appropriate Hertz values. It uses the tempered scale conversions\n")
oct=int(input("Give me an octave: "))
pitch=int(input("Give me a pitch class: "))
res=hertz(oct,pitch)
print(f"{oct} . {pitch} equals {res}")

print("\nLets do that again shall we\n")
oct=int(input("Give me an octave: "))
pitch=int(input("Give me a pitch class: "))
res=hertz(oct,pitch)
print(f"{oct} . {pitch} equals {res}")

print("\nOne more time\n")
oct=int(input("Give me an octave: "))
pitch=int(input("Give me a pitch class: "))
res=hertz(oct,pitch)
print(f"{oct} . {pitch} equals {res}")

print("Thanks for using my program")