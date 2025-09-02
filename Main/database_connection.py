import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS colleagues (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department VARCHAR(100) NOT NULL
        );
        """
        cursor.execute(create_table_query)

        insert_query = "INSERT INTO colleagues (name, department) VALUES (%s, %s)"
        insert_values = [("Arjun", "Data Engineer"),("Gokul", "Linux Administrator"),("Pritha", "Logical DBA")]
        cursor.executemany(insert_query, insert_values)
        connection.commit()
        
        select_query = "SELECT * FROM colleagues"
        cursor.execute(select_query)
        results = cursor.fetchall()
        
        with open("database_output.txt","w") as file1:
            for row in results:
                print(row)
                file1.write(f"{row}\n")
    print("Data inserted and retrieved successfully.")
finally:
    connection.close()