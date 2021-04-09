# Requirements
Ubuntu 18.04+
Python 3.6+
Selenium
Chrome Driver
# How to use
Prepare a telegram bot to notify you.
You can use 2 server, the first server collects the data from VNDirect, and second server checks if first server works or not.
Because Stock Exchange Website I know, use Javascript to get and show data (React), I cant use only BeautifulSoup and Requests. So the solution I used is Selenium and Chrome Driver, then uses BeautifulSoup to get exactly what I need (to have smaller data size)
You can set 1st server cronjob to run collect data every 10 minutes, to get data from Monday - Friday. And 2nd server to check if data exists, after 7 minutes.

The idea is, save timedone file, and give public access, like http://123.456.78.90/timedone , and then use 2nd server to get that file content, to check timestamp (last time to get data successfully). If there's something wrong, and 1st server cant get data, 2nd server will use Telegrram bot to notify you!