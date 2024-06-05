# Function that determines the max profit you can chieve by choosing a single day to buy one stock and another day in the future to sell that stock
# @author Manpreet Kaur

def max_stock_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    # Loop through each price in the price list and if a new lower price is found then update min_price
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price  # Calculates profit if the current price is sold at the min_price
            # If the calculated profit is greater than max_profit then it updates it
            if profit > max_profit:
                max_profit = profit
    
    return max_profit

# Test
prices = [7, 1, 5, 3, 6, 4]
print(max_stock_profit(prices))
