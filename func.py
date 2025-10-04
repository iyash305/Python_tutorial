def greeting(name,age=25):
    print("Hello " + name, "you are " + str(age) + " years old")
    print(f"Hello {name}! you are {age} years old")
name = input("Enter your name:")
greeting("John",27)
greeting("Diana")
greeting(name,26)