student ={}
student["name"] = input("Enter name :")
student["age"] = int(input("Enter age :"))
student["city"] = input("Enter city name :")
print("\nStudent profile")
print("---------------")
for key in student :
    print(key,":",student[key])