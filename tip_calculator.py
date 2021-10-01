print("Welcome to my wonderful tip calculator!")

bill_total = float(input("What was the total of the bill to split? "))

tip_percentage = int(input("What percentage tip would you like to give your lovely wait staff? "))

people = int(input("And how many are splitting the bill? "))

total_to_split = float((bill_total * (tip_percentage/100) + bill_total) / people)

rounded_total_each = round(total_to_split,2)

print(f"Sounds like a fun night! You each owe ${rounded_total_each} on the bill; Have a Safe Drive Home <3")