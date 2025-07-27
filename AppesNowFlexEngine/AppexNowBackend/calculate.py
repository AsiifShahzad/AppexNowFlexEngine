import math

def calculate_raise_bonus(data):
    """
    Enhanced salary calculation with realistic constraints and Pakistan city considerations
    """
    
    # Job role hierarchy and base raise percentages
    job_role_config = {
        "Software Engineer": {"base_raise": 0.06, "max_raise": 0.15, "bonus_multiplier": 1.0},
        "Senior Software Engineer": {"base_raise": 0.07, "max_raise": 0.18, "bonus_multiplier": 1.2},
        "Team Lead": {"base_raise": 0.08, "max_raise": 0.20, "bonus_multiplier": 1.4},
        "Project Manager": {"base_raise": 0.07, "max_raise": 0.17, "bonus_multiplier": 1.3},
        "Senior Manager": {"base_raise": 0.09, "max_raise": 0.22, "bonus_multiplier": 1.5},
        "Developer": {"base_raise": 0.05, "max_raise": 0.14, "bonus_multiplier": 0.9},
        "Data Scientist": {"base_raise": 0.08, "max_raise": 0.19, "bonus_multiplier": 1.3},
        "DevOps Engineer": {"base_raise": 0.07, "max_raise": 0.17, "bonus_multiplier": 1.1},
        "QA Engineer": {"base_raise": 0.05, "max_raise": 0.13, "bonus_multiplier": 0.8},
        "UI/UX Designer": {"base_raise": 0.06, "max_raise": 0.15, "bonus_multiplier": 1.0},
        "Other": {"base_raise": 0.05, "max_raise": 0.12, "bonus_multiplier": 0.8}
    }
    
    pakistan_cities_config = {
        "Karachi": {"cost_adjustment": 0.08, "bonus_base": 15000},
        "Lahore": {"cost_adjustment": 0.07, "bonus_base": 12000},
        "Islamabad": {"cost_adjustment": 0.09, "bonus_base": 18000}, 
        "Rawalpindi": {"cost_adjustment": 0.06, "bonus_base": 10000}, 
        "Faisalabad": {"cost_adjustment": 0.05, "bonus_base": 8000},  
        "Multan": {"cost_adjustment": 0.04, "bonus_base": 7000},     
        "Peshawar": {"cost_adjustment": 0.04, "bonus_base": 7500},   
        "Quetta": {"cost_adjustment": 0.05, "bonus_base": 8500},     
        "Sialkot": {"cost_adjustment": 0.04, "bonus_base": 6500},      
        "Gujranwala": {"cost_adjustment": 0.04, "bonus_base": 6000},   
        "Hyderabad": {"cost_adjustment": 0.03, "bonus_base": 5500},
        "Sargodha": {"cost_adjustment": 0.03, "bonus_base": 5000},    
        "Bahawalpur": {"cost_adjustment": 0.03, "bonus_base": 5000}, 
        "Sukkur": {"cost_adjustment": 0.03, "bonus_base": 4500},     
        "Larkana": {"cost_adjustment": 0.03, "bonus_base": 4500},  
        "Mardan": {"cost_adjustment": 0.03, "bonus_base": 4000},    
        "Kasur": {"cost_adjustment": 0.03, "bonus_base": 4000},     
        "Okara": {"cost_adjustment": 0.02, "bonus_base": 3500},      
        "Wah": {"cost_adjustment": 0.04, "bonus_base": 6000},     
        "Remote": {"cost_adjustment": 0.02, "bonus_base": 3000},       
        "Other": {"cost_adjustment": 0.02, "bonus_base": 3000}   
    }

    role_config = job_role_config.get(data.jobRole, job_role_config["Other"])
    base_raise_percentage = role_config["base_raise"]
    max_raise_percentage = role_config["max_raise"]
    bonus_multiplier = role_config["bonus_multiplier"]

    # Performance score should be 1-10, we'll normalize it to 0-1 impact
    performance_impact = 0
    if data.performanceScore >= 1 and data.performanceScore <= 10:
        normalized_performance = (data.performanceScore - 1) / 9  
        performance_impact = normalized_performance * 0.05  
    
    experience_impact = 0
    if data.yearsExperience > 0:
        # Logarithmic scaling for experience - early years matter more
        # Max impact around 4% for 20+ years
        experience_impact = min(0.04, math.log(data.yearsExperience + 1) * 0.015)
    
    total_raise_percentage = base_raise_percentage + performance_impact + experience_impact
    
    total_raise_percentage = min(total_raise_percentage, max_raise_percentage)
    
    raise_amount = data.currentSalary * total_raise_percentage

    city_config = pakistan_cities_config.get(data.location, pakistan_cities_config["Other"])
    
    location_salary_bonus = data.currentSalary * city_config["cost_adjustment"]
    location_fixed_bonus = city_config["bonus_base"]
    total_location_bonus = location_salary_bonus + location_fixed_bonus
    
    performance_bonus = 0
    if data.performanceScore >= 8:
        # Exceptional performers get additional bonus
        performance_bonus_percentage = (data.performanceScore - 7) * 0.01  # 1% per point above 7
        performance_bonus = data.currentSalary * performance_bonus_percentage * bonus_multiplier
    
    # Total bonus
    total_bonus = total_location_bonus + performance_bonus
    
    # Calculate total new salary
    total_new_salary = data.currentSalary + raise_amount + total_bonus
    
    # Return detailed breakdown
    return {
        "raiseAmount": round(raise_amount, 2),
        "bonusAmount": round(total_bonus, 2),
        "totalNewSalary": round(total_new_salary, 2),
        "breakdown": {
            "baseRaisePercentage": round(base_raise_percentage * 100, 2),
            "performanceImpact": round(performance_impact * 100, 2),
            "experienceImpact": round(experience_impact * 100, 2),
            "totalRaisePercentage": round(total_raise_percentage * 100, 2),
            "locationSalaryBonus": round(location_salary_bonus, 2),
            "locationFixedBonus": round(location_fixed_bonus, 2),
            "performanceBonus": round(performance_bonus, 2),
            "city": data.location,
            "jobRole": data.jobRole
        }
    }