#! /usr/bin/python3
## Parse vezme XML s výpisem z Monety a udělá z toho CSV soubor(s hodnotami, které využijeme) a také výstup pro Beancount
from lxml import etree 
import chime
## Načteme XML
# Sample XML file with namespaces
xml_file = 'export.xml'

# Parse the XML file
tree = etree.parse(xml_file)
root = tree.getroot()
# Chceme jenom transakce
parent_element = root.find('transactions')

if parent_element is not None:
    # Iterujeme skrz transakce
    for child in parent_element.iterchildren():
        # Chceme datum
        attribute_value = child.get('date-action')
        # Chceme amount
        attribute_value2 = child.get('amount')
        # Chceme popis transakce - ten je tam blbě, takže musíme takto
        trn_message_element = child.find('.//trnMessage[@position="2"]')
        if trn_message_element is not None:
            content = trn_message_element.text
            
        # tady to vypíšeme
            # TODO Převést datum na ISO, čárku na tečku
            # TODO Naformátovat do Formátu Beancountu        
        if attribute_value is not None:
            print(f"Datum: {attribute_value}, Amount: {attribute_value2}, Popis: {content}")

chime.success()
