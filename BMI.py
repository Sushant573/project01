while True:
    foot=12*(int(input("foot:-")))+int(input("inch:-"))
    weight=703*int(input("enter your weight:-"))
    c=weight/foot
    BMI=c/foot
    if BMI < 18.5:
        print("You are underweight.\n",BMI)
    elif 18.5 <= BMI < 24.9:
              print("You have a normal weight.\n",BMI)
    elif 25 <= BMI < 29.9:
       print("You are overweight.\n",BMI)
    else:
      print("You are obese.\n",BMI)
      again=input("do you want to calculate again press YES/NO:-")
      if again!='yes':
          print("thank you for visiting")
          break

