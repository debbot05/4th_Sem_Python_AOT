import matplotlib.pyplot as plt

def plot_election_results(total_seats, seats_X, seats_Y, seats_Z):
    parties = ['X', 'Y', 'Z']
    seats = [seats_X, seats_Y, seats_Z]

    plt.bar(parties, seats, color=['blue', 'green', 'red'])

    plt.xlabel('Parties')
    plt.ylabel('Number of Seats')
    plt.title('West Bengal Election Results')

    plt.text(-0.1, total_seats + 1, f'Total Seats: {total_seats}', fontweight='bold')

    for i in range(len(parties)):
    plt.text(i, seats[i] + 1, str(seats[i]), ha='center', va='bottom', fontweight='bold')

    plt.show()

if __name__ == "__main__":
    total_seats = int(input("Enter the total number of seats: "))
    seats_X = int(input("Enter the number of seats won by party X: "))
    seats_Y = int(input("Enter the number of seats won by party Y: "))
    seats_Z = int(input("Enter the number of seats won by party Z: "))

    plot_election_results(total_seats, seats_X, seats_Y, seats_Z)
