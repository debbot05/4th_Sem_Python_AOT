import matplotlib.pyplot as plt
import numpy as np

def display_electricity_consumption(months, consumption):
    # Line plot
    plt.figure(figsize=(10, 5))
    plt.plot(months, consumption, marker='o', color='blue', linestyle='-', linewidth=2)
    plt.title('Electricity Consumption Over 12 Months')
    plt.xlabel('Months')
    plt.ylabel('Electricity Consumption (kWh)')
    plt.grid(True)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Sample data for electricity consumption over 12 months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    consumption = np.random.randint(200, 500, size=12)  # Random data, replace with actual consumption values

    # Display the electricity consumption graphically
    display_electricity_consumption(months, consumption)
