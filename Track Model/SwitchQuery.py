import sqlite3

def selectSwitches(line, block):
    conn = sqlite3.connect('tracklayout.db')
    cur = conn.cursor()
    cur.execute("SELECT infrastructure FROM tracklayout WHERE block_number IS '" + block + "'")

    rows = cur.fetchall()
    
    return str(rows)