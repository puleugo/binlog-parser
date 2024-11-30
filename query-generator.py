shouldRows = set(['game_name1', 'game_name2'])
query = '''
### UPDATE `db_name`.`table_name`
### WHERE
###   @1='game_name'
###   @22=1
###   @23=2
###   @24=3
###   @25=4
###   @26=5
###   @27=6
###   @28=7
###   @29=8
###   @30=10
...
'''


def parse_query_value(result, buffer):
    result += "UPDATE `db_name`.`table_name`"
    rowId = buffer.pop('1')
    for key, value in buffer.items():
        if key == '1':
            continue
        if key == '22':
            result += f" SET `COLUMN_NAME1`={value}"
        if key == '23':
            result += f", `COLUMN_NAME2`={value}"
        if key == '24':
            result += f", `COLUMN_NAME3`={value}"
        if key == '25':
            result += f", `COLUMN_NAME4`={value}"
        if key == '26':
            result += f", `COLUMN_NAME5`={value}"
        if key == '27':
            result += f", `COLUMN_NAME6`={value}"
        if key == '28':
            result += f", `COLUMN_NAME7`={value}"
        if key == '29':
            result += f", `COLUMN_NAME8`={value}"
        if key == '30':
            result += f", `COLUMN_NAME9`={value}"

    result += f" WHERE `ID`={rowId};\n"
    return result


def get_sql_query(query):
    rowsCount = 0
    result = 'START TRANSACTION;\n'
    parsedRows = set()

    buffer = dict()
    for queryLine in query.split("\n"):
        # remove ###, whitespace
        queryLine = queryLine.replace("###", "").strip()
        # print(queryLine)
        if queryLine.startswith('@'):  # 변수라면
            key = queryLine.split('=')[0].replace('@', '')
            value = queryLine.split('=')[1]
            buffer[key] = value
        if queryLine.startswith('UPDATE') and len(buffer) > 0:  # 업데이트 쿼리의 시작점이라면
            # 이미 parsedRows에 있는 row라면
            if buffer['1'] in parsedRows:
                print('중복되어 무시함.', buffer['1'])
                buffer.clear()
                continue
            parsedRows.add(buffer['1'].replace("'", ""))
            result = parse_query_value(result, buffer)
            # print(buffer)

            rowsCount += 1
            buffer.clear()

    else:
        parsedRows.add(buffer['1'])
        result = parse_query_value(result, buffer)
        buffer.clear()
        result += 'COMMIT;'
        rowsCount += 1
        print(f"Total rows: {rowsCount}")
        print(f"누락된 데이터({len(shouldRows.difference(parsedRows))}): {shouldRows.difference(parsedRows)}")
        print(f"복구된 데이터({len(parsedRows)}): {parsedRows}")

    return result

print(get_sql_query(query))
