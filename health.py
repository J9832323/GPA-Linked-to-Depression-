
import pandas as pd

df = pd.read_csv('Student Mental health.csv')
print(df.head())

df.columns = df.columns.str.strip().str.lower().str.replace('[/\?\*\"!]', '', regex=True).str.replace(' ', '_')
print(df.columns.tolist())

#Gender and ages 
print(df['choose_your_gender'].value_counts())
print(df['age'].value_counts())

#year of study and course and gpa  
print(df['your_current_year_of_study'].value_counts())
print(df['what_is_your_course'].value_counts())
print(df['what_is_your_cgpa'].value_counts())

database = 'health.db'
import sqlite3
conn = sqlite3.connect(database)
cursor = conn.cursor()

#To help with elimanting labels with diffrent capilazation 
df['your_current_year_of_study'] = df['your_current_year_of_study'].str.strip().str.title()

df.to_sql('student_health', conn, if_exists='replace', index=False)


# Query one and two look at depression averages of kids by current year and gpa 
#Query 1 looks at kids with gpas equal or higher than 3.0 by year , when trying to find avg depression. Then also comparing genders
query = """
SELECT your_current_year_of_study,choose_your_gender, AVG(CASE WHEN do_you_have_depression = 'Yes' THEN 1 ELSE 0 END) AS avg_depression_rate
FROM student_health
WHERE what_is_your_cgpa >= 3
GROUP BY your_current_year_of_study, choose_your_gender
ORDER BY your_current_year_of_study, choose_your_gender;
"""

cursor.execute(query)
results = cursor.fetchall()
print('query 1 ')
for i in results:
    print(i)

df_heat = pd.read_sql_query(query, conn)

# Bar chart version
import matplotlib.pyplot as plt
import seaborn as sns 
plt.figure(figsize=(8, 5))
sns.barplot(data=df_heat,
            x= 'your_current_year_of_study',
            y='avg_depression_rate',
            hue='choose_your_gender',
            palette='Set2')
plt.title('Depression Rate by Year of Study (GPA >= 3) and gender')
plt.xlabel('Year of Study')
plt.ylabel('Average Depression Rate')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()




# Query 2 Looks at kids with gpa euqal or less than 3.0 by year , when trying to find avg depression. Also comparing genders
query2 = """
SELECT your_current_year_of_study,choose_your_gender, AVG(CASE WHEN do_you_have_depression = 'Yes' THEN 1 ELSE 0 END) AS avg_depression_rate
FROM student_health
WHERE what_is_your_cgpa <= 3
GROUP BY your_current_year_of_study, choose_your_gender
ORDER BY your_current_year_of_study, choose_your_gender;
"""

cursor.execute(query2)
results2 = cursor.fetchall()
print('query 2 ')
for i in results2:
    print(i)

df_heat2 = pd.read_sql_query(query2,conn)

plt.figure(figsize=(8, 5))
sns.barplot(data=df_heat2,
            x= 'your_current_year_of_study',
            y='avg_depression_rate',
            hue='choose_your_gender',
            palette='Set2')
plt.title('Depression Rate by Year of Study (GPA <= 3)')
plt.xlabel('Year of Study')
plt.ylabel('Average Depression Rate')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

# query 3 and 4 comapring percent of kids with anxity based on gpa and current year
#query 3 does kids with gpa equal or higher to 3.0. Also comparing genders
query3 = """
SELECT your_current_year_of_study, choose_your_gender, AVG (CASE WHEN do_you_have_anxiety = 'Yes' THEN 1 ELSE 0 END) AS avg_anxiety
FROM student_health
WHERE what_is_your_cgpa >= 3
GROUP BY your_current_year_of_study, choose_your_gender
ORDER BY your_current_year_of_study, choose_your_gender;
"""
cursor.execute(query3)
result3 = cursor.fetchall()
print('Query 3')
for i in result3:
    print(i)

df_heat3 = pd.read_sql_query(query3,conn)


plt.figure(figsize=(8, 5))
sns.barplot(data=df_heat3,
            x= 'your_current_year_of_study',
            y='avg_anxiety',
            hue='choose_your_gender',
            palette='Set2')
plt.title('Anxiety Rate by Year of Study (GPA >= 3)')
plt.xlabel('Year of Study')
plt.ylabel('Anxiety Rate')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

