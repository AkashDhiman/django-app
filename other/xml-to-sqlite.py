import xml.etree.ElementTree as ET
import sqlite3

tree = ET.parse('bioinformatics_posts_se.xml')
root = tree.getroot()

conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()


def sqlite_insert(conn, table, row):
  # to escape single quote character in input
    raw_values = list(row.values())
    values = []
    for value in raw_values:
        values.append(value.replace("'", "''"))

  # query
    cols = ', '.join("'{}'".format(col) for col in row.keys())
    vals = ', '.join("'{}'".format(col) for col in values)
    sql = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table, cols, vals)
    conn.cursor().execute(sql)
    print("Id", row['Id'], "written to database")


for child in root:
    sqlite_insert(conn, 'posts_post', child.attrib)

conn.commit()
print("all changes commited")
conn.close()
