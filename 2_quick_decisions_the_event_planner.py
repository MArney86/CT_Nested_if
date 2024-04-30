#Task 1: Code Correction

attendees = int(input("Enter number of attendees: ")) #typecasting needed for number inputs
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2: Venue Selection

recommendations = "We recommend requesting audio equipment and a projector" if attendees > 100 else "we have no equipment recommendations at this time" #recommend additional facilities like "audio system" or "projector" based on the number of attendees.
print(recommendations)

#Task 3: Catering Choices

veggie = input("Do you want vegetarian food?(yes/no) ")#Ask the user if they want "vegetarian" food.
caterers = "Veggie Delight Caterers" if veggie == "yes" else "Gourmet Meals Caterer" # Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
print("We recommend " + caterers + " for any catering needs you may have.")