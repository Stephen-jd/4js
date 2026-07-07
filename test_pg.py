import psycopg2

passwords = ["", "postgres", "admin", "1234", "password", "root"]
db_name = "4js website"
user = "postgres"

success = False
for pwd in passwords:
    try:
        conn = psycopg2.connect(dbname=db_name, user=user, password=pwd, host="localhost")
        print(f"SUCCESS: Connected with password '{pwd}'")
        conn.close()
        success = True
        break
    except psycopg2.Error as e:
        pass

if not success:
    print("FAILED: None of the common passwords worked.")
