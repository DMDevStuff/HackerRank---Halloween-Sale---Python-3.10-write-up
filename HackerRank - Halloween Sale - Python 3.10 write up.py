##    https://www.hackerrank.com/challenges/halloween-sale/problem
##
##    You wish to buy video games from the famous online video game store Mist.
##
##    Usually, all games are sold at the same price, p dollars. However, they
##    are planning to have the seasonal Halloween Sale next month in which you
##    can buy games at a cheaper price. Specifically, the first game will cost
##    p dollars, and every subsequent game will cost d dollars less than the
##    previous one. This continues until the cost becomes less than or equal
##    to m dollars, after which every game will cost m dollars. How many games
##    can you buy during the Halloween Sale?

##### ##### ##### #####

#   changed variable names

#   p = current_price
#   d = discount
#   m = price_floor
#   s = remaining_money

##### ##### ##### #####

#   O(n)
#   n = remaining_money
#   In the most extreme case the current_price and price_floor will
#   start at 1 causing us to loop (remaining_money / 1) times.

#   Idea:
#       This is straight forward iterate and check with some book keeping.
#       As long as we have more money than the current price of a game
#       we buy one, then update the price and our remaining money.

#   Algo:
#       1. Initiate a variable to keep track of the total games purchased => O(1)
#       2. Initiate a while loop that continues as long as we have atleast
#           as much money as the current price => O(remaining_money)
#               A. Subtract the current price from our remaining money => O(1)
#               B. Subtract the discount from the current price => O(1)
#               C. We need to make sure that the current price is not
#                   below the price floor, so we set current price to
#                   the max of current price and price floor => O(1)
#               D. Increment the number of games purchased by one => O(1)
#       3. Return the number of games purchased => O(1)

def howManyGames(current_price, discount, price_floor, remaining_money):
    
    number_of_games_purchased = 0
    
    while remaining_money >= current_price:
        
        remaining_money -= current_price
        current_price -= discount
        current_price = max(price_floor, current_price)
        number_of_games_purchased += 1
        
    return number_of_games_purchased
