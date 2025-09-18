 #🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available




customer_name = "Jake"
passes_bought = 3
tokens_per_pass = 30
pass_price = 15.00
tokens_per_games = 3

#Calculate
total_tokens = passes_bought * tokens_per_pass
total_cost = passes_bought * pass_price
games_available = total_tokens // tokens_per_games

print("=====ARCADE DAY PASS=====")
print("Name: ", customer_name)
print("Passes: ",passes_bought)
print("Total tokens: ",total_tokens)
print("Total cost: $",total_cost)
print("Games available: ",games_available)



