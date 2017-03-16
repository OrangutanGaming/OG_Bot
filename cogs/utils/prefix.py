prefixes = ["!.o", "o.!", "!o.", "o!"]

def Prefix(quote = None):
    if not quote:
        quote = '`'
    pPrefix = ""
    for prefix in prefixes:
        pPrefix += ("{}".format(quote)+prefix+"{}".format(quote)+", ")
    pPrefix = pPrefix[:-2]
    return pPrefix