import numpy
from scipy import stats

##Mittelwert, Median, Modus
#Aufgabe 1
zahlen = [8, 2, 5, 1, 10]
def berechene_mittelWert(liste):
    mittelWert = numpy.mean(liste)
    return mittelWert

berechene_mittelWert(zahlen)

#Aufgabe 2
zahlen1 = [7, 5, 3, 5]
zahlen2 = [1, 2, 3, 4, 5]
def berechne_median(liste):
    median = numpy.median(liste)
    return(median)

berechne_median(zahlen1)
berechne_median(zahlen2)

#Aufgabe 3
zahlen = [4, 1, 2, 2, 3, 1]
def berechne_modus(liste):
    modus = stats.mode(liste)
    return(modus)

berechne_modus(zahlen)

#Aufgabe 4
zahlen = [1, 2, 3, 4, 4, 5, 5, 5]
def kombinierte_statistik(liste):
    mittelWert = numpy.mean(liste)
    median = numpy.median(liste)
    modus = stats.mode(liste)
    tuple = (mittelWert, median, modus)
    return tuple

kombinierte_statistik(zahlen)

#Aufgabe 5
#zahlen = [10, 20, 30, 40, 50, 60, 70]
#def filter_und_statistik(liste:list, minWert, maxWert):
#    for i in liste:
#        if i < minWert:
#            liste = liste.remove(i)
#        elif i > maxWert:
#            liste = liste.remove(i)
#    mittelWert = numpy.mean(liste)
#    median = numpy.median(liste)
#    modus = stats.mode(liste)
#    tuple = (mittelWert, median, modus)
#    return tuple

#filter_und_statistik(zahlen, 20, 60)



##Standardabweichung
#Aufgabe 1
zahlen = [4, 8, 6, 5, 3, 2]
def berechne_varianz(liste):
    mittelWert = numpy.mean(liste)
    differenz = [(i-mittelWert) **2 for i in liste]
    varianz = numpy.mean(differenz)
    return varianz
       
berechne_varianz(zahlen)

#Aufgabe 2
zahlen = [9, 2, 5, 4, 12, 7, 8, 11]
def berechene_standardabweichung(liste):
    standardabweichung = numpy.sqrt(berechne_varianz(liste))
    return(standardabweichung)

berechene_standardabweichung(zahlen)



##Berechnung von Perzentile
schulstrecke = [5, 1, 25, 12, 7, 8,]
def percentile(liste):
     percentile = numpy.percentile(liste, 75)
     print(percentile)

percentile(schulstrecke)