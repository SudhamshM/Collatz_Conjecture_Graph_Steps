from matplotlib import pyplot as plt
print('''
        The Collatz Conjecture: Steps Down To One
        Using the Collatz Conjecture, it seems like almost any number
        can be brought back down to the number one.
        ''')
original_number = int(input("Enter Number: "))
number = original_number
highest = 0
steps = 0
y = [original_number]  # creating a blank list for numbers where the conjecture applies the rules to plot y axis
while True:
    if number % 2 == 0:  # if number is even
        number = number / 2
        steps = steps + 1
        if number > highest:
            highest = number
        y.append(number)
    elif (number % 2 != 0) and (number != 1):  # if number is odd and not 1
        number = (3 * number) + 1
        steps = steps + 1
        if number > highest:
            highest = number
        y.append(number)
    elif number == 1:  # when it is either 1 or comes down to 1
        print(f'''
            Applying the 3n+1 rule for odds & n/2 for evens...
            
            Original Number: {original_number}
            Final Number: {int(number)}
            Steps Taken To Reach To The Number One: {steps}
            Highest Number Reached During The Steps: {int(highest)}''')
        graph_choice = str(input("Would You Like To See A Graph For These Steps [y/n]? "))
        if graph_choice == 'y':
            x = range(steps + 1)
            plt.style.use('seaborn')
            plt.plot(x, y, color='g')
            plt.title("Collatz Conjecture - The 3n+1 Problem")
            plt.xlabel("Step Count")
            plt.ylabel("Operation Number")
            plt.legend(['Operation Line'])
            plt.show()
            break
        elif graph_choice == 'n':
            print("Okay, thank you for running this program!")
            break
        else:
            print("Not a valid choice. Quitting...")
            break
