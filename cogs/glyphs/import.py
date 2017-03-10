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
cPlatform = str(Platform)

# if Platform == PC:
#     cPlatform = "PC"
# elif Platform == XBox:
#     cPlatform = "XBox"
# elif Platform == PS4:
#     cPlatform = "PS4"

for i in Platform:
    c.execute("INSERT INTO codes (platform, code) VALUES (?, ?)", (cPlatform, i))

connect.commit()
c.close()
connect.close()