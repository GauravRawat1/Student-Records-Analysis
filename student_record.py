import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('student_record.csv')

# Display the first few rows of the data
print("------STUDENT RECORDS------")
print("\n")
print("First Five Records")
print(data.head())
print("\n")
print("Shape of Records")
print(data.shape)
print("\n")
print("Data Type of Records")
print(data.dtypes)
print("\n")
print("Basic Statistic")
print(data.describe())
print("\n")

# Check for missing values
print("Finding Missing Values(If Present)")
print(data.isnull().sum())
data = data.dropna()  # Drop rows with missing values
print("\n")

#Check for duplicates
print("Finding and Droping Duplicate values")
print(data.duplicated().sum())
data = data.drop_duplicates()  # Drop duplicate rows
print("\n\n")

#Feature engineering: Create a new feature for total score
data['Total'] = data['Maths'] + data['English'] + data['Science'] + data['Computer']
data['percentage'] = data['Total'] / 400 * 100
data['Rank'] = data['percentage'].rank(ascending=False)

def performance_category(percentage):
    if percentage >= 90:
        return 'Excellent'
    elif percentage >= 75:
        return 'Good'
    elif percentage >= 60:
        return 'Average'
    else:
        return 'Poor'
data['Performance'] = data['percentage'].apply(performance_category)

# Exploratory Data Analysis
print("Student with the highest percentage")
print(data.loc[data['percentage'].idxmax()])  # Student with the highest percentage
print("\n")

print("Student with the lowest percentage")
print(data.loc[data['percentage'].idxmin()])  # Student with the lowest percentage
print("\n")

print("Average score in each subject")
print(data[['Maths','Science','English','Computer']].mean())  # Average score in each subject
print("\n")

print("Subject with the highest average score")
print(data[['Maths', 'Science','English','Computer']].mean().idxmax())  # Subject with the highest average score
print("\n")

print("Subject with the lowest average score")
print(data[['Maths','Science','English','Computer']].mean().idxmin())  # Subject with the lowest average score
print("\n")

print("Garde distribution")
print(data['Grade'].value_counts()) # Garde distribution
print("\n")


# Visualizations
# Student Total marks
plt.figure(figsize=(12,6))
plt.bar(
    data['Name'],
    data['Total']
)
plt.title(
    "Student Total Marks"
)
plt.xticks(rotation=90)

plt.show()

# subject Averages
subject_avg = (
data[['Maths',
    'Science',
    'English',
    'Computer']]
.mean()
)
plt.bar(
    subject_avg.index,
    subject_avg.values
)

plt.show()

#Grade Distribution
grade = data['Grade'].value_counts()
plt.pie(
    grade,
    labels=grade.index,
    autopct='%1.1f%%'
)

plt.show()

# Attendence Distribution
plt.hist(
    data['Attendance'],
    bins=10
)

plt.show()
