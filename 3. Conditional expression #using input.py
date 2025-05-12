Motor_temperature = input("Please enter the motor temperatur of your car:")

Motor_temperature = int(Motor_temperature)

if (Motor_temperature > 100) :


    print("Your motor is boiling")

elif (Motor_temperature <= 100) :


    print("Your motor temperature is fine")

elif (Motor_temperature < 80) :



    print("There is something wrong with your motor")

else :

    print("Your motor is working fine")