import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_data(num_students, num_subjects):
    data = {'StudentID': [f'Student{i+1}' for i in range(num_students)]}

    for subject in range(1, num_subjects + 1):
        data[f'Subject_{subject}'] = np.random.randint(50, 100, size=num_students)

    return data

def save_to_csv(data, csv_file):
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print(f'Data saved to {csv_file}')

def read_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df

def plot_average_marks(data_frame):
    # Bar plot
    plt.figure(figsize=(12, 5))
    for subject in data_frame.columns[1:]:
        plt.bar(subject, data_frame[subject].mean(), label=subject)

    plt.title('Average Marks of Each Subject')
    plt.xlabel('Subjects')
    plt.ylabel('Average Marks')
    plt.legend()
    plt.show()

    # Pie plot
    plt.figure(figsize=(8, 8))
    plt.pie(data_frame.mean().values[1:], labels=data_frame.columns[1:], autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Average Marks Across Subjects')
    plt.show()

if __name__ == "__main__":
    num_students = 5
    num_subjects = 4
    csv_file = 'student_marks.csv'

    # Generate random data, save to CSV, and read from CSV
    data = generate_data(num_students, num_subjects)
    save_to_csv(data, csv_file)
    df = read_csv(csv_file)

    # Plot average marks using bar and pie plots
    plot_average_marks(df)
