class CoffeeMachine:
    def __init__(self):
        self.total_money = 550
        self.total_water = 400
        self.total_milk = 540
        self.total_beans = 120
        self.total_cups = 9

    def check_values(self, water, milk, beans, money):
        if water > self.total_water:
            print("Sorry, not enough water!")
        elif milk > self.total_milk:
            print("Sorry, not enough milk!")
        elif beans > self.total_beans:
            print("Sorry, not enough beans!")
        elif 1 > self.total_cups:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.total_water -= water
            self.total_milk -= milk
            self.total_beans -= beans
            self.total_money += money
            self.total_cups -= 1


    def buy(self, coffee):
        if coffee == '1':
            self.check_values(250, 0, 16, 4)
        elif coffee == '2':
            self.check_values(350, 75, 20, 7)
        elif coffee == '3':
            self.check_values(200, 100, 12, 6)
        elif coffee == 'back':
            pass
        else:
            print("Please make a valid selection.")

    def fill(self, add_water, add_milk, add_beans, add_cups):
        self.total_water += add_water
        self.total_milk += add_milk
        self.total_beans += add_beans
        self.total_cups += add_cups

    def take(self):
        print(f"I gave you ${self.total_money}")
        self.total_money = 0

    def remaining(self):
        print(f'''The coffee machine has: \n{self.total_water} of water \n{self.total_milk} of milk
{self.total_beans} of coffee beans \n{self.total_cups} disposable cups \n{self.total_money} of money\n''')


coffee_machine = CoffeeMachine()
while True:
    print("Write action (buy, fill, take, remaining, exit): ")
    action = input()
    print()
    if action.lower() == 'buy':
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_machine.buy(input())
    elif action.lower() == 'fill':
        print("Write how many ml of water do you want to add:")
        f_water = int(input())
        print("Write how many ml of milk do you want to add:")
        f_milk = int(input())
        print("Write how many ml of beans do you want to add:")
        f_beans = int(input())
        print("Write how many ml of cups do you want to add:")
        f_cups = int(input())
        coffee_machine.fill(f_water, f_milk, f_beans, f_cups)
    elif action.lower() == 'take':
        coffee_machine.take()
    elif action.lower() == 'remaining':
        coffee_machine.remaining()
    elif action.lower() == 'exit':
        break
