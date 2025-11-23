def classify_waste_by_name(item_name):
    """
    Classifies waste as 'Dry' or 'Wet' based on keywords in the item name.
    
    Args:
        item_name (str): The name of the waste item entered by the user.

    Returns:
        str: The classification result.
    """
    
    item_name = item_name.lower().strip()

    
    wet_waste_keywords = [
        "food", "vegetable", "fruit", "peel", "leftover", "rotten", 
        "egg shell", "tea bag", "coffee ground", "meat", "bone", 
        "garden", "leaf", "plant", "soil"
    ]

  
    dry_waste_keywords = [
        "plastic", "bottle", "paper", "cardboard", "metal", "can", 
        "glass", "tin", "wrapper", "styrofoam", "magazine", "battery",
        "aluminum", "foil", "bag", "cloth"
    ]

   
    for keyword in wet_waste_keywords:
        if keyword in item_name:
            return "**Wet Waste** (Compostable)"

   
    for keyword in dry_waste_keywords:
        if keyword in item_name:
            return "**Dry Waste** (Recyclable)"

    
    return "Classification **Unknown**. Please specify the material (e.g., 'plastic bottle' or 'rotten fruit')."


print("-Waste Segregation Guide-")
print("Enter the name of a waste item to find out where to put it (type 'quit' to exit).")

while True:
    user_input = input("\nEnter waste item name: ")
    
    if user_input.lower() == 'quit':
        print("Thank you for segregating your waste! Goodbye.")
        break
    
    classification = classify_waste_by_name(user_input)
    
    print(f"\n Item: **{user_input}**")
    print(f" Belongs in: {classification}")