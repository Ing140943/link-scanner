# Link Scanner

## Link Scanner Application

A Python program that scans a web page for hyperlinks.  It prints all the hyperlinks found on a page and then prints (again) any bad links.



Usage:
```
python link_scan.py  url-to-scan
```

Example:
```
cmd> python3 link_scan.py https://www.yahoo.com

http://info.yahoo.com/legal/us/yahoo/cc/en-us/
https://baseball.fantasysports.yahoo.com/b1/signup
https://beap.gemini.yahoo.com/mbclk
https://finance.yahoo.com/
https://gq.us.y.atwola.com/
https://help.yahoo.com/kb/account
https://login.yahoo.com/
...
https://search.yahoo.com/search
https://shopping.yahoo.com/
https://sports.yahoo.com/

Bad Links:
https://beap.gemini.yahoo.com/mbclk
https://sports.yahoo.com/
```