equation = input("""will you be converting celcius to fahrenheit or fahrenheit to celcius? /n
                 for C to F type 'CF', for F to C type 'FC' """)

value = input("""Please enter the number vaule: """)

value = float(value)

if equation == 'FC':
    strFahrenheit = (value - 32) * 5 / 9

    strFahrenheit = str(strFahrenheit)

    print(strFahrenheit)


elif 'CF':
    # strCelsius being our formula

    strCelsius = (value * 1.8) + 32

    # convert strcelsius to string format

    strCelsius = str(strCelsius)

    # give output

    print(strCelsius)

else:
    print("please enter either 'CF' or 'FC'. ")
