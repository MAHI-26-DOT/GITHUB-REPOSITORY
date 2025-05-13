import random


class DiceSimulator:
    def __init__(self):
        self.dice_sides = 6
        self.dice_count = 1

    def roll_dice(self):
        return [random.randint(1, self.dice_sides) for _ in range(self.dice_count)]

    def display_results(self, results):
        print(f"You rolled {self.dice_count}d{self.dice_sides}: {results}")
        print(f"Total: {sum(results)}")

    def play_game(self):
        while True:
            print("\n1. Roll Dice")
            print("2. Change Dice Count")
            print("3. Change Dice Sides")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                results = self.roll_dice()
                self.display_results(results)
            elif choice == "2":
                self.dice_count = int(input("Enter new dice count: "))
            elif choice == "3":
                self.dice_sides = int(input("Enter new dice sides: "))
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    simulator = DiceSimulator()
    simulator.play_game()