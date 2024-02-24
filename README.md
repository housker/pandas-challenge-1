# Columbia AI Module 3: Pandas Challenge 1

## Requirements

### Part 1: Explore the Data (30 points)
- [X] View the column names. (4 points)

- [X] Use the describe function. (4 points)

- [X] Correctly identify the category with the most entries. (4 points)

- [X] For the category with the most entries, correctly identify the subcategory with the most entries. (5 points)

- [X] Correctly identify the 5 clients with the most entries in the data. (5 points)

- [X] Store the client ids of those top 5 clients in a list. (4 points)

- [X] Display the total units (the qty column) that the client with the most entries ordered. (4 points)

### Part 2: Transform the Data (30 points)
- [X] Create a column that calculates the subtotal for each line using the unit_price and the qty. (6 points)

- [X] Create a column for shipping price. Assume a shipping price of $7 per pound for orders over 50 pounds and $10 per pound for items 50 pounds or under. (6 points)

- [X] Create a column for the total price using the subtotal and the shipping price along with a sales tax of 9.25%. (6 points)

- [X] Create a column for the cost of each line using unit cost, qty, and shipping price (assume the shipping cost is exactly what is charged to the client). (6 points)

- [X] Create a column for the profit of each line using line cost and line price. (6 points)

### Part 3: Confirm Your Work (15 points)
- [X] Confirm that Order ID 2742071 had a total price of $152,811.89. (5 points)

- [X] Confirm that Order ID 2173913 had a total price of $162,388.71. (5 points)

- [X] Confirm that Order ID 6128929 had a total price of $923,441.25. (5 points)

### Part 4: Summarize and Analyze (25 points)
- [X] Calculate the total revenue from each of the top 5 clients in Part 1. (5 points)

- [X] Create a summary DataFrame showing the totals for the top 5 clients with the following information: total units purchased, total shipping price, total revenue, and total profit. Sort by total profit. (5 points)

- [X] Format the data and rename the columns to names suitable for presentation. Currency should be in millions of dollars. (5 points)

- [X] Write a brief 2-3 sentence summary of your findings. (10 points)