print("Practical 5 (C) performed by rahul  rathod")

library_books = ["Data Science", "Soft Computing", "Research", "Blockchain"]

requested_book = "Soft Computing"

print("\n=== Membership Operators ===")

if requested_book in library_books:
    print(f"{requested_book} is available in the library.")
else:
    print(f"{requested_book} is NOT available in the library.")

if "Image Processing" not in library_books:
    print("Image Processing is not in the library database.")

print("\n=== Identity Operators ===")

student1 = {"name": "Chayan Bhattacharjee", "id": 101}
student2 = {"name": "Sayali Parab", "id": 101}
student3 = student1

print("student1 is student2:", student1 is student2)    
print("student1 is student3:", student1 is student3)   
print("student1 is not student2:", student1 is not student2)  
print("student1 is not student3:", student1 is not student3)

