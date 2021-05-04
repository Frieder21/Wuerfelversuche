import random
import sys
def Hilfe():
    print("\nDies ist die Hilfe\n    --help or -h\n\nStandart Syntax:\n    "+ str(sys.argv[0]) + " <Agumente> Wiederholungen Anzahl_Würfel Anzahl_Augen\n    In Ganzzahlen\n\n  ohne warte Prozuentzahl\n      --no-wait-procent\n\n  nur die Ausgabe der gewürfelten Zahlen\n      --no-procent\n\n  nur die Ausgabe in Prozent\n      --only-procent\n\n  Als Datei speichern\n      --file or -f <Dateiname>\n\n  Ohne Output\n      --no-output or -no")
    exit()
def Fehler():
    print("Probiere: --help oder -h")
    exit()
def Ist_Intiger_Positiv(ist_int):
    try:
        ist_int = int(ist_int)
    except:
        if ist_int in befehle:
            print("Eine Zahl zu wenig")
            exit()
        else:
            try:
                ist_int = str(ist_int)
            except:
                print(str(ist_int) + " ist keine Ganzzahl")
                exit()
            print(str(ist_int) + " ist keine Zahl")
            exit()
    if ist_int < 0:
        print(str(ist_int) + " ist kleiner als 0")
        exit()
    else:
        return int(ist_int)
def Input_Ist_Intiger_Positiv(frage):
    while True:
        try:
            int_frage = int(input(frage))
        except:
            continue
        else:
            if int_frage < 0:
                print("Die Zahl ist kleiner als 0")
                continue
            else:
                return int_frage
                break
def Write_Datei(Data_name, write_input):
    Datei = open(Data_name,"a")
    Datei.write(write_input)
    Datei.close()
befehle = ["--help", "-h", "--no-wait-procent", "--no-procent", "--only-procent","--no-output", "-no", "--file", "-f"]
no_wait_procent = False
no_procent = False
only_procent = False
no_output = False
file = False
if len(sys.argv) > 1:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        Hilfe()
    file_count = 0
    Wert = 1
    for Schleife_1 in range(len(sys.argv)-4):
        if sys.argv[Schleife_1+1] in befehle:
            if sys.argv[Schleife_1+1] == "--no-wait-procent":
                no_wait_procent = True
            if sys.argv[Schleife_1+1] == "--no-procent":
                no_procent = True
            if sys.argv[Schleife_1+1] == "--only-procent":
                only_procent = True
            if sys.argv[Schleife_1+1] == "--no-output" or sys.argv[Schleife_1+1] == "-no":
                no_output = True
            if sys.argv[Schleife_1+1] == "--file" or sys.argv[Schleife_1+1] == "-f":
                if sys.argv[Schleife_1+2] == sys.argv[0]:
                    Fehler()
                Datei_name = sys.argv[Schleife_1+2]
                Wert+=1
                file = True
            Wert += 1
        else:
            if file == True and file_count == 0:
                file_count+=1
            else:
                Fehler()

    if len(sys.argv)-3 != Wert:
        Fehler()
    zahl = Ist_Intiger_Positiv(sys.argv[Wert])
    Wert += 1
    Anzahl_Würfel = Ist_Intiger_Positiv(sys.argv[Wert])
    Wert += 1
    Anzahl_Würfel_Seiten = Ist_Intiger_Positiv(sys.argv[Wert])
else:
    zahl = Input_Ist_Intiger_Positiv("Wie oft soll gewürfelt werden?\n")
    Anzahl_Würfel = Input_Ist_Intiger_Positiv("\nMit wie vielen Würfeln\n")
    if Anzahl_Würfel == 1:
        Anzahl_Würfel_Seiten = Input_Ist_Intiger_Positiv("\nWie viele Seiten hat der Würfel\n")
    else:
        Anzahl_Würfel_Seiten = Input_Ist_Intiger_Positiv("\nWie viele Seiten hat je ein Würfel\n")
if only_procent == no_procent == True:
    print("Was soll dir nun Ausgegeben werden?")
    exit()
addierter_wert_Gewürfelt = 0
Würfel_Möglichkeiten = []
Gewürfelt = []
Gewürfelt_In_Prozent = []
JSON_Gewürfelt = "{"
JSON_Gewürfelt_In_Prozent = "{"
if no_wait_procent == False and no_output == False:
    print("\n")
Prozent = ("warte bis " + str(round(0 / zahl * 100,1)) + "% von " + str(zahl)+ "      ")
Prozent_Alt = Prozent
for Schleife_1 in range(Anzahl_Würfel, Anzahl_Würfel*Anzahl_Würfel_Seiten+1):
    Würfel_Möglichkeiten.append(Schleife_1)
    Gewürfelt.append(0)
    Gewürfelt_In_Prozent.append(0)
for a in range(zahl+1):
    if no_wait_procent == False and no_output == False:
        Prozent = ("warte bis " + str(round(a / zahl * 100,1)) + "% von " + str(zahl)+ "      ")
        if Prozent != Prozent_Alt:
            sys.stdout.write("\r" + str(Prozent))
            sys.stdout.flush()
            Prozent_Alt = Prozent
    if(zahl==a):
        for Schleife_1 in range(len(Würfel_Möglichkeiten)):
            addierter_wert_Gewürfelt+=Gewürfelt[Schleife_1]
            JSON_Gewürfelt = JSON_Gewürfelt +'"'+ str(Würfel_Möglichkeiten[Schleife_1]) +'":"'+ str(Gewürfelt[Schleife_1]) + '",'
        JSON_Gewürfelt = JSON_Gewürfelt[:-1] + '}'
        for Schleife_1 in range(len(Würfel_Möglichkeiten)):
            Gewürfelt_In_Prozent[Schleife_1] = str(round(Gewürfelt[Schleife_1] / addierter_wert_Gewürfelt *100))+"%"
            JSON_Gewürfelt_In_Prozent = JSON_Gewürfelt_In_Prozent +'"'+ str(Würfel_Möglichkeiten[Schleife_1]) +'":"'+ str(Gewürfelt_In_Prozent[Schleife_1]) + '",'
        JSON_Gewürfelt_In_Prozent = JSON_Gewürfelt_In_Prozent[:-1] + '}'
        if file == True:
            Datei = open(Datei_name,"w")
            Datei.write("")
            Datei.close()
        if no_wait_procent == False and no_output == False:
            print("\n")
        if only_procent == False:
            if no_output == False:
                print(JSON_Gewürfelt)
            if file == True:
                Write_Datei(Datei_name, JSON_Gewürfelt)
        if no_procent == False:
            if no_output == False:
                print(JSON_Gewürfelt_In_Prozent)
            if file == True:
                Write_Datei(Datei_name, JSON_Gewürfelt_In_Prozent)
    Random_Würfelwert = 0
    for Schleife_1 in range( Anzahl_Würfel):
        Random_Würfelwert += random.randint(1, Anzahl_Würfel_Seiten)
    for Schleife_1 in range(len(Würfel_Möglichkeiten)):
        if Random_Würfelwert == Würfel_Möglichkeiten[Schleife_1]:
            Gewürfelt[Schleife_1]+=1
        exit
