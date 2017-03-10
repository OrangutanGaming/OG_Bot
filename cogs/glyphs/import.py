import sqlite3
import cogs.glyphs.codes as codes

connect = sqlite3.connect("codes.db")
c = connect.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS codes"
#           "(platform text, code text, id text)")

PC = codes.PC
XBox = codes.xBox
PS4 = codes.PS4

Platform = PC

for i in Platform:
    c.execute("INSERT INTO codes (platform, code) VALUES (?, ?)", ("{}".format(Platform), Platform[i]))

connect.commit()
c.close()
connect.close()