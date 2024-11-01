def personalized_nutrition_guide(sport, age_group, health_condition, food_allergies, dietary_preference):
    guide = {}

    # Nutrition guide by sport
    if sport == "Yoga":
        guide["sport"] = "Plant-based and anti-inflammatory foods to aid flexibility and recovery"
    elif sport == "Running":
        guide["sport"] = "Carbohydrates for endurance and protein for muscle recovery"
    elif sport == "Swimming":
        guide["sport"] = "Balanced high-protein and quick energy sources"
    else:
        guide["sport"] = "General sports nutrition guide"

    # Recommendations by age group
    age_nutrition = {
        "Under 18": "Calcium and protein are essential to support growth",
        "18-25": "High-energy foods and low-fat protein",
        "26-35": "Antioxidant-rich foods for recovery and muscle fatigue prevention",
        "36-45": "Anti-inflammatory foods and low-fat protein for heart health",
        "46-55": "High-fiber foods and joint-supporting nutrients",
        "56-65": "Nutrient-dense foods for bone and joint support",
        "Over 65": "Easy-to-digest foods that support energy and bone health"
    }
    guide["age"] = age_nutrition.get(age_group, "General age-based nutrition guide")

    # Recommendations based on health condition
    guide["health_condition"] = "Low-sugar foods friendly to the heart, avoiding triggers" if health_condition == "Yes" else "Standard sport-specific nutrition guide"

    # Adjustments based on food allergies
    guide["food_allergies"] = "Alternatives to common allergens (e.g., dairy, nuts)" if food_allergies == "Yes" else "All foods available"

    # Guide based on dietary preference
    guide["dietary_preference"] = "Balanced protein, carbohydrates, and fats" if dietary_preference == "Normal" else "Plant-based protein, whole grains, and iron-rich foods"

    # Sample menu creation (covering all condition combinations)
    if dietary_preference == "Vegetarian":
        if sport == "Running":
            guide["sample_menu"] = {
                "breakfast": "Acai bowl and chia seeds",
                "lunch": "Bean and kale salad",
                "dinner": "Vegetable stir-fry with quinoa",
                "snacks": "Protein bar and nuts",
                "supplements": "B12, iron, omega-3"
            }
        elif sport == "Swimming":
            guide["sample_menu"] = {
                "breakfast": "Smoothie with banana and almond butter",
                "lunch": "Falafel and spinach wrap",
                "dinner": "Tofu steak and sweet potato",
                "snacks": "Dried fruits and seeds",
                "supplements": "B12, iron, omega-3"
            }
        else:
            guide["sample_menu"] = {
                "breakfast": "Yogurt with berries and mixed nuts",
                "lunch": "Avocado and black bean salad",
                "dinner": "Grilled eggplant with lentil curry",
                "snacks": "Oat bar",
                "supplements": "B12, iron, omega-3"
            }
    else:
        if sport == "Running":
            guide["sample_menu"] = {
                "breakfast": "Avocado toast with boiled eggs",
                "lunch": "Chicken breast and quinoa salad",
                "dinner": "Roasted salmon with vegetables",
                "snacks": "Greek yogurt with mixed berries",
                "supplements": "Multivitamin, calcium"
            }
        elif sport == "Swimming":
            guide["sample_menu"] = {
                "breakfast": "Protein smoothie (banana, spinach, protein powder)",
                "lunch": "Chicken salad wrap",
                "dinner": "Chicken and brown rice bowl",
                "snacks": "Nuts and fruits",
                "supplements": "Vitamin D, magnesium"
            }
        elif sport == "Yoga":
            guide["sample_menu"] = {
                "breakfast": "Green smoothie and acai bowl",
                "lunch": "Avocado and veggie sandwich",
                "dinner": "Tomato and spicy tofu pasta",
                "snacks": "Almonds and apple",
                "supplements": "Vitamin C, antioxidants"
            }
        else:
            guide["sample_menu"] = {
                "breakfast": "Omelette with toast",
                "lunch": "Turkey sandwich with salad",
                "dinner": "Beef and vegetable stir-fry",
                "snacks": "Nuts and fruit bar",
                "supplements": "Multivitamin"
            }

    return guide
