# Step 1: Create the gradebook from raw data
def create_gradebook(data_list):
    gradebook = {}

    for entry in data_list:
        parts = entry.strip().split(',')

        # Validate format
        if len(parts) != 3:
            print(f" Invalid format, skipped: {entry}")
            continue

        name, subject, score_text = parts

        # Validate score
        try:
            score = int(score_text)
        except ValueError:
            print(f" Invalid score, skipped: {entry}")
            continue

        # Add student and subject
        if name not in gradebook:
            gradebook[name] = {}

        gradebook[name][subject] = score

    return gradebook

# Step 2: Compute average scores for each student
def compute_averages(gradebook):
    averages = {}

    for student, subjects in gradebook.items():
        scores = list(subjects.values())
        if scores:  # Avoid division by zero
            average = round(sum(scores) / len(scores), 2)
            averages[student] = average
        else:
            averages[student] = 0.0

    return averages

# Step 3: Identify top-performing student(s)
def get_top_students(averages):
    if not averages:
        return [], 0.0

    highest_score = max(averages.values())
    top_names = [name for name, score in averages.items() if score == highest_score]
    return top_names, highest_score

# Step 4: Display ranking from highest to lowest average
def display_ranking(averages):
    if not averages:
        print("No student averages to rank.")
        return

    sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    print("\n Student Ranking:")
    for position, (name, score) in enumerate(sorted_students, start=1):
        print(f"{position}. {name} - Average Score: {score}")

# Sample student data
student_data = [
    "Alice,Math,85",
    "Bob,Math,78",
    "Alice,English,92",
    "Bob,English,81",
    "Alice,History,88",
    "Bob,History,74"
]

# Run the program
gradebook = create_gradebook(student_data)
print("\n Gradebook:")
for student, subjects in gradebook.items():
    print(f"{student}: {subjects}")

averages = compute_averages(gradebook)
print("\n Averages:")
for student, avg in averages.items():
    print(f"{student}: {avg}")

top_students, top_average = get_top_students(averages)
print(f"\n Top Student(s): {', '.join(top_students)} with average score of {top_average}")

display_ranking(averages)