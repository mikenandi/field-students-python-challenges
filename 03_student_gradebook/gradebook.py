# Step 1: Rekodi za wanafunzi
records = [
    "Alice,Math,85",
    "Bob,Math,78",
    "Alice,English,92",
    "Bob,English,81",
    "Alice,History,88",
    "Bob,History,74",
]

# Step 2: Kutengeneza gradebook
gradebook = {}

for record in records:
    name, subject, score = record.split(",")
    score = float(score)

    if name not in gradebook:
        gradebook[name] = {}

    gradebook[name][subject] = score

# Step 3: Kukokotoa average ya kila mwanafunzi
averages = {}

for student in gradebook:
    scores = gradebook[student].values()
    average = sum(scores) / len(scores)
    averages[student] = round(average, 2)

# Step 4: Kuweka wanafunzi kwenye rank
ranking = sorted(averages.items(), key=lambda x: x[1], reverse=True)

# Step 5: Kuonesha matokeo
print("\nStudent Ranking (Highest to Lowest):\n")
for i, (name, avg) in enumerate(ranking, start=1):
    print(f"{i}. {name}: {avg}")