import os
import subprocess

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
                command = f"mysqlbinlog {binlog_path} > {sql_path}"
                subprocess.run(command, shell=True, check=True)
                print(f"Converted '{binlog_path}' to '{sql_path}'.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert '{binlog_path}': {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    convert_binlog_to_sql()
