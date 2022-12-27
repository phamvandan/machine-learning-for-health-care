# https://www.prokerala.com/health/health-calculators/waist-to-hip-ratio.php
# https://nutritionalassessment.mumc.nl/en/waist-hip-ratio-whr-and-waist-circumference#:~:text=The%20Waist%20Hip%20Ratio%20is,%3D%20waist%20circumference%20%2F%20hip%20circumference.
# male/female, cm, cm
def waist_to_hip_ratio(sex, waist_circumference, hip_circumference):
    ratio = waist_circumference / hip_circumference
    if sex == 'male':
        if ratio <= 0.95:
            message = 'Your ratio are idealy'
        else:
            message = 'Your ratio are not idealy'
        if waist_circumference<94:
            health_risk = 'Low'
        elif 94<=waist_circumference<100:
            health_risk = 'High'
        else:
            health_risk = 'Very high'
    else:
        if ratio <= 0.7:
            message = 'Your ratio are idealy'
        else:
            message = 'Your ratio are not idealy'

        if waist_circumference<80:
            health_risk = 'Low'
        elif 80<=waist_circumference<89:
            health_risk = 'High'
        else:
            health_risk = 'Very high'

    return {
       'ratio': ratio, 
       'message': message,
       'health risk': health_risk
    }   

# API waist to hip ratio and health risk
print(waist_to_hip_ratio('female', 70, 100))