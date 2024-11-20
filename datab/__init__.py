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
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            role TEXT DEFAULT 'user'
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

def save_llm_message(user_id, username, message, timestamp):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (user_id, username, message, timestamp, role) VALUES (?, ?, ?, ?, ?)', (user_id, username, message, timestamp, "assistant"))
    conn.commit()
    conn.close()


def get_user_messages(user_id):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT message, role FROM messages WHERE user_id = ?', (user_id,))
    messages = cursor.fetchall()
    conn.close()
    return messages

def message_count(user_id):
    if not user_id is int:
        print(user_id, type(user_id))
        try:
            user_id = int(user_id)
        except:
            raise TypeError("user_id must be an integer")
    conn = sqlite3.connect('messages.db')  
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM messages WHERE user_id = ? AND role = \'user\'', (user_id,))
    count = cursor.fetchone()[0]
    conn.close()
    return count
