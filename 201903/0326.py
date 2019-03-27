# Daniel can run 3 miles per hour, how long can he ran for half hour? 
# Daniel has 100 dollars at Jan 1st which is a Sat, he spends 15 dollars everyday. What is the weekday that he will run out of money? 
# Use operaters and variable to calcualte these questions then print it out as following format "Daniel can run {} miles in {} hour. Daniel will ran out of monay on {} day"
halfHour = 3 / 2
print(f"Daniel can run {halfHour} miles in half an hour.")
amountOfDays = 100 // 15
dayThatIRunOut = amountOfDays + 1
aaa = "meh"
if dayThatIRunOut == 6 :
 aaa = "friday"
if dayThatIRunOut == 7 : 
 aaa = "saturday"
if dayThatIRunOut == 8 :
 aaa = "sunday"
print(f"Daniel will run out of money on {aaa}.")