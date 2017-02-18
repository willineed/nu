# Jeg har sat print() til slut af nogle af spørgsmålene, så man kan se forskel mellem programmerne.
1.
# Jeg gætter på at den vil skrive
# 0
# 2
# 4
# 6
# 8
# Da den starter med værdien 0 og lægger 2 til hver gang den er under 10.
# ved 10 er x-værdien ikke under 10 og derfor skrives det ikke.
# I loopen printer den også x ud inden den lægger 2 til.
x = 0
while x < 10:
    print(x)
    x = x + 2
# Mit gæt er rigtigt.
print()
2.
# jeg gætter på at den printer
# 1
# 2
# 4
# 8
# 16
# 32
# Af samme årsag som den ovenover.
# Der printes først 1 og derefter ganges den med 2 hver gang.
# Den stopper ved 32, da den ikke må ramme 64.

x = 1
while x < 64:
    print(x)
    x = x * 2
# Det er rigtigt.
print()

3.
# X-værdien er ligegyldigt hvad større eller lig med 0
# da den starter på 0 og plusses med 2 hver gang
# og den stopper ligegyldigt hvad under 10.

4.
# x starter med værdien 5
# while-loopen kører indtil at 5 er mindre end 0.
# i starten printes x til 5, da den ikke er blevet minusset med 1 endnu.
# if-statementet behandler "1" som en tekst, da der er double-quotes om den.
# Dvs. at det ikke bliver behandlet som et tal og derfor ikke behandles som en true statement.
# x = x - 1 er ikke indrykket under if-statementet og minusser derfor med 1 efter hver gang.
# til sidst får vi tallene
# 5
# 4
# 3
# 2
# 1
# 0
# Den stopper her, da x-værdien ikke må under 0.
# Blast off! ender med ikke at være skrevet.

5.
done = False

while not done:
    x = float(input("Enter a number greater than zero: "))
    if x <= 0:
        print("Too small.")
    else:
        print("That is greater than zero!")
        done = True

6.
# Der skal stå while x > 0:
# og x -= 1
7.
# i behøves ikke at sættes lig 0, da den allerede starter på 0 i for-loopen.
# der behøves heller ikke i += 1, da den allerede går en op hver gang den printer i ud.
# Det er igen for-loopen når den sættes til range(10)

8.
# I sample 1 er der ikke indentation mellem de to for-loops.
# Da x-værdien starter på 0 plusses der først med 1, 10 gange, og derefter igen med 1, 10 gange. I alt 20.

# I sample 2 er der indentation.
# Det betyder, at der først plusses med 1 og derefter i for-loopen, for j in range(10):,
# bliver der plusset med 10 mere.
# Det foregår 10 gange på grund af loopen, for i in range(10):
# Man kan sige at regnestykket bliver
# (1+10)*10= 110

