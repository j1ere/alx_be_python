weather = input("What's the weather like today?(sunny/rainy/cold):")

weather_input = weather.lower()

if weather_input == 'sunny':
    print('Wear a t-shirt and sunglasses.')
elif weather_input == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather_input == 'cold':
    print("Make sure you wear a warm coat and a scarf")
else:
    print("Sorry, I don't have recommendations for this weather.")
    