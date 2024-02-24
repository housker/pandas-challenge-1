import re
import pandas as pd

df = pd.read_csv('./transformed.csv')
summary_1_df = pd.read_csv('./summary_1.csv')
summary_2_df = pd.read_csv('./summary_2.csv')

def search_file(file, pattern):
    content = open(file).read()
    if re.search(pattern, content, re.MULTILINE):
        return True
    return False


### Part 1: Explore the Data (30 points)
def test_part_1():
    assert search_file("module_4_challenge.ipynb", rf"df\.columns") == True, "View the column names. (4 points)"

    assert search_file("module_4_challenge.ipynb", rf"df.describe\(\)") == True, "Use the describe function. (4 points)"

    assert search_file("module_4_challenge.ipynb", rf"df\[\'category\'\]\.value_counts\(\)\.head\(3\)") == True, "Correctly identify the category with the most entries. (4 points)"

    assert search_file("module_4_challenge.ipynb", rf"df\.loc\[df\[\'category\'\] == \'consumables\', \'subcategory\'\]\.value_counts\(\)\.head\(1\)") == True, "For the category with the most entries, correctly identify the subcategory with the most entries. (5 points)"

    assert search_file("module_4_challenge.ipynb", rf"df\[\'client_id\'\]\.value_counts\(\)\.head\(5\)") == True, "Correctly identify the 5 clients with the most entries in the data. (5 points)"

    assert search_file("module_4_challenge.ipynb", rf"top_clients = df\[\'client_id\'\]\.value_counts\(\)\.head\(5\)\.index\.to_list\(\)") == True, "Store the client ids of those top 5 clients in a list. (4 points)"

    assert search_file("module_4_challenge.ipynb", rf"df\.loc\[df\[\'client_id\'\] == 33615\]\[\'qty\'\]\.sum\(\)") == True, "Display the total units (the qty column) that the client with the most entries ordered. (4 points)"


### Part 2: Transform the Data (30 points)
def test_part_2():
    assert search_file("module_4_challenge.ipynb", rf"df\[\'line_subtotal\'\] = df\[\'unit_price\'\] \* df\[\'qty\'\]") == True, "Create a column that calculates the subtotal for each line using the unit_price and the qty. (6 points)"

    assert search_file("module_4_challenge.ipynb", rf"df\[\'shipping_price\'\] = df\[\'total_weight\'\]\.apply\(lambda x: x \* 7 if x > 50 else x \* 10\)") == True, "Create a column for shipping price. Assume a shipping price of $7 per pound for orders over 50 pounds and $10 per pound for items 50 pounds or under. (6 points)"

    assert search_file("module_4_challenge.ipynb", rf"df\[\'line_price\'\] = \(\(df\[\'line_subtotal\'\] \+ df\[\'shipping_price\'\]\) \* 1.0925\)\.round\(2\)") == True, "Create a column for the total price using the subtotal and the shipping price along with a sales tax of 9.25%. (6 points)"

    assert search_file("module_4_challenge.ipynb", rf"df\[\'line_cost\'\] = \(df\[\'unit_cost\'\] \* df\[\'qty\'\]\) \+ df\[\'shipping_price\'\]") == True, "Create a column for the cost of each line using unit cost, qty, and shipping price (assume the shipping cost is exactly what is charged to the client). (6 points)"

    assert search_file("module_4_challenge.ipynb", rf"df\[\'line_profit\'\] = df\[\'line_price\'\] - df\[\'line_cost\'\]") == True, "Create a column for the profit of each line using line cost and line price. (6 points)"


### Part 3: Confirm Your Work (15 points)
def test_part_3():
    assert df.loc[df['order_id'] == 2742071, 'line_price'].sum().round(2) == 152811.89, "Confirm that Order ID 2742071 had a total price of $152,811.89. (5 points)"

    assert df.loc[df['order_id'] == 2173913, 'line_price'].sum().round(2) == 162388.71, "Confirm that Order ID 2173913 had a total price of $162,388.71. (5 points)"

    assert df.loc[df['order_id'] == 6128929, 'line_price'].sum().round(2) == 923441.25, "Confirm that Order ID 6128929 had a total price of $923,441.25. (5 points)"


### Part 4: Summarize and Analyze (25 points)
def test_part_4():
    top_clients = df['client_id'].value_counts().head(5).index.to_list()
    expected_totals = [8377308.52, 10259514.79, 9743794.36, 12906550.87, 82268892.02]
    for e in zip(top_clients, expected_totals):
        assert df.loc[df['client_id'] == e[0], 'line_price'].sum().round(2) == e[1], "Calculate the total revenue from each of the top 5 clients in Part 1. (5 points)"

    assert summary_1_df['client_id'].isin(top_clients).all(), "Create a summary DataFrame showing the totals for the top 5 clients with the following information: total units purchased, total shipping price, total revenue, and total profit. Sort by total profit. (5 points)"

    expected_cols = ['Client ID', 'Units', 'Shipping', 'Total Revenue', 'Total Cost','Total Profit']
    currency_cols = ['Shipping', 'Total Revenue', 'Total Cost','Total Profit']
    assert summary_2_df.columns.isin(expected_cols).all() and summary_2_df[currency_cols].map(lambda x: isinstance(x, str) and x.startswith('$') and x.endswith('M')).all().all(), "Format the data and rename the columns to names suitable for presentation. Currency should be in millions of dollars. (5 points)"

    assert search_file("module_4_challenge.ipynb", rf"Consumables, furniture, and software are the most profitable .* in revenue\."
) == True, "Write a brief 2-3 sentence summary of your findings. (10 points)"
