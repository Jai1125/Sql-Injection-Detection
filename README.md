# Sql-Injection-Detection
 How the Code Works:-
 
1.Pattern Matching:
The script defines a list of regex patterns that correspond to common SQL injection techniques.
The detect_sql_injection function checks if any of these patterns exist in the SQL query.

2.Logging:
SQL queries and potential injection alerts are logged to a file named sql_injection_detection.log.

3.Simulation:
The script simulates running SQL queries, checking them for injection patterns, and logging the results.
