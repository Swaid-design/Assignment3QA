import unittest
import app

from app import BMI_Calculator
from app import Retirement_Savings

class BMICalcTest(unittest.TestCase):

    def test_set_weight_error(self):  #bad values
        person = BMI_Calculator("5 11", -1)
        with self.assertRaises(KeyError):
            person.set_weight()
        person = BMI_Calculator("5 11", 0)
        with self.assertRaises(KeyError):
            person.set_weight()
        person = BMI_Calculator("5 11", 601)
        with self.assertRaises(KeyError):
            person.set_weight()

    def test_set_weight_no_error(self):  #good values
        person = BMI_Calculator("5 11", 150)
        self.assertAlmostEqual(person.set_weight(), 68.04)

    def test_set_height_error(self):  #bad values
        person = BMI_Calculator("-1 -1", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("-1 0", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("0 -1", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("0 0", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("0 12", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("-1 12", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("-1 11", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("11 -1", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("11 0", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("10 -1", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("11 12", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("11 11", 150)
        with self.assertRaises(KeyError):
            person.set_height()
        person = BMI_Calculator("10 12", 150)
        with self.assertRaises(KeyError):
            person.set_height()

        
    def test_set_height_no_error(self):  #good values
        person = BMI_Calculator("0 11", 150)
        self.assertEqual(person.set_height(), .08)
        person = BMI_Calculator("10 11", 150)
        self.assertEqual(person.set_height(), 11.07)
        person = BMI_Calculator("10 0", 150)
        self.assertEqual(person.set_height(), 9.29)

    def test_BMI_Calc(self):
        person = BMI_Calculator("5 11", 150)
        self.assertEqual(person.set_height(), 3.25)
        self.assertEqual(person.set_weight(), 68.04)
        self.assertEqual(person.BMICalc(), 20.92)

    def test_BMI_category(self):
        person = BMI_Calculator("5 11", 100)
        person.set_height()
        person.set_weight()
        self.assertEqual(person.BMI_category(), "Underweight")
        person = BMI_Calculator("5 11", 150)
        person.set_height()
        person.set_weight()
        self.assertEqual(person.BMI_category(), "Normal weight")
        person = BMI_Calculator("5 11", 200)
        person.set_height()
        person.set_weight()
        self.assertEqual(person.BMI_category(), "Overweight")
        person = BMI_Calculator("5 11", 300)
        person.set_height()
        person.set_weight()
        self.assertEqual(person.BMI_category(), "Obese")

class Retirement(unittest.TestCase):
    
    def test_create_Retirment(self):
        person = Retirement_Savings(22, 70000, .2, 500000)

    def test_set_age(self):
        person = Retirement_Savings(22, 70000, .2, 500000)
        with self.assertRaises(KeyError):
            person.set_age(-1)
        with self.assertRaises(KeyError):
            person.set_age(0)
        with self.assertRaises(KeyError):
            person.set_age(101)
        self.assertEqual(person.set_age(100), 100)
        self.assertEqual(person.set_age(22), 22)

    def test_set_salary(self):
        person = Retirement_Savings(22, 70000, .2, 500000)
        with self.assertRaises(KeyError):
            person.set_salary(-1)
        with self.assertRaises(KeyError):
            person.set_salary(0)
        with self.assertRaises(KeyError):
            person.set_salary(500001)
        self.assertEqual(person.set_salary(500000), 500000)
        self.assertEqual(person.set_salary(70000), 70000)

    def test_set_percent(self):
        person = Retirement_Savings(22, 70000, .2, 500000)
        with self.assertRaises(KeyError):
            person.set_percent(-1)
        with self.assertRaises(KeyError):
            person.set_percent(0)
        with self.assertRaises(KeyError):
            person.set_percent(1.1)
        self.assertEqual(person.set_percent(1), 1)
        self.assertEqual(person.set_percent(.2), .2)

    def test_set_goal(self):
        person = Retirement_Savings(22, 70000, .2, 500000)
        with self.assertRaises(KeyError):
            person.set_goal(-1)
        with self.assertRaises(KeyError):
            person.set_goal(0)
        with self.assertRaises(KeyError):
            person.set_goal(1000000001)
        self.assertEqual(person.set_goal(1000000000), 1000000000)
        self.assertEqual(person.set_goal(1000000), 1000000)

    def test_savings_per_year(self):
        person = Retirement_Savings(22, 70000, .2, 500000)
        self.assertEqual(person.savings_per_year(70000, .2), 18900)

    def test_age_goal_met(self):
        person = Retirement_Savings(22, 70000, .2, 1000000)
        self.assertEqual(person.age_goal_met(), 75)
    

if __name__ == '__main__':
    unittest.main()