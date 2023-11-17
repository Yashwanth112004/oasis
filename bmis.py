print("BMI Calculator")
weight=float(input("Enter your Weight in kilogrames : "))
height=float(input("Enter your height in meters : "))
t=height*height
m=weight/t
if(m<18.5):
    print("Your Body Mass Index is: ",m,"kg/m2")
    print("According to the Scientific Research, your weight status is : UnderWeight (You must take good food to increase your weight)")
elif(m>=18.5 and m<=24.9):
    print("Your Body Mass Index is: ",m,"kg/m2")
    print("According to the Scientific Research, your weight status is : Normal (Healthy Weight)")
elif(m>=25.0 and m<=29.9):
    print("Your Body Mass Index is: ",m,"kg/m2")
    print("According to the Scientific Research, your weight status is : OverWeight (You must take non-fatty foods and prefer doing exercise daily to burn fat)")
else:
    print("Your Body Mass Index is: ",m,"kg/m2")
    print("According to the Scientific Reasearch, your weight status is: Obesity (Take precautions before your health is damaged)")
