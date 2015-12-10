tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

for i in ["/","-","|","\\","|"]:
    print "%s\r" % i,

gang_a = "gang_a is\awhat??"
gang_b = "gang_b is\bwhat??"
gang_f = "gang_f is\fwhat??"
gang_u = "gang_u is \u559c what??"
gang_U = "gang_U is \U559c6b22 what??"
gang_v = "gang_v is\vwhat??"
gang_ooo = "gang_ooo is \110 what??"
gang_xhh = "gang_xhh is \x43 what??"

print gang_a
print gang_b
print gang_f
print gang_u.decode("raw_unicode_escape")
print gang_U.decode("raw_unicode_escape")
print gang_v
print gang_ooo
print gang_xhh
