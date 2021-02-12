import cgi

data = cgi.FieldStorage()

operator = data.getvalue("operator")
customer = data.getvalue("Customer")
seller = data.getvalue("Seller")

if operator == "Customer":
	print("<a href=\"CarsListCGI.html\">Go to Store</a>")

if operator == "Seller":
	print("<a href=\"AdminFunctionalities.html\">Go to Admin Panel</a>")

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Operator Selection</title>")
print("</head>")
print("<body>")
if data.getvalue("Customer") == 1:
	print("<a href=\"CarsListCGI.html\"><b>Go to Store</b></a>")
else:
	print("<a href=\"AdminFunctionalities.html\"><b>Go to Admin Panel</b></a>")
print("</body>")
print("</html>")