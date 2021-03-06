import sys
import re

infile = "z:\\win_fuse_smb\\vfs_je.c"
funcre = re.compile(r"static .+ \*?(.+)\(.*\)")
infuncre = re.compile(r"^\s*{\s*$")
if not funcre: exit(1)

infuncname = ''

#with open(infile) as f:
with sys.stdin as f:
    for line in f.readlines():
        if line[-1] == '\n': line = line[:-1]
        m = funcre.search(line)
        if m:
            infuncname = m.group(1)
        print line
        m = infuncre.search(line)
        if m:
            print "\tfprintf(stderr, \"In %s\\n\");" % infuncname
