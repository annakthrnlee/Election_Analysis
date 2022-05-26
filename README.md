# Election_Analysis

## Project Overview:
I worked with Tom to summarize the tasks needed to complete the election audit. We also discussed the information needed by the Colorado Board of Elections.
### Tasks
To ensure that my final Python script would deliver the following information when the script is run: 
1. Total number of votes cast.
2. A complete list of candidates who received votes.
3. Total number of votes each candidate received.
4. Percentage of votes each candidate won.
5. The winner of the election based on popular vote.

## Resources:
### Resources Folder
Data source: election_results(3).csv

Analysis.py: incldues the final analysis of the election and county vote results.
### PyPoll.py 
Includes all of the codes I used to determine the election results. 
### PyPoll_Challenge.py 
Includes all of the codes I used to determine the election results and the voter turnout results for each county. 
### Software
Python version 3.7.6, Visual Studio Code 1.67.2

## Results: 
The analysis of the election contained the following:
- There were 369,712 total votes in the election. 
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23% (85,213) of the total votes casted.
    - Diana DeGetter received 73.8% (272,892) of the total votes casted.
    - Raymon Anthony Doana received 3.1% (11.606) of the total votes casted.
- The winner of the election was:
    - Diana DeGetter who received 73.8% (272,892) of the total votes casted.

## Challenge Overview:
The election commission has requested some additional data to complete the audit. I provided a written analysis of the election audit for the election commission, including the new results and a clearly written overview of your methods. 
### Tasks
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Results:
The analysis of the election audit concering vote turnout for each county contained the following:
- The counties were:
    - Jefferson
    - Denver
    - Arapahoe
- The total county votes were:
    - Jefferson accounted for 10.5% (38,855) of the total votes.
    - Denver accounted for 82.8% (306,055) of the total votes.
    - Arapahoe accounted for 6.7% (24,801) of the total votes.
- The largest county turnout was:
    - Denver which accounted for 82.8% (306,055) of the total votes casted. 
  
## Summary: 
This proposal outlines how this script can be used, with some modifications, for any election. 
#### It should be made apparent that the first edit should be made by selecting different csv files for different elections. 

For starters, one editing option could be to eliminate the "county_options" line and replace it with, for example, "state_options". With more editing, you would be able to create a new dictionary that corresponded with specific or all states if necessary. Another editing option that could be done would include changing or even adding specific lines that could dictate how voters chose to cast their votes. To determine how voters chose to vote would also include another file that analyzed all votes casted and the options available/chosen on an individual level by state (or county). 


