import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="test",
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        table_name=input("Enter table name :").strip()
        data_limit=int(input("Enter no. of entries: "))
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
        EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
        EmployeeName VARCHAR(100),
        Salary INT
        );
        """
        cursor.execute(create_table_query)

        insert_query = f"INSERT INTO {table_name}(EmployeeName, Salary) values (%s,%s)"
        for i in range(data_limit):
            employee_name=input("Enter employee name: ").strip()
            employee_salary=int(input("Enter employee salary: "))
            insert_values = (f"{employee_name}", employee_salary)
            cursor.execute(insert_query, insert_values)

        connection.commit()

        select_query = f"SELECT * FROM {table_name}"
        cursor.execute(select_query)
        results = cursor.fetchall()

        with open("output_file3.txt", "w") as file1:
            for row in results:
                print(row)
                file1.write(f"{row}\n")

    print("Data inserted and retrieved successfully")
except Exception as e:
    print(f"EXC: {type(e).__name__}: {e}")
    connection.close()