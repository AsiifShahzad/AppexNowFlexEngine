def calculate_raise_bonus(data):
    base_raise_percentage = 0.05

    raise_percentage = base_raise_percentage + (data.performanceScore * 0.01) + (data.yearsExperience * 0.005)

    location_bonus_map = {
        "New York": 1000,
        "San Francisco": 1200,
        "Remote": 800
    }

    bonus = location_bonus_map.get(data.location, 500)
    raise_amount = data.currentSalary * raise_percentage
    total_new_salary = data.currentSalary + raise_amount + bonus

    return {
        "raiseAmount": round(raise_amount, 2),
        "bonusAmount": round(bonus, 2),
        "totalNewSalary": round(total_new_salary, 2)
    }
