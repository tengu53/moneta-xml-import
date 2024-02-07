# Input number in the format -400,00
input_number_str = "-400,00"

# Replace comma with dot, remove the leading '-' and convert to float
output_number = float(input_number_str.replace(',', '').replace('-', ''))

print("Input number:", input_number_str)
print("Output number:", '{:.2f}'.format(output_number))