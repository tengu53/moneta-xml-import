from datetime import datetime

# Input date in the format dd-mm-yyyy
input_date_str = "07-02-2024"

# Convert the input date to a datetime object
input_date_obj = datetime.strptime(input_date_str, "%d-%m-%Y")

# Convert the datetime object to ISO format (yyyy-mm-dd)
iso_date_str = input_date_obj.strftime("%Y-%m-%d")

print("Input date:", input_date_str)
print("ISO format:", iso_date_str)
