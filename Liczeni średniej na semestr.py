print("Hej, podaj ilość danych ocen a otrzymasz średnią na koniec semestru")
Bdb=float(input("Podaj ilośc ocen Bardzo dobrych: "))
Db=float(input("Podaj ilośc ocen  Dobrych: "))
Dst=float(input("Podaj ilośc ocen Bardzo dostatecznych: "))
Dop=float(input("Podaj ilośc ocen Dopuszczających: "))
Ndst=float(input("Podaj ilośc ocen Niedostatecznych: "))
bdbx=Bdb*5
dbx=Db*4
dstx=Dst*3
dopx=Dop*2
ndstx=Ndst*2
Średnia=(bdbx+dbx+dstx+dopx+ndstx)/(Bdb+Db+Dst+Dop+Ndst)       
print(" Twoja średnia: ",Średnia)
if  Średnia >= 4.75:
    print("Gratulacje masz świadectwo z paskiem")
elif Średnia >= 4.5:
    print("Całkiem nieźle")
elif Średnia >= 4.0:
    print("Nie ma tragedii ale mogło by być lepiej")
else: print("Bierz się do pracy! Twoje oceny są nie najlepsze.") 
