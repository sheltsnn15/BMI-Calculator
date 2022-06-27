numGym = input("Enter num gym members:")
numGym = int(numGym)
count = 0
for x in range(numGym):

    memberName = input("Enter your name:")
    units = input ("Would you like to calculate your BMI using metric units or imperial units:")
    
    if units == ("metric"): #if the user inputs "metric", the program will calculate metric
        metricHeight = float(input("\nPlease enter your height in meters: "))
        metricWeight = int(input("\nPlease enter your weight in kilograms: "))
        
        bmiMetric = metricWeight / (metricHeight**2)
        bmiMetric = round(bmiMetric,1)
        
        if bmiMetric <18.5:
            print(numGym,".",memberName,",your BMI is" ,bmiMetric, "which means your are Underweight")
        
        elif bmiMetric >= 18.5 and bmiMetric <25:
            print(numGym,".",memberName,",your BMI is" ,bmiMetric, "which means your are Normal")
        
        elif bmiMetric >= 25 and bmiMetric <30:
            print(numGym,".",memberName,",your BMI is" ,bmiMetric, "which means your are Overweight")
        
        elif bmiMetric >=30:
            print(numGym,".",memberName,",your BMI is" ,bmiMetric, "which means your are Obese")
    #the loop if the user enters "imperial"

    else : # else if the user inputs "imperial", the program will calculate imperial
        imperialHeight = float(input("\nPlease enter your height in inches:"))
        imperialWeight = int(input("\nPlease enter your weight in pounds:"))
        
        bmiImperial = imperialWeight*703 / (imperialHeight**2)
        bmiImperial = round(bmiImperial,1)# round off the answer to one decimal place
        
        if bmiImperial <18.5:
            print(numGym,".",memberName,",your BMI is" ,bmiImperial, "which means your are Underweight")
        
        elif bmiImperial >= 18.5 and bmiImperial <25:
            print(numGym,".",memberName,",your BMI is" ,bmiImperial, "which means your are Normal")
        
        elif bmiImperial >= 25 and bmiImperial <30:
            print(numGym,".",memberName,",your BMI is" ,bmiImperial, "which means your are Overweight")
        
        elif bmiImperial >=30:
            print(numGym,".",memberName,",your BMI is" ,bmiImperial, "which means your are Obese")
