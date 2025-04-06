# Calculate the average of rain
def rain_average(list_rain):
    return (sum(list_rain))/len(list_rain)

# Calculate the average of wind
def wind_average(list_average):
    return(sum(list_average))/len(list_average)

# Calculate the weather severity
def weather_severity(rainAverage, windAverage):
    return (rainAverage*10) + windAverage

rain_list = []
wind_list = []
end_loop = True

# loop to obtain value for the wind and the rain

while end_loop:

    input_string = input("Enter the rain and the wind seperated by a space:\n")
    input_list = input_string.split()

    if len(input_list) == 0: # check if the user enter a value
        print("Please enter a value\n")

    elif len(input_list) < 2 and input_list[0] == '-1.0' : # check if the user enter -1.0
        end_loop = False

    elif len(input_list) == 2:# check if the user enter 2 value
            rain_list.append(float(input_list[0]))
            wind_list.append(float(input_list[1]))

    else:
        print("Values entered are incorrect.\n")
        continue

avg_rain = rain_average(rain_list)
avg_wind = wind_average(wind_list)
weatherSeverity = weather_severity(avg_rain, avg_wind)

print(f"The average rain is {avg_rain:.1f} inches\n"
      f"The average wind is {avg_wind:.1f} mph \n"
      f"The weather severity for these {len(rain_list)} readings is: {weatherSeverity:.1f}")