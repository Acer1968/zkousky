"""
Vytvoří soubor všech 90 kostek pro souboj ve hře Gangzzz, který je možné podsunout do Photoshopu funkci Grafika řízená daty.

Jako vstup bere soubor šestic s čísly 1-6, ve kterém platí, že podle pozice v šestici je určen typ souboje, který bude zobrazen ikonou:
Pozice 1 nebo 2: útok silou (obrázek gym.psd)
Pozice 3 nebo 4: útok zbraní (obrázek arm.psd)
Pozice 5 nebo 6: útok informacemi (obrázek lib.psd)

Podle pozice v šestici je vybrán příslušný obrázek a ten je vložen na příslušnou pozici v šabloně kostky D6 pro TTS. Protože pozice hodnot 1-6 je na kostce pevně daná, je třeba obrázky útoku přesunout na správnou pozici ve výstupním souboru, protože ve vstupním souboru jsou řazeny podle typu útoku a nikoli podle hodnoty.

Příklad:
Vstup:
2,4,3,5,1,6
3,6,1,4,2,5
Výstup:
lib.psd, gym.psd, arm.psd, gym.psd, arm.psd, lib.psd
arm.psd, lib.psd, gym.psd, arm.psd, lib.psd, gym.psd
"""

import random as rnd
import itertools as it
import os


DEBUG = False

IMGFILEPREFIX = r"D:\PetrVavrinec\Dokumenty\zabava\Hry moje\Gangzzz\2021\symboly-budov-4-kvadrant"
DATAFILEPREFIX = r"D:\PetrVavrinec\PythonProjects\zkousky\gangzzz"
INPUTDATAFILE = "gangzzz-dices-first-result.txt"
OUTPUTDATAFILE = "gangzzz-dices-final-result.txt"

SYMBOLS = "gym-red.psd gym-red.psd arm.psd arm.psd lib.psd lib.psd".split()

"""
def reduce_symetric(combs):
    result_combs = []
    for comb in combs:
        if comb in result_combs or tuple(reversed(comb)) in result_combs:
            continue
        else:
            result_combs.append(comb)
    return result_combs
"""

def combs_to_txt(datafile, combs):
    with open(datafile, 'w') as f:
        f.write("name, position1, position2, position3, position4, position5, position6\n")
        counter = 0
        for comb in combs:
            temp_dice = [1,2,3,4,5,6]
            counter += 1
            f.write(f"Dice_{str(counter).zfill(2)},")
            for iner_index, index in enumerate(comb):
                if index == 1 or index == 6:
                    temp_dice[index - 1] = SYMBOLS[iner_index][:-4]+"-180.psd"
                else:
                    temp_dice[index - 1] = SYMBOLS[iner_index]
            for iner_index, item in enumerate(temp_dice):
                f.write(f"{os.path.join(IMGFILEPREFIX, item)}")
                if iner_index < 5:
                    f.write(",")
                else:
                    f.write("\n")
            print(f"Vstupní šestice:\n{comb}")
            print(f"Výstup:\n{temp_dice}")


def combine_two_combs(colors, runestones):
    complete_combs = []
    counter = 0
    for color in colors:
        randomized = rnd.random() < 0.5
        if randomized:
            color = tuple(reversed(color))
        for runestone in runestones:
            counter += 1
            randomized = rnd.random() < 0.5
            if randomized:
                runestone = tuple(reversed(runestone))
            new_list = []
            for index in range(5):
                filename = FILEPREFIX + f"runestone-{list(runestone)[index]}-circle-{list(color)[index]}-200dpi.png"
                new_list.append(filename)
            complete_combs.append(new_list)
            if DEBUG:
                print(f"{counter:4}  {complete_combs[-1]}")
    return complete_combs

def load_full_list(datafile):
    tmp = []
    with open(datafile) as f:
        for line in f.read().splitlines():
            tmp.append([int(i) for i in line.split(',')])
    return tmp

if __name__ == "__main__":
    test_combs = [
        [2,4,3,5,1,6],
        [3,6,1,4,2,5],
    ]

    inputdatafile = os.path.join(DATAFILEPREFIX, INPUTDATAFILE)
    datafile = os.path.join(DATAFILEPREFIX, OUTPUTDATAFILE)

    test_combs = load_full_list(inputdatafile)
    combs_to_txt(datafile, test_combs)


"""
3600  ['D:\\PetrVavrinec\\Dokumenty\\zabava\\Hry moje\\Rozcvicka\\runova-varianta-2022\\TTS\\ExportPNG_100ppi\\runestones\\runestone-othala-circle-color5-200dpi.png', 'D:\\PetrVavrinec\\Dokumenty\\zabava\\Hry moje\\Rozcvicka\\runova-varianta-2022\\TTS\\ExportPNG_100ppi\\runestones\\runestone-jera-circle-color1-200dpi.png', 'D:\\PetrVavrinec\\Dokumenty\\zabava\\Hry moje\\Rozcvicka\\runova-varianta-2022\\TTS\\ExportPNG_100ppi\\runestones\\runestone-dagaz-circle-color2-200dpi.png', 'D:\\PetrVavrinec\\Dokumenty\\zabava\\Hry moje\\Rozcvicka\\runova-varianta-2022\\TTS\\ExportPNG_100ppi\\runestones\\runestone-teiwaz-circle-color3-200dpi.png', 'D:\\PetrVavrinec\\Dokumenty\\zabava\\Hry moje\\Rozcvicka\\runova-varianta-2022\\TTS\\ExportPNG_100ppi\\runestones\\runestone-raido-circle-color4-200dpi.png']
"""


