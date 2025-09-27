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
print("C) Hard (18 credits)\n")

choice = input("Your choice: ")

if choice == "A":
    print("A) Easy (12 credits)\n")
elif choice == "B":
    print("B) Medium (15 credits)\n")
elif choice == "C":
    print("C) Hard (18 credits)\n")
else:
    print("Invalid choice: pick again\n")

# Step 3: Study Strategy Decision (Test Case 3)
study_options = ["Programming", "Math", "English", "History"]

print("Study Options:")
print("A) Programming")
print("B) Math")
print("C) English")
print("D) History\n")

study_choice = input("Which will you prioritize? ")

# Map letter choice to actual subject
if study_choice == "A":
    study_choice = "Programming"
elif study_choice == "B":
    study_choice = "Math"
elif study_choice == "C":
    study_choice = "English"
elif study_choice == "D":
    study_choice = "History"

# Use 'not in' for invalid input
if study_choice not in study_options:
    print("That's not an available study option. No changes made.")
else:
    print("You chose:", study_choice)
    # Logical operators affecting GPA and social points
    if study_choice == "Programming" and current_gpa < 3.0:
        current_gpa += 0.2  # hard work pays off
        social_points -= 5  # less free time
        print("Programming improved your GPA, but you missed some social time.")
    elif study_choice == "Math" or study_choice == "English":
        current_gpa += 0.1
        social_points -= 5
        print("Math/English improved your GPA, but you missed some social time.")
    elif not (study_choice == "History"):
        current_gpa += 0.05
        print("Not History - your choice balanced your academics.")
    else:  # History path
        social_points += 10
        print("History boosted your social connections!")