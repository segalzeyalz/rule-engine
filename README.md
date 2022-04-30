# Rule Engine


## Installation
`docker build -t rule-engine .` <br>
`docker --env USER_ID={USERID HERE} --env PWD={PASSWORD HERE here} run -dp 8000:8000 --mount src="$(pwd)",target=/app,type=bind rule-engine` <br>
Then you can run the project!


## EndPoints
###http://127.0.0.1:8000/facts?tableName=<tableName>
<b>Expected response</b> <br>
1. The table name
2. Under the table name, show each of the 4 facts: the fact name and the fact
value: Number-of-rows, Number-of-indexes, has-primary-key, primary-key-count-columns
<br>
<b>Checks</b> <br>
1. Valid table name
2. User used the param "variable name"
###http://127.0.0.1:8000/rules?tableName=<tableName>
<b>Expected response</b> <br>
1. 3 rules, or error in case of table not exist/table not passed
<br>
<b>Checks</b> <br>
1. Valid table name
2. User used the param "variable name"


## Logging
<b>Format</b> <br/>
Time and messages; If time permitted I'd add: 
1. Generate request/procedure ID, and store it in DB
2. Header - os, user etc.

<b>INFO</b> <br/>
For data such as: query executed, args on each request, request succeeded

<b>Debug</b>
Creation of tables
<b>Exception</b>
Every exception, and auth issues;

## Decision-making
Actually, I've chosen some trade-offs here:
1. pretty-good architecture for easy changes, Over the best output; 
2. More time spent on Docker, less time on Logger.
3. I had some issues with one of the packages in Docker. I decided to dive in, instead of test

I realize there are bugs here and I didn't always make the right
decisions - but I learn as I go
## RoadMap - more rules based on real-world db related problems.
### More Logging options
1. Logging to a file with log rotation/connection service (such as opentelemtery)
2. Saving some of the logs in a DB
3. Log metadata 
4. Logger - singleton

### Rules
1. Rule engine that supports multiple operands and predicats
2. Rule engine that can response in real-tile on data change (webhooks/listeners from DB)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)