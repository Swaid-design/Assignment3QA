import math

class BMI_Calculator:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.BMI = 0
        self.category = ""

        pass

    def set_height(self):
        height = self.height.split()
        feet = float(height[0])
        if feet < 0 or feet > 10:
            raise KeyError
        inches = int(height[1])
        if inches < 0 or inches >= 12:
            raise KeyError
        if feet == 0 and inches == 0:
            raise KeyError
        height = (feet * 12) + inches
        meters = height*.0254
        self.height = meters * meters
    
        return round(self.height, 2)

    def get_height(self):
        return self.height

    def set_weight(self):
        #weight = int(input("How much do you weigh in pounds: "))
        if self.weight <= 0 or self.weight > 600:
            raise KeyError()
        else:
            self.weight = self.weight*.45359
            return round(self.weight, 2)

    def get_weight(self):
        return self.weight

    def BMICalc(self):
        self.BMI = self.weight/self.height
        return round(self.BMI, 2)

    def BMI_category(self):
        self.BMICalc()
        if (self.BMI < 18.5):
            self.category = "Underweight"
        if (self.BMI >= 18.5 and self.BMI <= 24.9):
            self.category = "Normal weight"
        if (self.BMI >= 25 and self.BMI <= 29.9):
            self.category = "Overweight"
        if (self.BMI >= 30):
            self.category = "Obese"
        return self.category




class Retirement_Savings:

    def __init__(self, age, salary, percent, goal):
        self.age = age
        self.salary = salary
        self.percent = percent
        self.goal = goal
        self.savingsPerYear = 0
        self.ageGoalMet = 0
        pass

    def set_age(self, age):
        if (age <= 0):
            raise KeyError
        if (age > 100):
            raise KeyError

        return age

    def set_salary(self, salary):
        if (salary <= 0):
            raise KeyError
        if (salary > 500000):
            raise KeyError

        return salary

    def set_percent(self, percent):
        if (percent <= 0.0):
            raise KeyError
        if (percent > 1.0):
            raise KeyError

        return percent

    def set_goal(self, goal):
        if (goal <= 0):
            raise KeyError
        if (goal > 1000000000):
            raise KeyError

        return goal

    def savings_per_year(self, salary, percent):
        self.savingsPerYear = (self.salary * self.percent) * 1.35

        return self.savingsPerYear

    def age_goal_met(self):
        self.savingsPerYear = (self.salary * self.percent) * 1.35
        years = self.goal / self.savingsPerYear
        years = math.ceil(years)

        self.ageGoalMet = years + self.age

        return self.ageGoalMet


if __name__ == "__main__":
    selection = 0
    while selection == 0:
        print("Option 1: BMI Calculator")
        print("Option 2: Retirement Savings Calculator")
        print("Option 3: Exit Program")
        selection = int(input("Select an option: "))
        if (selection == 2):
            age = int(input("Your age: "))
            salary = int(input("Your salary: "))
            percent = float(input("Your percentage saved each year: "))
            goal = int(input("Your goal: "))
            person = Retirement_Savings(age, salary, percent, goal)
            print("---------------------------------------------------")
            print("You will be ", person.age_goal_met(), "when you achieve your goal.")
            print("---------------------------------------------------")
            selection = 0
        if (selection == 3):
            exit()
        if(selection == 1):
            weight = int(input("Your weight in lbs: "))
            height = str(input("Your height (ft in): "))
            
            person = BMI_Calculator(height, weight)
            person.set_height()
            person.set_weight()

            print("---------------------------------------------------")
            print("Your BMI is: ", person.BMICalc(), "which is considered: ", person.BMI_category())
            print("---------------------------------------------------")
            selection = 0




        



