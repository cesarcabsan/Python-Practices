import pandas as pd

# one key join
students = pd.DataFrame({
    'student_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'major': ['Physics', 'History', 'Computer Science', 'Biology'],
})


enrollments = pd.DataFrame({
    'student_id': [101, 102, 103, 104],
    'course': ['Calculus', 'World History', 'Operating Systems', 'Genetics'],
    'semester': ['Fall', 'Spring', 'Fall', 'Spring']
})


merge_data = pd.merge(students, enrollments, on='student_id')
print("Merged dataframe with one matching key:\n", merge_data)


# multiple matching keys
course_data1 = pd.DataFrame({
        "dept_code": ["CS", "OS", "MATH", "PHYS"],
        "course_level": ["lvl100", "lvl200", "lvl100", "lvl200"],
        "course_name": ["Intro to CS", "Data Structures", "Calculus I", "Mechanics"],
        "instructor": ["Smith", "Lee", "Patel", "Gomez"],
})

course_data2 = pd.DataFrame({
        "dept_code": ["CS", "OS", "MATH", "PHYS"],
        "course_level": ["lvl100", "lvl100", "lvl100", "lvl100"],
        "room": ["A101", "B202", "B203", "C303"],
        "time_slot": ["9AM", "10AM", "11AM", "12PM"],
})

### Merging the keys + how argument
# Inner join (Default)
merger = pd.merge(course_data1, course_data2, on=["dept_code", "course_level"], how='inner') 
print("\nMerged dataframe with multiple matching keys:\n--- INNER MERGE ---\n", merger) # The inner join uses an intersection of keys from both frames. The output only shows the matching columns
 

# other joining methods (outer, left and right)
for method in ['outer', 'left', 'right']:
    print(f"\n--- {method.upper()} MERGE ---")
    merged = course_data1.merge(course_data2, on=["dept_code", "course_level"], how=method)
    print(merged)

# The outer join uses the union of keys to combine all rows from both DataFrames.  
# The left join returns all rows from the left DataFrame and the matching rows from the right DataFrame.  
# The right join returns all rows from the right DataFrame and the matching rows from the left DataFrame. 
 
# Any unmatching values will be filled with NaN