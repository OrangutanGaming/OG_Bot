import sqlite3
import cogs.glyphs.codes as codes

connect = sqlite3.connect("codes.db")
c = connect.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS codes"
#           "(platform text, code text, id text)")

PC = codes.PC

for i in PC:
    c.execute("INSERT INTO codes (platform, code) VALUES (?, ?)", ("PC", PC[i]))

connect.commit()
c.close()
connect.close()