def switch(season):
    return {
        'fall': 1,
        'winter': 2,
        'summer': 3,
        'spring': 4,
    }[season.lower()]


try:
    print(switch('Winter'))
except:
    print("enter a correct value")
