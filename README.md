# Dota2_BigData
Python App for Dota2 Big Data Analysis. Software Environment: python 2.7 - python(x,y)2.7.6.1 distribution, Mysql 5.0+, libcurl 

The goal of this project is to design a python application for Dota2 BigData analysis purpose.

The project is split into two parts, data mining and data analysis.

Currently, I have provided my source code for downloading match history data into a mysql database.

Data source: Steam Database

WebApi Used:
(GetMatchHistory)   https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v001/?key=<key>&start_at_match_id=<match_id>

(GetMatchDetails)   https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v001/?key=<key>&match_id=<match_id>


If you are interested, check the following two links:

Api Online Resources
Steam Official Documation:
https://wiki.teamfortress.com/wiki/WebAPI


Dota2 Development Forum:
http://dev.dota2.com/showthread.php?t=58317
