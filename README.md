### PaloAltoProj

This project runs on Python 3.6 or higher (Python 3.8 is recommended).

Given a set of rules in a json file, and a "logs.txt" file, this script will create an output.txt file, which contains all of the logs that follows at least one of the given rules.

## Running PaloAltoProj
### Windows

1. git clone //gitlink
2. cd buildDotsProject
3. pip3 install -r requirements.txt
4. python3 main.py

### Mac OSX

1. git clone https://github.com/yoav130193/CodeProject.git
2. cd buildDotsProject
3. pip3 install -r requirements.txt
4. python3 main.py

## Additional Testing 

# How to add new rules file:
Replace the file rules.json in the Data folder with your own json file.
Each rule should be with the following format: 
```sh
{"field": string, "operation": "eq", "value": string}
```  
# How to add logs files:
Replace the file logs.txt in the Data folder with your own text file.
Each rule should be with the following format: 
```sh
{"message": string, "type": string, "severity": string, "id": string}
```  





