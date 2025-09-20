# Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.

weather_today = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather_today == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_today == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_today == "cold":   
    print("Wear a warm coat and a scarf.")
else: 
    print("Sorry, I don't have recommendations for this weather.")