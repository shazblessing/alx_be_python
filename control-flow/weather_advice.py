def main():
    """Asks user for weather condition and provides clothing advice."""
    #Suggested weather condions
    weather_options = ["sunny", "rainy", "cold"]
    #user input
    weather = input("What's the weather like today? (sunny/rainy/cold): ")
    # check weather and provide recommendations
    if weather.lower() in weather_options:
        if weather == "sunny":
            print("Wear a t-shirt and sunglasses!")
        elif weather == "rainy":
            print("Don't forget your umbrella and a raincoat.")
        else: # Weather == "cold"
            print("Make sure to wear a warm coat and a scarf.")   
    else:
        print(f"Sorry, I don't have recommendations for '{weather}' weather.")
if __name__ == "__main__":  
    main() 