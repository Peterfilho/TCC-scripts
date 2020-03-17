import sqlite3
database = "locale.db"

conn = sqlite3.connect(database)
cur  = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, department TEXT, role TEXT, ra TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS positions (id INTEGER PRIMARY KEY, user_id INTEGER, search TEXT, result TEXT, locale TEXT, date DATE, FOREIGN KEY (user_id) REFERENCES users(id))")
#creating users to test
cur.execute("INSERT INTO `users` (`id`, `name`, `department`, `role`, `ra`) VALUES (1, 'Peterson', 'COGETI', 'Estagiario', '1630342'),(2, 'Hermano', 'COINT', 'Professor', '22222222')")
#creating locals associated to user Peterson
cur.execute("INSERT INTO `positions` (`id`, `user_id`, `search`, `result`, `locale`, `date`) VALUES (1, 1, '[-73 -73 -77 -53 -70 -78]', '[-64 -75 -78 -60 -76 -76]', 'B6A', '2020-03-11'), (2, 1, '[-100  -67  -63  -49  -53  -48]', '[-100  -70  -68  -55  -53  -55]', 'WC-M', '2020-03-18')")

conn.commit()
conn.close()