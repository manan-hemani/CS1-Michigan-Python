richter=input("Please enter a Richter Scale Value: ")
richter_float=float(richter)
richter_to_joules=10**((1.5*richter_float)+4.8)
richter_to_tons=richter_to_joules/(4.184*(10**9))
print("Your Richter value: ",richter_float)
print("Equivalence in Joules: ",richter_to_joules)
print("Equivalence in Tons of TNT: ",richter_to_tons)

#Points to Ponder
# On inputting negative values it calculates the energy i.e joules and its tons in TNT
# on inputting string value it generates error as can't convert string to float 