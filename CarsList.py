import cgi
from datetime import datetime

data = cgi.FieldStorage()

# Create an unordered (bulleted) list to display the toppings
cars = "<ul>"
price = 0
quantity = data.getvalue("nissanquantity")

# Check if the checkbox was checked, i.e. if it has a value
if data.getvalue("Audi e-tron"):
	# Using the value from the checkbox
	# Each bulleted list item must be enclosed in li tags
	cars += "<li>" + data.getvalue("Audi e-tron") + ":  $25000</li>"
	price += 25000

if data.getvalue("Toyota Avensis"):
	# Not using the value from the checkbox
	cars += "<li>Toyota Avensis:  $28600</li>"
	price += 28600
	quantity = 2

if data.getvalue("Suzuki KingQuad"):
	cars += "<li>Suzuki KingQuad:  $8000</li>"
	price += 8000
	quantity = 2

if data.getvalue("1931 Harley Davidson"):
	cars += "<li>1931 Harley Davidson:  $11000</li>"
	price += 11000
	quantity = 1

if data.getvalue("Nissan Leaf"):
	cars += "<li>Nissan Leaf:  $19000</li>"
	price += 19000


cars += "</ul>"

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Your Order</title>")
print("</head>")
print("<body>")
print("<h1>Your Order:</h1>")
print(cars)
print("Price:  ${0:.2f}<br/><br/>".format(price))
print("<a href=\"CarsListCGI.html\"><b>Return to Store</b></a><br></br>")
now = datetime.now()
dt_tm = now.strftime("<b>%d/%m/%Y %H:%M:%S</b>")
print("<b>Date of purchase: </b>", dt_tm[0:13])
print("<br>Time of purchase: ", now.strftime("%X"))
print("</body>")
print("</html>")