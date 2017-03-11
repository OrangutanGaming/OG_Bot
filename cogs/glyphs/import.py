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

for code in Platform:
    c.execute("INSERT INTO codes (platform, code) VALUES (?, ?)", (cPlatform, code))

connect.commit()
c.close()
connect.close()

# import rethinkdb as r
# r.connect("localhost", 28015).repl()
#
#
# PC = codes.PC
# XBox = codes.xBox
# PS4 = codes.PS4
#
# Platforms = PC
# cPlatform = str(Platform)
#
# for code in Platform:
#     r.db("OG_Bot").table("codes").insert([
#         {"platform": "{}".format(cPlatform), "code": "{}".format(Platform), "u-id": ""}]).run()