#! /usr/bin/python3
## Parse vezme XML s výpisem z Monety a udělá z toho CSV soubor(s hodnotami, které využijeme) a také výstup pro Beancount
from lxml import etree 
from datetime import datetime
import chime

## Načteme XML
xml_file = 'export.xml'

# Parse the XML file
tree = etree.parse(xml_file)
root = tree.getroot()
# Chceme jenom transakce
parent_element = root.find('transactions')

if parent_element is not None:
    # Iterujeme skrz transakce
    for child in parent_element.iterchildren():
        
        # DATUM
        if child.get("date-action") is not "":  # Test, zda není atribut prázdný
            raw_date = child.get('date-action')
        else:
            raw_date = "01.01.1900" # Pokud je atribut prázdný, dáme tam toto datum, podle kterého pak najdeme špatný záznam
        # Konvertujeme do ISO formátu
        input_date_obj = datetime.strptime(raw_date, "%d.%m.%Y")
        iso_date = input_date_obj.strftime("%Y-%m-%d")
        
        # AMOUNT:
        raw_amount = child.get('amount') # Je to string!
        # Ořízneme "-" pomocí slicingu a vyměníme čárku za tečku   
        amount = (raw_amount [1:].replace(",","."))
        # POPIS - ten je tam blbě, takže musíme takto
        trn_message_element = child.find('.//trnMessage[@position="2"]')
        if trn_message_element is not None:
            content = trn_message_element.text
            
        # tady to vypíšeme
        # Uložíme to do tuple, kdybych s tím chtěl ještě nějak pracovat  
        record = (iso_date, amount, content)
        
        print(record[0], " *", "\"", record[2],"\"")
        print ("Expenses:FIXME", record [1])
        print ("Assets:Moneta")


chime.success()
