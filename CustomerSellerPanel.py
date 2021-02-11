import cgi

data = cgi.FieldStorage()

operator = data.getvalue("operator")

if operator == "Customer":
	print("<a href=\"CarsListCGICarsListCGI.html\">Back</a>")

if operator == "Seller":
	print("<a href=\"AdminFunctionalities.html\">Back</a>")

print("Content-Type: text/html")
print()
print("<!DOCTYPE HTML>")
print("<html>")
print("<head>")
print("<title>Pizza delivery location</title>")
print("</head>")
print("<body>")
print("<a href=\"CarsListCGI.html\"><b>Go to Store</b></a>")
print("</body>")
print("</html>")