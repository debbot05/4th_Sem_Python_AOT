file_path = 'your_file.txt'

def extract_consumption(file_path):
    july_consumption = november_consumption = 0

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                customer_id, month, consumption = parts
                if month.lower() == 'july':
                    july_consumption += int(consumption)
                elif month.lower() == 'november':
                    november_consumption += int(consumption)

    return july_consumption, november_consumption

july, november = extract_consumption(file_path)

print(f"Electricity consumption for July: {july} units")
print(f"Electricity consumption for November: {november} units")