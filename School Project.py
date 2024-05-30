from time import sleep
from os import system
import os
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import ctypes
from sys import platform
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))

if platform == "linux" or platform == "linux2":
    clear = lambda: system('cls') # for linux
elif platform == "darwin":
    clear = lambda: system('clear') # for MacOS
elif platform == "win32":
    clear = lambda: system('cls') # for Windows

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    print("")
    clear()
else:
    print("Please run this program as an administrator.")
    sleep(1)
    input("\nPress enter to exit...")
    exit()

def main():
    print("If you are doing this review program, you were probably absent.")
    sleep(1)
    print("Don't worry, that's why I am here to help you catch up to what we have learned in the lesson so far.")
    sleep(3)
    input("\nPress enter to continue...")
    clear()

    while True:
        print("What unit do you want to check (1-3)?")
        unitNum = input("\nUnit number: ")
        sleep(1)
        clear()

        if unitNum == "1":
            print("What lesson did you miss that you want to review (1.1-1.12)?")
            lessonNum = input("\nLesson number: ")

            if lessonNum == "1.1":
                clear()
                sleep(1)
                print("Lesson 1.1: Number Sets and Infinity\n")
                sleep(1)
                print("In the begining of the lesson, we learned what a set is.")
                sleep(2)
                print("A set is a collection of objects which may be mathematical or not.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("A set is commonly represented as a list of all its member enclosed in curly brackets.")
                sleep(2)
                print("For example, the set of even natural numbers is A = {2, 4, 6, 8, ...}")
                showImage("evenNaturalNumbers.png")
                sleep(2)
                input("\nPress enter to continue...")
                print("\nOr we could say 2 ∈ A.")
                sleep(2)
                print("This means that 2 is an element of the set A.")
                showImage("2EA.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("There are also a thing called a Subset.\n")
                sleep(2)
                print("Imagine Set A is said to be a subset of Set B.")
                sleep(2)
                print("Meaning that all the elements in Set A are also in Set B.")
                showImage("subset.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("There are different types of number sets.")
                sleep(2)
                print("There are Natural Numbers, Whole Numbers, Integers, Rational Numbers, Irrational Numbers, and Real Numbers.\n")
                sleep(2)
                print("\nNatural Numbers are all positive numbers starting from 1. It is represented with the letter N")
                sleep(2)
                print("\nWhole Numbers are Natural Numbers but start at 0 instead. It is represented with the letter W")
                sleep(2)
                print("\nIntegers are numbers that are both negative and positive. It is represented with the letter Z")
                sleep(2)
                print("\nRational Numbers is any number that can be represented as a fraction. It is represented with the letter Q")
                sleep(2)
                print("\nIrrational Numbers are numbers that can't be represented as a fraction (eg. π = 3.14..., e = 2.71...). It is represented with the letter P")
                sleep(2)
                print("\nAnd finally, Real Numbers. Real Numbers is any number. It is represented with the letter R")
                showImage("numberSets.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("Now, lets talk about infinity.\n")
                sleep(2)
                print("infinity is something that never ends,\nis an extremely large number,\nand has no limit.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("Whats a limit?\n")
                sleep(2)
                print("A limit is a boundary or a point where something ends or the maximum amount allowed,\nor it is something that is restricted.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("Let's talk about the density property.\n")
                sleep(2)
                print("Density property is the property that states that there always exists another rational number between any two given rational numbers. This means that the set of rational numbers is dense (infinite numbers exist between the two rational numbers).")
                sleep(2)
                showImage("densityProperty.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("Therefore, do Rational Numbers satisfy the density property?")

                q1 = input("Does (Y) : Does Not (N)\nAnswer: ").lower()

                if q1 == "y":
                    sleep(1)
                    print("Correct!")
                    sleep(2)
                    print("\n")
                else:
                    sleep(1)
                    print("Sorry, but it does satisfy it.")
                    sleep(2)
                    print("\n")

                print("Now, do Whole Numbers satisfy the density property?")

                q2 = input("Does (Y) : Does Not (N)\nAnswer: ").lower()

                if q2 == "n":
                    sleep(1)
                    print("Correct!")
                    sleep(2)
                    print("\n")
                else:
                    sleep(1)
                    print("Sorry, but it does not satisfy it.")
                    sleep(2)
                    print("\n")

                input("\nPress enter to continue...")
                clear()
                print("You are all caught up on lesson 1.1!")
                sleep(2)
                input("\nPress enter to go back to select a unit...")
                clear()
            elif lessonNum == "1.2":
                print("1.2")
            elif lessonNum == "1.3":
                print("1.3")
            elif lessonNum == "1.4":
                print("1.4")
            elif lessonNum == "1.5":
                print("1.5")
            elif lessonNum == "1.6":
                print("1.6")
            elif lessonNum == "1.7":
                print("1.7")
            elif lessonNum == "1.8":
                print("1.8")
            elif lessonNum == "1.9":
                print("1.9")
            elif lessonNum == "1.10":
                print("1.10")
            elif lessonNum == "1.11":
                print("1.11")
            elif lessonNum == "1.12":
                print("1.12")
            else:
                print("That isn't a lesson in the unit")
                sleep(3)
                clear()
        elif unitNum == "2":
            print("What lesson did you miss that you want to review (2.1-2.10)?")
            lessonNum = input("\nLesson number: ")

            if lessonNum == "2.1":
                clear()
                sleep(1)
                print("Lesson 2.1: Intro to Algebra\n")
                sleep(2)
                print("In algebra, we use letters called variables to represent any unknown number.")
                sleep(2)
                print("Variables can be any letter, such as x, y, z, a, b, c, etc.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("I am going to show you an image with some important definitions.")
                sleep(1)
                showImage("algebraDefinitions.png")
                input("\nPress enter to continue...")
                sleep(2)
                print("\nAs you can see, the variable in the image is x.")
                sleep(2)
                print("The coefficient is the number in front of the variable being 5.")
                sleep(2)
                print("And the exponent is the number that is a superscript of the variable being 3.")
                sleep(2)
                print("\nThis whole thing is called a term.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()

                print("Imagine you have the term -4.9^5x^2 (the \"^\" means \"to the power of\", \nso it would be negative four point nine to the power of 5 x to the power of 2).")

                q3 = input("\nWhat is the coefficient of the term?\nAnswer: ").lower()

                if q3 == "-4.9^5":
                    sleep(1)
                    print("Correct!")
                    sleep(2)
                    print("\n")
                else:
                    sleep(1)
                    print("Sorry, but the coefficient was -4.9^5.")
                    sleep(2)
                    print("\n")

                q4 = input("What is the variable of the term?\nAnswer: ").lower()

                if q4 == "x":
                    sleep(1)
                    print("Correct!")
                    sleep(2)
                    print("\n")
                else:
                    sleep(1)
                    print("Sorry, but the variable was x.")
                    sleep(2)
                    print("\n")

                print("Last question for now.")
                q5 = input("\nWhat is the exponent of the term?\nAnswer: ").lower()

                if q5 == "2":
                    sleep(1)
                    print("Correct!")
                    sleep(2)
                    print("\n")
                else:
                    sleep(1)
                    print("Sorry, but the exponent was 2.")
                    sleep(2)
                    print("\n")

                input("\nPress enter to continue...")
                clear()
                print("Now, lets talk about different scenerions.")
                sleep(2)
                print("\nImagine the term was just 7.")
                showImage("sevenUnaswered.png")
                input("\nPress enter to continue...")
                sleep(2)
                print("\nThis would just be called a constant.")
                sleep(4)
                print("This is because it has no variable, so it has no coefficient\nAnd there is no exponent.")
                showImage("sevenAnswered.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("Now, imagine the term was just x.")
                showImage("xUnanswered.png")
                input("\nPress enter to continue...")
                sleep(2)
                print("\nWhat do you think the coefficient and exponent would be?")
                sleep(4)
                showImage("xAnswered.png")
                input("\nPress enter to continue...")
                print("\nThe coefficient would be 1 and the exponent would be 1.")
                sleep(2)
                print("This is because you have only 1 of x, and the exponent is 1 because there is no number to the power of x so its just itself.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("Now let's talk about what is a polynomial.\n")
                sleep(2)
                print("A polynomial is an algebraic expression that has 2 or more terms.")
                sleep(2)
                print("These terms are separated by addition or subtraction signs.")
                sleep(2)
                print("The variable of these terms can only have an exponent that is a natural number.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("There are different types of polynomials.\n")
                sleep(2)
                print("There are monomials, binomials, trinomials, and polynomials.")
                sleep(2)
                print("\nMonomials are polynomials that have only one term.")
                sleep(2)
                print("Binomials are polynomials that have two terms.")
                sleep(2)
                print("Trinomials are polynomials that have three terms.")
                sleep(2)
                print("And polynomials are polynomials that have four or more terms.")
                showImage("polynomials.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("Now, let's talk about the degree of a term.\n")
                sleep(2)
                print("The degree of a term is the sum of all of the exponents on the variables.")
                sleep(2)
                print("For example, the degree of -3xyz^5 is 7\nbecause x has an exponent of 1, y has an exponent of 1 and z has an exponent of 5.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("Now, let's talk about the degree of a polynomial.\n")
                sleep(2)
                print("The degree of a polynomial is the highest degree of any of the terms.")
                sleep(2)
                print("For example, the degree of 3x^2 + 4x + 1 is 2\nbecause the highest degree of any of the terms is 2.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()

                print("What is the degree of the term 3x^4y^2?")
                q6 = input("Answer: ")
                if q6 == "6":
                    sleep(1)
                    print("Correct!")
                    sleep(2)
                    print("\n")
                else:
                    sleep(1)
                    print("Sorry, but the degree of the term is 6.")
                    sleep(2)
                    print("\n")

                print("Question 2:")
                sleep(1)
                print("What is the degree of the polynomial 2x^3 + 5x^2 - 7x + 1?")
                q7 = input("Answer: ")

                if q7 == "3":
                    sleep(1)
                    print("Correct!")
                    sleep(2)
                    print("\n")
                else:
                    sleep(1)
                    print("Sorry, but the degree of the polynomial is 3.")
                    sleep(2)
                    print("\n")

                input("\nPress enter to continue...")
                clear()
                print("You are all caught up on lesson 2.1!")
                sleep(2)
                input("\nPress enter to go back to select a unit...")
                clear()
            elif lessonNum == "2.2":
                print("2.2")
            elif lessonNum == "2.3":
                print("2.3")
            elif lessonNum == "2.4":
                print("2.4")
            elif lessonNum == "2.5":
                print("2.5")
            elif lessonNum == "2.6":
                print("2.6")
            elif lessonNum == "2.7":
                print("2.7")
            elif lessonNum == "2.8":
                print("2.8")
            elif lessonNum == "2.9":
                print("2.9")
            elif lessonNum == "2.10":
                print("2.10")
            else:
                print("That isn't a lesson in the unit")
                sleep(3)
                clear()
        elif unitNum == "3":
            print("What lesson did you miss that you want to review (3.1-3.6)?")
            lessonNum = input("\nLesson number: ")

            if lessonNum == "3.1":
                clear()
                sleep(1)
                print("Lesson 3.1: Introduction to Data & Statistics\n")
                sleep(2)
                print("First, I am going to explain what is Data?\n")
                sleep(2)
                print("Data is a collection of facts, such as numbers, words, measurements, observations or just descriptions of things.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("There are two types of data.\n")
                sleep(2)
                print("There is Primary Data and Secondary Data.")
                sleep(2)
                print("\nPrimary data is data that is collected by you")
                sleep(2)
                print("Secondary data is data that is collected by someone else.\nSecondary data might be found in a book, newspaper, the internet, or by asking someone")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("Here is an example of primary data.\n")
                sleep(2)
                showImage("primaryData.png")
                sleep(2)
                input("\nPress enter to continue...")
                print("And here is an example of secondary data.\n")
                sleep(2)
                showImage("secondaryData.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("Lets talk about the difference between Numerical Data and Categorical Data.\n")
                sleep(2)
                print("Numerical Data is data that is expressed in numbers and involves a measurment or count.\n")
                sleep(2)
                print("On the other hand, cantegorial data is data that can be sorted by type or quality.\n")
                sleep(2)
                print("Categorial Data can be sorted into Nominal data or Ordinal data.")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("Nominal Data is classified without a natural order or rank (for eg. hair color or gender).\n")
                sleep(2)
                print("Whereas Ordinal Data has a predetermined or natural order (for eg. low, medium, high).\n")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                print("Here are some examples of Numerical Data.")
                sleep(2)
                showImage("numericalData.png")
                sleep(2)
                input("\nPress enter to continue...")
                print("And here are some examples of Categorical Data.")
                sleep(2)
                showImage("categorialData.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("Here is a little note on how to find the angle of a pie chart slice.\n")
                sleep(2)
                print("To find the angle you would need to do the number of responses of the catergory divided by the total number of responses and multiply by 360.")
                sleep(2)
                print("Here is an example image of a pie chart.\n")
                showImage("pieChart.png")
                sleep(2)
                input("\nPress enter to continue...")
                clear()
                hideImage()
                print("You are all caught up on lesson 3.1!")
                sleep(2)
                input("\nPress enter to go back to select a unit...")
                clear()
            elif lessonNum == "3.2":
                print("3.2")
            elif lessonNum == "3.3":
                print("3.3")
            elif lessonNum == "3.4":
                print("3.4")
            elif lessonNum == "3.5":
                print("3.5")
            elif lessonNum == "3.6":
                print("3.6")
            else:
                print("That isn't a lesson in the unit.")
                sleep(3)
                clear()
        else:
            print("That wasn't a unit number I can review")
            sleep(2)
            clear()

def showImage(imagePath):
    image_path = os.path.join(current_dir, "Images", imagePath)
    img = mpimg.imread(image_path)
    imgplot = plt.imshow(img)

    plt.show(block=False)

def hideImage():
    plt.close()

main()
input("")