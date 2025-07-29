import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    print("Note: This script will create a table only with two columns and insert data into it. Please provide the data as prompted.")
    table_name = input("Enter the table name: ").strip()
    column_name1 = input("Enter the first column name: ").strip()
    column_name2 = input("Enter the second column name: ").strip()
    with connection.cursor() as cursor:
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            {column_name1} VARCHAR(100) NOT NULL,
            {column_name2} VARCHAR(100) NOT NULL
        );
        """
        cursor.execute(create_table_query)

        rows = int(input("Enter the number of rows to insert: "))
        if rows <= 0:
            raise ValueError("Number of rows must be greater than zero.")

        insert_query = f"INSERT INTO {table_name} ({column_name1}, {column_name2}) VALUES (%s, %s)"
        for _ in range(rows):
            name = input(f"Enter {column_name1}: ").strip()
            department = input(f"Enter {column_name2}: ").strip()
            cursor.execute(insert_query, (name, department))
        connection.commit()

        select_query = f"SELECT * FROM {table_name}"
        cursor.execute(select_query)
        results = cursor.fetchall()
        
        output_file = input("Enter the output file name (without extension): ").strip()
        with open(f"{output_file}.txt", "w") as file1:
            for row in results:
                print(row)
                file1.write(f"{row}\n")
    print("Data inserted and retrieved successfully.")
finally:
    connection.close()