import sqlite3

conn = sqlite3.connect("instituto.db")

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS cursos(
        id INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        horas INTEGER NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS estudiantes(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL
    )
    """
)

#conn.execute(
#    """
#    INSERT INTO cursos (descripcion,horas)
#    VALUES ('Python de 0 a experto',40)
#    """
#)

#conn.commit()

print("\nCURSOS")
cursor = conn.execute("SELECT * FROM cursos")
for row in cursor:
    print(row)
    
cursor = conn.execute("SELECT * FROM estudiantes")
for fila in cursor:
    print (fila)