prefixes = ["?", "!.o", "o.!", "!o."]

def Prefix(quote = None):
    if quote == None:
        quote = '"'
    pPrefix = ""
    for prefix in prefixes:
        pPrefix += ('{}'.format(quote)+prefix+'{}'.format(quote)+", ")
    pPrefix = pPrefix[:-2]
    return pPrefix