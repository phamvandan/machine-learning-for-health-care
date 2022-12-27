## Calorie perday Needs to lose weight
# Oxford 
# https://www.forbes.com/health/body/calorie-calculator/#:~:text=One%20pound%20equals%20about%203%2C500,to%20create%20this%20caloric%20deficit.
"""
Input: 
    Gender: "male, female" (str)
    Age: int > 0
    Height: int > 0
    Current weight: int > 0
    Goal weight: int > Current weight > 0 
    Time to obtain: int > 0
    Exercise mode: sedentary, light, moderate, hard, very hard (str)
Output:
    Calorie perday Needs to gain weight (cal): float
    Recomend: str
"""
# Ty le trao doi chat co ban
def Basal_Metabolic_Rate(age, sex, weight):
    if sex == "male":
        if 0<age<=3:
            return 61*weight - 33.7
        elif 3<age<=10:
            return 23.3*weight + 514
        elif 10<age<=18:
            return 18.4*weight + 581
        elif 18<age<=30:
            return 16*weight + 545
        elif 30<age<=60:
            return 14.2*weight + 593
        elif 60<age:
            return 16.5*weight + 514
    else:
        if 0<age<=3:
            return 58.9*weight - 23.1
        elif 3<age<=10:
            return 20.1*weight + 507
        elif 10<age<=18:
            return 11.1*weight + 761
        elif 18<age<=30:
            return 13.1*weight + 558
        elif 30<age<=60:
            return 9.74*weight + 694
        elif 60<age:
            return 10.1*weight + 569

# calorie burn perday by activities
# https://www.bmi-calculator.net/bmr-calculator/harris-benedict-equation/
def Harris_Benedict_Equation(age, sex, weight, activity):
    bmr = Basal_Metabolic_Rate(age, sex, weight)
    ratio = 1
    if activity == 'sedentary': # little or no exercise
        ratio = 1.2
    elif activity == 'light': # light exercise/sports 1-3 days/week
        ratio = 1.375
    elif activity == 'moderate': # moderate exercise/sports 3-5 days/week
        ratio = 1.55
    elif activity == 'hard': # hard exercise/sports 6-7 days a week
        ratio = 1.725
    elif activity == 'very hard': # very hard exercise/sports & physical job or 2x training
        ratio = 1.9
    return bmr*ratio*1.1 # thermogenic

# https://www.bmi-calculator.net/bmr-calculator/harris-benedict-equation/calorie-intake-to-lose-weight.php
# tang can trong 1 khoang thoi gian
def gain_weight(age, sex, weight, activity, height, goal_weight, days):
    if goal_weight <= weight:
        return {"Message": "Invalid input"}

    hbe = Harris_Benedict_Equation(age, sex, weight, activity)
    total_calo_plus = (goal_weight - weight)*7716
    return {
        "Cal/day": hbe + total_calo_plus/days,
        "Days": days
    }

# recomend thoi gian va calo moi ngay de giam can   
def recomend_gain_weight(age, sex, weight, activity, height, goal_weight):
    if goal_weight <= weight:
        return {"Message": "Invalid input"}

    hbe = Harris_Benedict_Equation(age, sex, weight, activity)
    total_calo_plus = (goal_weight - weight)*7716
    return {
        "Cal/day": hbe*1.2,
        "Days": total_calo_plus/(hbe*0.2)
    }

# API 1: tang can trong 1 khoang thoi gian
cal_per_day = gain_weight(25, "male", 60, "light", 170, 70, 60)
print(cal_per_day)
# API 2: recomend thoi gian va calo moi ngay de tang can 
print(recomend_gain_weight(25, "male", 60, "light", 170, 70))
