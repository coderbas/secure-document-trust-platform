import sqlite3


DB_NAME = "database.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operation TEXT,
        filename TEXT,
        status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def log_operation(
    operation,
    filename,
    status
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO audit_logs
        (
            operation,
            filename,
            status
        )
        VALUES (?, ?, ?)
        """,
        (
            operation,
            filename,
            status
        )
    )

    conn.commit()
    conn.close()
def get_dashboard_stats():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM audit_logs
        WHERE operation='SIGN'
        """
    )

    signed_count = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM audit_logs
        WHERE operation='VERIFY'
        """
    )

    verified_count = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM audit_logs
        WHERE status='INVALID'
        """
    )

    tampered_count = cursor.fetchone()[0]
    cursor.execute("""
SELECT COUNT(*)
FROM audit_logs
WHERE operation='ENCRYPT'
""")

    encrypted_count = cursor.fetchone()[0]
    conn.close()

    return {
        "signed": signed_count,
        "verified": verified_count,
        "tampered": tampered_count,
        "encrypted": encrypted_count
    }
def get_audit_logs():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            timestamp,
            operation,
            filename,
            status
        FROM audit_logs
        ORDER BY id DESC
        """
    )

    logs = cursor.fetchall()

    conn.close()

    return logs