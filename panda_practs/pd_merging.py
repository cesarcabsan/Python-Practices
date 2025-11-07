import pandas as pd

#one key join
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


# multiple keys
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

# merging the keys + how argument
inner_merge = pd.merge(course_data1, course_data2, on=["dept_code", "course_level"], how='inner') 
print("\nMerged dataframe with multiple matching keys")
print("Inner join (default):\n", inner_merge)

# If a key combination does not appear in either the left or right tables, the values in the joined table will be labeled NA
# Outer join
outer_merge = pd.merge(course_data1, course_data2, on=["dept_code", "course_level"], how='outer')
print("\nOuter join:\n", outer_merge)

# Left join
left_merge = pd.merge(course_data1, course_data2, on=["dept_code", "course_level"], how='left')
print("\nLeft join:\n", left_merge)

# Right join
right_merge = pd.merge(course_data1, course_data2, on=["dept_code", "course_level"], how='right')
print("\nRight join:\n", right_merge)