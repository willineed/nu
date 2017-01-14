# 1.1 Part A
# Konverterer fahrenheit til celcius

fahrenheit = float(input("Enter temperature in Fahrenheit:"))
celcius = (fahrenheit - 32) / 1.8
print("The temperature in Celcius is:", celcius)

# 1.2 Part B
# Regner arealet af en trapez ud
print("Areal af en trapez.")
højde_trapez = float(input("Indtast højden af trapezen:")) 
længde_trapez_bund = float(input("Indtast længden af grundlinjen:"))
længde_trapez_top = float(input("Indtast længden af trapezens top:"))
areal_trapez = 1 / 2 * (længde_trapez_top + længde_trapez_bund) * højde_trapez
print("Areal af trapez= ", areal_trapez)

# 1.3 Part C
# Regner arealet af en cirkel ud
print("Areal af en cirkel.")
radius = float(input("Indtast radius af cirklen:"))                          
areal_cirkel = 3.14 * radius ** 2
print("Areal af cirkel= ", areal_cirkel)
print("\nSå er programmet færdigt.\n\nLavet af:  William Abildtrup")
