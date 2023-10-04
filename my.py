def Registration():
    Name = input('my name is: ')
    phone_number = input('my number is:')
    email = input('my email is: ')
    gender = input('Enter student gender: ')
    age = int(input('student age is: '))

    # return Name, phone_number, email,gender,age

    print(Name)
    print(phone_number)
    print(email)
    print(gender)
    print(age)

Registration()




import Registration
student_record = Registration.student File
print(student_record['name'])