#Query 4 Looks at kids with gpa less than or equal to 3.0 . Then comapres gender 

query4 = """
SELECT your_current_year_of_study, choose_your_gender, AVG (CASE WHEN do_you_have_anxiety = 'Yes' THEN 1 ELSE 0 END) AS avg_anxiety
FROM student_health
WHERE what_is_your_cgpa <= 3
GROUP BY your_current_year_of_study, choose_your_gender
ORDER BY your_current_year_of_study, choose_your_gender;
"""

cursor.execute(query4)
result4 = cursor.fetchall()
print('Query 4')
for i in result4:
    print(i)

df_heat4 = pd.read_sql_query(query4,conn)


plt.figure(figsize=(8, 5))
sns.barplot(data=df_heat4,
            x= 'your_current_year_of_study',
            y='avg_anxiety',
            hue='choose_your_gender',
            palette='Set2')
plt.title('Anxiety Rate by Year of Study (GPA <= 3)')
plt.xlabel('Year of Study')
plt.ylabel('Anxiety Rate')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()


# Painc attack by year and gpa 3.0 or above. Also sepreated by gender

query5 = """
SELECT your_current_year_of_study,choose_your_gender, AVG(CASE WHEN do_you_have_panic_attack = 'Yes' THEN 1 ELSE 0 END) AS panic_avg
FROM student_health
WHERE what_is_your_cgpa >= 3 
GROUP BY your_current_year_of_study, choose_your_gender
ORDER BY your_current_year_of_study, choose_your_gender;
"""

cursor.execute(query5)
result5 = cursor.fetchall()
print('Query5')
for i in result5:
    print(i)
df_heat5 = pd.read_sql_query(query5,conn)


plt.figure(figsize=(8, 5))
sns.barplot(data=df_heat5,
            x= 'your_current_year_of_study',
            y='panic_avg',
            hue='choose_your_gender',
            palette='Set2')
plt.title('percent of students with painc attacks with(GPA >= 3.0)')
plt.xlabel('Year of Study')
plt.ylabel('Panic attack Rate')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()


#Query6 looking at painc attacks of year level based on gps euqal to 3.0 or less. Sepreated by genders 

query6 = """
SELECT your_current_year_of_study, choose_your_gender, AVG(CASE WHEN do_you_have_panic_attack = 'Yes' THEN 1 ELSE 0 END) AS panic_avg
FROM student_health
WHERE what_is_your_cgpa <= 3 
GROUP BY your_current_year_of_study, choose_your_gender
ORDER BY your_current_year_of_study, choose_your_gender;
"""
cursor.execute(query6)
result6 = cursor.fetchall()
print('Query6')
for i in result6:
    print(i)
df_heat6 = pd.read_sql_query(query6,conn)

plt.figure(figsize=(8, 5))
sns.barplot(data=df_heat6,
            x= 'your_current_year_of_study',
            y='panic_avg',
            hue='choose_your_gender',
            palette='Set2')
plt.title('percent of students with painc attacks with(GPA <= 3.0)')
plt.xlabel('Year of Study')
plt.ylabel('Panic attack Rate')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

#Summary 

# Depression Rates
# - GPA >= 3.0: Highest in Year 3 females (50%) and Year 2 males (40%)
# - GPA <= 3.0: Highest in Year 1 females (66%), no reported depression among males

# Anxiety Rates
# - GPA >= 3.0: High in Year 1-3 students; peaks at Year 2 males (50%) and Year 3 females (~39%)
# - GPA <= 3.0: Only Year 1 females report anxiety (33.3%), rest are 0%

# Panic Attacks
# - GPA >= 3.0: Highest in Year 3 females (44%) and Year 1 males (50%)
# - GPA <= 3.0: Year 2 males (100%), Year 1 females (66%), Year 3 females (50%)

#Key Takeaways:
# - Mental health issues are more common in early and middle years (Year 1–3)
# - Female students report higher depression and panic rates across both GPA ranges
# - Students with GPA ≥ 3.0 still experience significant anxiety and panic symptoms
# - Some data and lack of data could cause some these percents to not be as accruate. As alot the data for students less than 3.00 or equal
# seems to be missing from the data. A bigger dataset would help give more accurate insight


