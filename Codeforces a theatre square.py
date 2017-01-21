n, m, a = map(int,input("Enter n, m and a in that order:").split())

h = n // a
if n%a != 0: h+=1 # Jeg kom umiddelbart først frem til flagstones_needed = n // a * m // a
# men det vil ikke virke, da det bliver rundet ned og så får du derfor det forkerte antal.
# Jeg var nødt til at slå videre op for at finde frem til dette.
 
w = m//a
if m%a != 0: w+=1

print(h*w)
