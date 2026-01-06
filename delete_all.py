import sqlite3
conn = sqlite3.connect('info.db')
conn.execute('DELETE FROM users')
conn.commit()
conn.execute('VACUUM')
conn.close()
print('All rows deleted from users')
