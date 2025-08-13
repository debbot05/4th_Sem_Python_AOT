import matplotlib.pyplot as plt
import numpy as np

def display_marks_graph(marks):
    subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5']

    # Bar graph
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.bar(subjects, marks, color='skyblue')
    plt.title('Student Marks - Bar Graph')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')

    # Line plot
    plt.subplot(1, 2, 2)
    plt.plot(subjects, marks, marker='o', color='green', linestyle='-', linewidth=2)
    plt.title('Student Marks - Line Plot')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Input marks for a student
    marks = [85, 92, 78, 88, 90]

    # Display the marks graphically
    display_marks_graph(marks)
