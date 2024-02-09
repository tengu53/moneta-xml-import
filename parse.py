#! python3
## Parse vezme XML s výpisem z Monety a udělá z toho co nejvíc srozumitelný výstup pro Beancount
## Nekategorizuje výdaje - dává tam "FIXME", abych to pak mohl manuálně přiřadit 
from lxml import etree 
from datetime import datetime
import chime

## Načteme XML - ideální postup - v internetovém bankovnictví vyfiltrovat odchozí platby a exportovat do XML
## Tady zadat XML soubor 
xml_file = 'export.xml'

# Tady ho parsujeme
tree = etree.parse(xml_file)
root = tree.getroot()
# Chceme jenom transakce
parent_element = root.find('transactions')

if parent_element != None:
    # Iterujeme skrz transakce
    for child in parent_element.iterchildren():
        
        # DATUM
        if child.get("date-action") != "":  # Test, zda není atribut prázdný
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
        # POPIS -v xml je ukrytý do child elementu, takže musíme takto
        trn_message_element = child.find('.//trnMessage[@position="2"]')
        if trn_message_element != None:
            content = trn_message_element.text
            
        # Uložíme to do tuple, kdybych s tím chtěl pak ještě nějak pracovat  
        record = (iso_date, amount, content)
        
        # Tady to vypíšeme
        print(record[0], " *", "\"", record[2],"\"")
        print ("Expenses:FIXME", record [1], "CZK")
        print ("Assets:Moneta")
        print()

chime.success()
