# Read student details
name = input("Enter the student's name: ")
usn = input("Enter the USN: ")
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
total_marks = m1 + m2 + m3
average_marks = total_marks / 3
print("\n--- Student Details ---")
print(f"Name         : {name}")
print(f"USN          : {usn}")
print(f"Subject 1    : {m1}")
print(f"Subject 2    : {m2}")
print(f"Subject 3    : {m3}")
print(f"Total Marks  : {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
