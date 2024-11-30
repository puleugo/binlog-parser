import os
import subprocess

# https://dev.mysql.com/doc/refman/8.4/en/mysqlbinlog.html
# This is Row Based Binlog Converter
# If you want to convert Statement Based Binlog, you can remove --base64-output=DECODE-ROWS
def convert_binlog_to_sql(binlog_dir="./binlog", sql_dir="./sql"):
    # Ensure the directory exists
    if not os.path.exists(binlog_dir):
        print(f"Directory '{binlog_dir}' does not exist.")
        return

    # List all files in the directory
    for file_name in os.listdir(binlog_dir):
        if file_name.startswith("binlog.") and not file_name.endswith(".sql"):
            binlog_path = os.path.join(binlog_dir, file_name)
            sql_path = os.path.join(sql_dir, f"{file_name}.sql")

            try:
                # Run mysqlbinlog command to convert the binlog to sql
                command = f"mysqlbinlog --base64-output=DECODE-ROWS -v {binlog_path} > {sql_path}"
                subprocess.run(command, shell=True, check=True)
                print(f"Converted '{binlog_path}' to '{sql_path}'.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert '{binlog_path}': {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    convert_binlog_to_sql()
