import sqlite3

def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def save_message(user_id, username, message, timestamp):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (user_id, username, message, timestamp) VALUES (?, ?, ?, ?)', (user_id, username, message, timestamp))
    conn.commit()
    conn.close()


def get_user_messages(user_id):
    conn = sqlite3.connect('messages.db')
    print('userid',user_id)
    cursor = conn.cursor()
    cursor.execute('SELECT message FROM messages WHERE user_id = ?', (user_id,))
    messages = cursor.fetchall()
    conn.close()
    return messages
