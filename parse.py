#! /usr/bin/python3
## Parse vezme XML s výpisem z Monety a udělá z toho CSV soubor(s hodnotami, které využijeme) a také výstup pro Beancount

import xml.etree.ElementTree as ET
import chime
## Načteme XML
tree = ET.parse('export.xml')

## Najdeme transakce
transactions = tree.findall('.//transaction')

## zkouška, co jsme vůbec našli
print(type(transactions))
print(transactions[1].attrib)
print("---------------------------------------------------------------")

## Vypíšeme datum, amount a zprávu a naformátujeme pro beancount, jako výdaj dáme FIXME 

for transaction in transactions:
    datum = transaction.attrib["date-eff"] + " * "
    print (datum, end="")
    
    texty = transaction.findall('.//trn-message')
    for one in texty:
        popis='"' + one.text + '"'  
        print(popis)
    print ("Expenses:FIXME", end="  ")

    print(transaction.attrib["amount"][1:], " CZK")
    print ("Assets:Moneta")
    print() 

chime.success()