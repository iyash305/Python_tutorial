def greeting(name,age=25,colour ="red"):
    print("Hello " + name.capitalize(), " you will be " + str(age+1) + " next birthday")
    print(f"Hello {name.capitalize()}! you will be  {age+1} next birthday")
    print(f"We heard you like the colour {colour.lower()}")
name = input("Enter your name:")
age = input("Enter your age: ")
colour = input("Enter your favourite colour: ")

greeting("Yash",int(age),colour)
