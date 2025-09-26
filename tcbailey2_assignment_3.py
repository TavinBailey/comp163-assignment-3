# Step 1: Foundation Setup (Test Case 1)
# Starting stats
student_name = "Tavin Bailey"
current_gpa = 4.0
study_hours = 30
social_points = 40
stress_level = 80

# Print starting stats
print(f"Welcome, {student_name}!") # Welcome student
print(f"GPA: {current_gpa}") # Evaluated as float 1.0-4.0 scale
print(f"Student Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}\n") # Evaluated as int 0-100 scale

# Step 2: Course Planning Decision (Test Case 2)
print("Choose your course load:")
print("A) Easy (12 credits)")
print("B) Medium (15 credits)")
print("C) Hard (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    print("A) Easy (12 credits)")
elif choice == "B":
    print("B) Medium (15 credits)")
elif choice == "C":
    print("C) Hard (18 credits)")
else:
    print("Invalid choice: pick again")