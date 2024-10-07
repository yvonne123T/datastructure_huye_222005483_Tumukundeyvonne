#8.	Create a 2D list representing a seating arrangement in a theater, and assign reserved seats.
# Create a 2D list representing the seating arrangement in a theater (e.g., 5 rows and 6 seats per row)
seating_arrangement = [
    ["Available", "Available", "Available", "Available", "Available", "Available"],  # Row 1
    ["Available", "Available", "Available", "Available", "Available", "Available"],  # Row 2
    ["Available", "Available", "Available", "Available", "Available", "Available"],  # Row 3
    ["Available", "Available", "Available", "Available", "Available", "Available"],  # Row 4
    ["Available", "Available", "Available", "Available", "Available", "Available"]   # Row 5
]

# Manually assign reserved seats (marking them as 'Reserved')
seating_arrangement[0][1] = "Reserved"  # Reserve seat in Row 1, Seat 2
seating_arrangement[2][3] = "Reserved"  # Reserve seat in Row 3, Seat 4
seating_arrangement[4][0] = "Reserved"  # Reserve seat in Row 5, Seat 1
seating_arrangement[1][5] = "Reserved"  # Reserve seat in Row 2, Seat 6
seating_arrangement[3][2] = "Reserved"  # Reserve seat in Row 4, Seat 3

# Print the seating arrangement
print("Theater Seating Arrangement:")
for row in seating_arrangement:
    print(row)
