# Weight loss: 40/40/20 (carbs/protein/fats)
# Weight gain: 40/30/30
# Weight maintenance: 40/30/33

# cal to carb,protein,fat requirement conversion
def carb_protein_fat_require(total_cal, type):
    if type == 'loss':
        return {
            "Carbs(g)": 0.4*total_cal//4,
            "Protein(g)": 0.4*total_cal//4,
            "Fats(g)": 0.2*total_cal//9,
        }
    return {
        "Carbs(g)": 0.4*total_cal//4,
        "Protein(g)": 0.3*total_cal//4,
        "Fats(g)": 0.3*total_cal//9,
    }

# API: cal to carb,protein,fat requirement conversion
print(carb_protein_fat_require(total_cal=2731.575, type='gain'))