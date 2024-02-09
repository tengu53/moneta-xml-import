Skript, který převede XML s výpisem bankovních trasakcí z Moneta banky, do formátu pro Beancount. Nic moc chytrého, jen takový základ.

## Doporučený postup
1. _pip install lxml_
2. V internetovém bankovnictví vyfiltrovat odchozí platby a exportovat XML
3. Ve srcriptu zadat název XML souboru
4. Spustit to - ideálně takto ./parse.py >> data.txt
5. Z TXT souboru pak nakopírovat data do .beancount soboru
6. Doplnit kategorie plateb (tam, kde jen "FIXME")   
