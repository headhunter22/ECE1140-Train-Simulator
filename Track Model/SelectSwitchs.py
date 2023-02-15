import sqlite3

def selectSwitches(db, line, section, block):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT infrastructure FROM blueline WHERE (section IS " + section + ") AND (block_number IS " + block + ")")

    rows = cur.fetchall()
    
    return rows

print(selectSwitches('blueline.db', 'BLUE', 'A', '5'))