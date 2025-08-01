### 🐍 Python Challenge: “Student Gradebook”

#### **Problem Statement**

You are given a list of student records. Each record is a string in the format:

```
"Name,Subject,Score"
```

Example:

```python
records = [
    "Alice,Math,85",
    "Bob,Math,78",
    "Alice,English,92",
    "Bob,English,81",
    "Alice,History,88",
    "Bob,History,74"
]
```

Your task is to:

1. **Parse the records** into a structured format.
2. **Create a gradebook** where each student's name maps to their subjects and scores.
   Example expected structure:

   ```python
   {
       "Alice": {"Math": 85, "English": 92, "History": 88},
       "Bob": {"Math": 78, "English": 81, "History": 74}
   }
   ```

3. **Calculate the average score** for each student and return a dictionary of averages.
   Example:

   ```python
   {
       "Alice": 88.33,
       "Bob": 77.67
   }
   ```

4. **Print the student(s) with the highest average.**

---

### ✅ Requirements

- Use functions where necessary.
- Handle invalid records gracefully (e.g., missing score or incorrect format).
- Round average scores to **2 decimal places**.

---

### ✨ Bonus Task

Add a function that ranks students from highest to lowest based on their average score and prints the ranking.

---

### 📌 Sample Output

```
Gradebook:
{'Alice': {'Math': 85, 'English': 92, 'History': 88}, 'Bob': {'Math': 78, 'English': 81, 'History': 74}}

Averages:
{'Alice': 88.33, 'Bob': 77.67}

Top Student(s): Alice with average 88.33

Ranking:
1. Alice - 88.33
2. Bob - 77.67
```
