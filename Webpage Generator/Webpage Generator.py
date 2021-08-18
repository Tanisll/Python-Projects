# We need to import the "webbrowser" module in order for this code to work.
import webbrowser
# This will overwrite any content contained within the HTML file.
# That way, any changes made here will also change the website.
c = open("SummerSale.html", "w")
c.write("<html>\n"
        "   <body>\n"
        "      <h1>Stay tuned for our amazing summer sale!</h1>\n"
        "   </body>\n"
        "</html>")
c.close()


# This next code is to view how the HTML looks within the Python program.
# By using the "r" tag, we will not be able to change any of the information
# inside the HTML file. Only view it.
c = open("SummerSale.html", "r")
print(c.read())



# This will open the HTML file in the default web browser and with a new tab
# if that browser is already open.
url = "SummerSale.html"
webbrowser.open_new_tab(url)
