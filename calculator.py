def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("Error: Cannot divide by 0")
        return None
    else:
        return x / y


def main():
    print('\n Welcome to my calculator.')
    print('Select an operation.')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')

    while True:
        print('Select an operation.')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Quit')

        choice = input('Please enter 1,2,3,4 or 5 to quit: ')

        if choice == '5':
            print('Thank you for using my calculator.')
            break


        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input('Please enter the first number here: '))
                num2 = float(input('Please enter the second number here: '))
            except ValueError:
                print('Welcome enter 1,2,3,4 or 5')
                continue


            if choice == '1':
                print(f'{num1} + {num2} = {add(num1, num2)}')

            elif choice == '2':
                print(f'{num1} - {num2} = {subtract(num1, num2)}')

            elif choice == '3':
                print(f'{num1} * {num2} = {multiply(num1, num2)}')

            elif choice == '4':
                result = divide(num1, num2)
                if result is not None:
                    print(f'{num1} + {num2} = {result}')

        else:
            print('Please enter a valid number.')


if __name__ == '__main__':
    main()
