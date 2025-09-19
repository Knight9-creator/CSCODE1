#Shopping variable declared so we have use the while loop.
shopping = "yes"

#Initialize basic Constants
COFFEE_QTY = 120
MUFFIN_QTY = 80
FRUIT_QTY = 60

while shopping == "yes":

    #Make these variables greater than the QTY of the above variables(items) so the while loops underneath this code works.
    user_buy_coffee = 255
    user_buy_muffin = 255
    user_buy_fruit = 255


    #Asks user for input
    while user_buy_coffee > COFFEE_QTY or user_buy_coffee < 0:
        user_buy_coffee = int(input(f"How many coffee cups would you like to order? We have {COFFEE_QTY} in stock: "))

    while user_buy_muffin > MUFFIN_QTY or user_buy_muffin < 0:
        user_buy_muffin = int(input(f"How many muffins would you like to order? We have {MUFFIN_QTY} in stock: "))

    while user_buy_fruit > FRUIT_QTY or user_buy_fruit < 0:
        user_buy_fruit = int(input(f"How many fruits would you like to order? We have {FRUIT_QTY} in stock: "))


    #Constants for Quantity
    COFFEE_QTY = 120 - user_buy_coffee #120
    MUFFIN_QTY = 80 - user_buy_muffin #80
    FRUIT_QTY = 60 - user_buy_fruit #60

    #Constants for Unit Costs
    COFFEE_UNIT_COST = 0.80
    MUFFIN_UNIT_COST = 1.10
    FRUIT_UNIT_COST = 1.25

    #Constants for Fees
    VENUE_FEE = 75.00
    PROCESSING_RATE = 0.029 #2.9%
    PROCESSING_FLAT = 0.30

    #Constants for Price
    COFFEE_PRICE = 2.50
    MUFFIN_PRICE = 3.50
    FRUIT_PRICE = 4.00

    #Variables that can calculate the gross revenue
    coffee_gross = user_buy_coffee * COFFEE_PRICE
    muffin_gross = user_buy_muffin * MUFFIN_PRICE
    fruit_gross = user_buy_fruit * FRUIT_PRICE

    #Variables that can calculate the cost
    coffee_cost = user_buy_coffee * COFFEE_UNIT_COST
    muffin_cost = user_buy_muffin * MUFFIN_UNIT_COST
    fruit_cost = user_buy_fruit * FRUIT_UNIT_COST

    #Find total gross revenue
    total_gross = coffee_gross + muffin_gross + fruit_gross

    #Find total item costs
    total_cost = coffee_cost + muffin_cost + fruit_cost

    #Find processing fees
    processing_fees = (total_gross * PROCESSING_RATE) + (PROCESSING_FLAT * (user_buy_coffee + user_buy_muffin + user_buy_fruit))

    #Find total_cash_out & total_cash_in
    total_cash_out = total_cost + VENUE_FEE + processing_fees
    total_cash_in = total_gross - processing_fees

    #Find net profit/loss & print a labeled summary with money formatting
    net_profit_or_loss = total_gross - total_cost - VENUE_FEE - processing_fees

    if net_profit_or_loss < 0:
        print("Net Loss: ", format(net_profit_or_loss, ".2f"))
    else:
        print("Net Profit: ", format(net_profit_or_loss, ".2f"))

    shopping = input("Would you like to shop again? (Yes / No): ").lower().strip(" ")





#README PARAGRAPH
#First, we made a variable called "shopping", that will be used for a while loop in case we need multiple customers.
#Then we initialize the constants, "COFFEE QTY, MUFFIN QTY, FRUIT QTY".
#Then we make variables, "user_buy_coffee, user_buy_muffin, user_buy_fruit", to use later. We make these variables greater than the amount of stock available to get an appropriate answer from the user in the while loop.
#Then, we declare all the constants that will be used in later calculations. 
#Then, we make variables to calculate the gross revenue of each item, as well as the cost of the items.
#Then we add all the gross values to find the "total_gross". As well as the "total_cost".
#Then we find the "total_cash_out" as well as the "total_cash_in".
#Then we calculate the "net_profit_or_loss".
#Based on the "net_profit_or_loss" variable, we determine whether the shop gained a net profit or a net loss.
#Finally we ask the user if they would like to shop again. If so, we repeat the loop.
