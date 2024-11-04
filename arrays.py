courses = ["MIT", "CyberSecurity", "Data Science"]
print(courses)

print(courses[1])
print("\n")

for course in courses:
    print("The course is", course)

courses.append("Android development")
print(courses)
courses.remove("MIT")
print(courses)