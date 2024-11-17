def personalized_nutrition_guide(health_condition, food_allergies, dietary_preference):
    guide = {}

    # Recommendations based on health condition
    guide["health_condition"] = (
        "Low-sugar foods friendly to the heart, avoiding triggers"
        if health_condition == "Yes"
        else "Standard health-based nutrition guide"
    )

    # Adjustments based on food allergies
    if food_allergies == "Yes":
        guide["food_allergies"] = "Alternatives to common allergens (e.g., dairy, nuts)"
    else:
        guide["food_allergies"] = "All foods available"

    # Guide based on dietary preference
    if dietary_preference == "vegetarian":
        guide["dietary_preference"] = "Plant-based protein, whole grains, and iron-rich foods"
    else:
        guide["dietary_preference"] = "Balanced protein, carbohydrates, and fats"

    # Sample menu creation based on food allergies and dietary preference
    if dietary_preference == "vegetarian":
        if food_allergies == "Yes":
            guide["sample_menu"] = {
                "breakfast": "Smoothie with banana, oat milk, and chia seeds",
                "lunch": "Quinoa and black bean salad with sunflower seeds",
                "dinner": "Vegetable stir-fry with tofu (no nuts)",
                "snacks": "Apple slices with sunflower butter",
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
        if food_allergies == "Yes":
            guide["sample_menu"] = {
                "breakfast": "Avocado toast with boiled eggs (gluten-free bread)",
                "lunch": "Chicken breast with quinoa and roasted vegetables",
                "dinner": "Grilled salmon with sweet potato (no dairy)",
                "snacks": "Fruit salad with seeds",
                "supplements": "Multivitamin, calcium"
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
