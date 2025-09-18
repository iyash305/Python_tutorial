# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"


total_race_time = float(input("Please enter the total race time in seconds: "))
pit_stops = int(input("How many pit stops were made? "))
avg_pit_time = float(input("Please tell us about the average pit stop duration in seconds: "))

total_pit_time = pit_stops * avg_pit_time
percent_of_race_spent = (total_pit_time / total_race_time) * 100
percent_of_race_spent = round(percent_of_race_spent, 2)

print("-----Pit Stop Summary-----")
print(f"Total pit stop in seconds is {total_pit_time}")
print(f"Percentage of race time spent in pits: {percent_of_race_spent:}%")


if percent_of_race_spent > 5:
    print("You need a new pit crew")