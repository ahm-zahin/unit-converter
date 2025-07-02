
def main():
    print('welcome to the unit converter program')
    while True:
        c = int(input('\nChoose:\n1. Temp\n2. Distance\n3. Exit\nYou choose: '))
        if c == 1:
            temp_conversion()
        elif c == 2:
            distance_conversion()
        elif c == 3:
            print(f'{c} is pressed, we are exiting...')
            break
        else:
            print('Invalid input, please enter 1, 2 or 3')
            continue
    print('Thank you for using the unit converter program!')
def temp_conversion():
    t=int(input('\nConvert from:\n1. Cel\n2. Fahr\n3. Kel\nYou choose: '))
    if t==1:
        temp_c=float(input('Enter value in Cel: '))
        temp_f=(temp_c * 9/5) + 32
        temp_k=temp_c + 273.15
        print(f'Temperature in Fahrenheit: {temp_f:.2f}°F')
        print(f'Temperature in Kelvin: {temp_k:.2f}K')
    elif t==2:
        temp_f=float(input('Enter value in Fahrenheit: '))
        temp_c=(temp_f - 32) * 5/9
        temp_k=temp_c + 273.15
        print(f'Temperature in Celsius: {temp_c:.2f}°C')
        print(f'Temperature in Kelvin: {temp_k:.2f}K')
    elif t==3:
        temp_k=float(input('Enter value in Kelvin: '))
        temp_c=temp_k - 273.15
        temp_f=(temp_c * 9/5) + 32
        print(f'Temperature in Celsius: {temp_c:.2f}°C')
        print(f'Temperature in Fahrenheit: {temp_f:.2f}°F')
        
def distance_conversion():
    dis=int(input('\nConvert from:\n1. Kilometers\n2. Meters\n3. Miles\nYou choose: '))
    if dis==1:
        km=float(input('Enter value in Kilometers: '))
        m=km * 1000
        mi=km * 0.621371
        print(f'Distance in Meters: {m:.2f}m')
        print(f'Distance in Miles: {mi:.2f}mi')
    elif dis==2:
        m=float(input('Enter value in Meters: '))
        km=m / 1000
        mi=m * 0.000621371
        print(f'Distance in Kilometers: {km:.2f}km')
        print(f'Distance in Miles: {mi:.2f}mi')
    elif dis==3:
        mi=float(input('Enter value in Mile: '))
        km=mi / 0.621371
        m=mi / 0.000621371
        print(f'Distance in Kilometers: {km:.2f}km')
        print(f'Distance in Meters: {m:.2f}m')
    
main()
