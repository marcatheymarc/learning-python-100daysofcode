# learning-python-100daysofcode
Here's the projects I've been making in the #100daysofcode challenge! I'm taking the class taught by Dr. Angela on Udemy

On Day 1, we did a simple band name generator that concatenated the input of user's "City" and "Pet Animal" into a _Band Name_ lol
  It was pretty fun, learned the simple idea behind getting "input" and "printing" things to the terminal. I unfortunately didn't think to save the file itself but the concept     behind it was simple enough that I shouldn't have to worry about reproducing it.
  
**Day 2**
Learning is getting me nice and motivated! Today the ending challenge was to compose a tip calculator which would take into account the following variables"
- How much did the total bill come up to
- How much (%) tip do you want to give
- How many people are splitting the total bill

I uploaded the file as tip-calculator.py on my github profile (and am writing this!) in hopes of getting more comfortable with the community's tools. Here's the line of code for the tip calculator should you wish to just use it for yourself :D <3

# CODE BEGINS BELOW
#Tip Calculator

# This print function prints the first line which welcomes the user to the tip calculator, you can change what's between the "" to display text of your choosing!
print("Welcome to my wonderful tip calculator!")

# Here we ask the user to input the bill total that will be split. This input is then marked as a float; floats are simply numbers that include decimals! That way, if the user enters cents, they'll be considered. This now defined "bill_total" will be used later.
bill_total = float(input("What was the total of the bill to split? $"))

# Here we ask the user to input percentage tip they would like to give. Instead of using float, the int(integer) function is being used. This would eliminate any decimal numbers. The float function could be used instead if we'd like to consider decimal percentages.
tip_percentage = int(input("What percentage tip would you like to give your lovely wait staff? %"))

# This line asks the user to input the number of people who are splitting the bill. The int function is being used simply because there's no such thing as "half people".
people = int(input("And how many are splitting the bill? "))

# Above, we just defined the "bill_total", the "tip_percentage" and the "people"; Now all we need is to math it all together!

# Let's define "total_to_split" with a bill of 200$ and 15% tip

# Since we want decimals in this number, we'll use the float function. This new float will be defined by (AND FOLLOWING PEMDAS):
# - Firstly, the "tip_percentage" will get calculated first; so e.g. an input of "15" would result in 15 / 100 = 0.15
# - Second, the "bill_total" gets multiplied by this previous equation: 200 * 0.15 = 30
# - Third, this now defined tip amount gets added to the "bill_total" once more
# - Finally, this amount gets split between the number of people sharing the bill
total_to_split = float((bill_total * (tip_percentage/100) + bill_total) / people)

# Given that the above float might have a very lengthy decimal sequence, we define here the "rounded_total_each", which .formats to 2floats after the "." the "total_to_split" (I think?) This part was quickly shown by the teacher to ensure 2 decimals would always show even if they were .00
rounded_total_each = "{:.2f}".format(total_to_split,2)

# Last but not least, we print it all for the user :D <3
print(f"Sounds like a fun night! You each owe ${rounded_total_each} on the bill; Have a Safe Drive Home <3")
# **CODE ENDS ABOVE**
