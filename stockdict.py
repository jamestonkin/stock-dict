stockDict = {'AET': 'Aetna', 'AMZN': 'Amazon', 'AAL': 'American Airlines', 'AAPL': 'Apple', 'BA': 'Boeing'}

purchases = [ ('AET', 50, '3-mar-2017', 27),
('AMZN', 75, '17-feb-2017', 99),
('AAL', 20, '03-apr-2017', 59),
('AAPL', 200, '23-jan-2017', 230),
('BA', 125, '21-dec-2016', 134) ]

for purchase in purchases:
    ticker = purchase[0]
    full_company_name = stockDict[ticker]
    full_purchase_price = purchase[1] * purchase[3]

    print("I purchased {0} stock for ${1}".format(full_company_name, full_purchase_price))
