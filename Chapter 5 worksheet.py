
1.
# Koordinatsættet (0,0) er placeret i øverste venstre hjørne.
# Y-værdien går lodret nedad og kan enten være nul eller positiv.
# X-værdien går vandret og kan enten være nul eller negativ.
# Så på den måde er der kun 1 kvadrant i stedet for 4.
2.
# De her to linjer skal være der.
import pygame
pygame.init()
3.
# Farven bygger på et system, hvor at man kan vælge mængden af grøn, rød og blå farve der skal i.
# 0 er 0 af farven og 255 er maksimum af den farve.
# Så hvis du har farven (255, 255, 255) vil den vise at der skal maksimal farve af grøn, rød og blå.
# Det vises i form af farven hvid.
4.
# Hvis vi ikke forventer at farven hvid kommer til at ændre sig skal vi skrive det med stort.
# Dog hvis vi har en farve der repræsenterer himlen og vi forventer at den kommer til at ændre sig
# skal den stå med små bogstaver.
# Den ene er en konstant og den anden er en variabel.
5.
6.
# Hver gang at man trykker på noget med musen eller trykker på tastaturet, kan man bruge den kode
# til at registrere det og translatere det om til en aktion.
7.
# Det bruges til at vælge hvor ofte, at skærmen skal opdatere sig selv. Det gør at spillene kan have et hurtigere pace.
8.
# screen henfører til en variabel tidligere, hvor at man har sat skærmen til et bestemt størrelsesforhold.
# det at man skriver screen henfører til at linjen skal vises på den screen.
# [0, 0] viser at startpunktet for linjen skal være på koordinatsættet (0,0)
# [100, 100] viser slutpunktet for linjen.
# 5 er hvor mange pixels bred linjen skal være. Her er den på 5.
9.
# Du bruger en for loop
10.
# Der vil ikke være nogen ramme om rektanglet.
# Dog vil den blive fyldt med den farve som rammen ville have haft.
11.
# [20, 20, 250, 100]  er tal der repræsenterer [x, y, width, height] for den rektangel som ellipsen skal fylde mest muligt af.
# Startkoordinaten er så på (20,20), og det betyder at rektanglets øverste venstre hjørne starter der.
# Så går den 250 pixels hen og 100 pixels nedad.
# længden af ellipsen må svare til width.
# bredden af ellipsen må svare til height.
12.
# Du skal vide hvad radianer er, da man bruger det til at bestemme hvor langt der skal tegnes på ellipsen.
13.
# font = pygame.font.SysFont('skrifttype', skriftstørrelse, True, False)
# text = font.render("Hvad du vil have teksten til at sige",True,hvilken farve teksten skal være)
# screen.blit(text, [250, 250])
# [250, 250] er hvilket koordinatsæt teksten skal starte på.
14.
# Det er ikke noget, der behøver at gentages for at få resultater på skærmen.
# Det skal bare stå en gang.
15.
# Der er 4 koordinater
# (50,100), (0,200), (200,200) og (100,50)
16.
# Det gør, at computeren kun viser på skærmen hvad den har tegnet efter at den har tegnet det.
# Det gør, at skærmen ikke flimrer.
17.
# Det gør, at hvis du trykker på luk-knappen, vil den lukke det hele som vi ønsker at den skal gøre.
# I stedet for at vi skal klikke så meget rundt.
18.
# pygame.draw.circle(Surface, color, pos, radius, width)
# Et eksempel kunne være
# pygame.draw.circle(screen, BLACK, [100, 100], 55, 1)
