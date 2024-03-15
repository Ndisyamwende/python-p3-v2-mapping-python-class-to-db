from __init__ import CURSOR, CONN


class Department:
    def __init__(self, name, location):
        self.id = None  # Initialize id as None
        self.name = name
        self.location = location

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        CONN.commit()

    def save(self):
        CURSOR.execute("INSERT INTO departments (name, location) VALUES (?, ?)", (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, location):
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        if self.id is None:
            raise ValueError("Cannot update department without id.")
        CURSOR.execute("UPDATE departments SET name=?, location=? WHERE id=?", (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        if self.id is None:
            raise ValueError("Cannot delete department without id.")
        CURSOR.execute("DELETE FROM departments WHERE id=?", (self.id,))
        CONN.commit()