# Import data from file 

read data from excel or CSV file, using Pandas library and insert it in datebase 

## Abstract

the script will work when the user uploads the file, read the file using the panda's library, will check the file formatting is xlsx or xls or CSV, and start the processing of the file, if the file has an empty row the script will not select these rows and so on.

Last but not least, the script will provide you with a log file
The index of blank lines and their positions, and the number of valid lines 

## Upload excel file
In the feature allowed uploading file

Method	| Path	| Description	
------------- | ------------------------- | ------------- 
POST	| upload_file	| Upload Your File 





# Run Project
``` 
pip install -r requirements.txt
python manage.py runserver
``` 

## Contributions are welcome!
greatly appreciate your help. Feel free to suggest and implement improvements.

