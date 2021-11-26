import pyshorteners
url = input("Enter your long url")
s = pyshorteners.Shortener().tinyurl.short(url)
 print("your Short URL is -->",s)

 