name = input("Hi, please enter your name!:")
print(name)
score = input("What score did you get in the test?:")
print(score)
if score >="075":
    print("Well",name,"the score",score,"is amazing. Well done!")
elif score >="050":
    print("Well",name,"the score",score,"is good, keep going for better marks!")
elif score <="050":
    print("Well",name,"the score",score,"is not so good, try harder!")

