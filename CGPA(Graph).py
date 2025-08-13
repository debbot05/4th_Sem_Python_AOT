import matplotlib.pyplot as plt
import numpy as np

def generate_data():
    # Generate random CGPA data for 10 sections
    np.random.seed(42)  # Set seed for reproducibility
    section_names = [f'Section {i+1}' for i in range(10)]
    cgpa_data = np.random.uniform(7.0, 9.0, size=10)  # Generating random CGPA values

    return section_names, cgpa_data

def plot_average_cgpa(section_names, cgpa_data):
    # Calculate the average CGPA
    average_cgpa = np.mean(cgpa_data)

    # Create a bar graph
    plt.bar(section_names, cgpa_data, color='skyblue')

    # Add labels and title
    plt.xlabel('Sections')
    plt.ylabel('Average CGPA')
    plt.title('Average CGPA of 10 Sections')

    # Display the average CGPA as a horizontal line
    plt.axhline(y=average_cgpa, color='red', linestyle='--', label=f'Average CGPA: {average_cgpa:.2f}')
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Generate random CGPA data for 10 sections
    section_names, cgpa_data = generate_data()

    # Plot the average CGPA
    plot_average_cgpa(section_names, cgpa_data)
