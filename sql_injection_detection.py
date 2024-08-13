# import re
# import logging

# # Setup logging
# logging.basicConfig(filename='sql_injection_detection.log', level=logging.INFO)

# # List of basic SQL injection patterns to detect
# sql_injection_patterns = [
#     r"(?i)union select",       # Detects "UNION SELECT"
#     r"(?i)or\s+1=1",           # Detects "OR 1=1"
#     r"(?i)or\s+'1'='1'",       # Detects "OR '1'='1'"
#     r"(?i)or\s+\"1\"=\"1\"",   # Detects 'OR "1"="1"'
#     r"(?i)drop\s+table",       # Detects "DROP TABLE"
#     r"(?i)';--",               # Detects "';--"
#     r"(?i)' OR 'a'='a",        # Detects "' OR 'a'='a"
# ]

# def detect_sql_injection(query):
#     """
#     Detects if the SQL query contains any known SQL injection patterns.
#     """
#     for pattern in sql_injection_patterns:
#         if re.search(pattern, query):
#             logging.warning(f"Potential SQL injection detected: {query}")
#             return True
#     return False

# # Example usage: Simulating SQL query logging and detection
# def log_sql_query(query):
#     logging.info(f"SQL Query Executed: {query}")
#     if detect_sql_injection(query):
#         print("Warning: Potential SQL injection detected!")
#     else:
#         print("SQL query logged successfully.")

# # Simulated queries
# queries = [
#     # "SELECT * FROM users WHERE username = 'admin' AND password = 'password'",
#     # "SELECT * FROM users WHERE username = 'admin' OR '1'='1'",
#     # "SELECT * FROM products WHERE id = 1; DROP TABLE users; --",
#     "SELECT * FROM users WHERE username = 'admin' OR '1'='1'",
#     "SELECT * FROM products WHERE id = 1; DROP TABLE users; --",
# ]

# for query in queries:
#     log_sql_query(query)






import re
import logging

# Setup logging
logging.basicConfig(filename='sql_injection_detection.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define SQL injection patterns to detect
sql_injection_patterns = [
    r"(?i)union\s+select",   # UNION SELECT pattern
    r"(?i)or\s+1=1",         # OR 1=1 pattern
    r"(?i)or\s+'1'='1'",     # OR '1'='1' pattern
    r"(?i)--",               # SQL comment pattern
    r"(?i);",                # Semicolon to end SQL statements
    r"(?i)drop\s+table",     # DROP TABLE pattern
    r"(?i)';\s*--",          # Ending a query and commenting out the rest
    r"(?i)\";\s*--",         # Ending a query with a double quote and commenting out the rest
]

def detect_sql_injection(query):
    """
    Detect if the SQL query contains any known SQL injection patterns.
    """
    for pattern in sql_injection_patterns:
        if re.search(pattern, query):
            logging.warning(f"Potential SQL injection detected: {query}")
            return True
    return False

def log_sql_query(query):
    logging.info(f"SQL Query Executed: {query}")
    if detect_sql_injection(query):
        print("Warning: Potential SQL injection detected!")
    else:
        print("SQL query logged successfully.")

if __name__ == "__main__":
    # Get the SQL query from user input
    query = input("Enter the SQL query: ")
    log_sql_query(query)

