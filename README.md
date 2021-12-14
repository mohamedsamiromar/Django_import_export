# Import data from file 

read data from excel or CSV file, using Pandas library.

## Abstract

the script will work when the user uploads the file, read the file using the pandas library, and will check the file formatting, It will xlsx or xls or CSV, and then start the processing of the file, if the file has an empty row the script will not select this is row and so on
Finally, the script will provide you with a log file
The index of blank lines and their positions, and the number of valid lines 

## Upload excel file
In the feature allowed uploading file

Method	| Path	| Description	 
------------- | ------------------------- :|

POST	| upload_file| upload your file|  





# Run Project
``` 
pip install -r requirements.txt
python manage.py runserver
``` 

## Contributions are welcome!
greatly appreciate your help. Feel free to suggest and implement improvements.

