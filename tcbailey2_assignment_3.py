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

# Step 4: Final Semester Assessment
print("\nFinal Semester Assessment")
final_choice = input("Type 'finish' to evaluate your semester: ")

# Identity operator for type checking
if type(final_choice) is str:

    # Nested if statements (minimum 2 levels) for multiple endings
    if final_choice != "":  # Using 'is not' to ensure user typed something
        if current_gpa >= 3.5:
            if stress_level < 50:
                print("\nEnding 1: Academic Champion!")
                print("Your GPA is excellent and stress is manageable. You graduate with honors!")
            else:
                print("\nEnding 2: Overachiever Burnout")
                print("GPA is high but stress took a toll. Time to relax this summer!")
        elif current_gpa >= 2.0:
            if social_points > 60:
                print("\nEnding 3: Well-Rounded Success")
                print("Your GPA is decent and your social life thrived. Balance achieved!")
            else:
                print("\nEnding 4: Mediocre Semester")
                print("You passed, but could improve academics or social life next time.")
        else:
            print("\nEnding 5: Semester Struggles")
            print("GPA too low. Need to rethink your strategies and study habits.")
    else:
        print("You did not enter a choice. Cannot evaluate semester.")  # is not used above
else:
    print("Unexpected input type. Cannot evaluate semester.")

# Display final stats
print("\nFinal Statistics:")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")