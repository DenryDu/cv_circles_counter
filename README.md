## A coin or circle counter for python using OpenCV
## 1.coin_counter_test_to_find_good_parameter.py

A simple coin counter for python 2.7 using OpenCV.<br><br>
load image -> convert to grey scale -> apply gaussian blur -> apply canny edge detection -> find contours -> draw contours -> count the number of contours -> thus, count the number of coins.<br><br>
Replace "money.jpg" at the top of the program with your own coin images and have a play with the parameters values.<br><br>
![alt tag](http://i.imgur.com/WkcFwzb.png?1)<br><br>
![alt tag](http://i.imgur.com/ZTVaWan.png?1)<br>
(Shows 7 coins, but infact there are 14).<br><br>
Rhys Dunn 2015
