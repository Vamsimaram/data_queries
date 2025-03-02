## testDBs
Assignment specific files should be stored in this folder.  
This folder must contain the following files:
1. `create_empty_tables_mysql.sql` must contain the sql commands to create empty tables
2. `view_names.json` must contain the views belonging to the answer in the format:
    ```
    {
       "views": [
            <view_name1>,
            <view_name1>,
            ...
            ]
    }
    ```
3. `db*.json` files such as `db1.json` must contain tables and their elements in the following format:
   ```
       {
          "db_name": <db_name>,
          "tables": {
               <table1>: [
                       {                               # tuple 1
                           <attrib1>: <val1>,          
                           <attrib2>: <val2>,
                           ...
                       },
                       {                               # tuple 1
                           <attrib1>: <val1>,
                           <attrib2>: <val2>,
                           ...
                       },
                       ...
                   ],
               <table2>: ...,
               ...
          }
           
       }
   ```
4. `correct_answers.json` must contain the right answers to check against student answers
