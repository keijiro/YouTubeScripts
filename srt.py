import sys

filename = sys.argv[1]
lines = list(map(str.strip, open(filename).readlines()))

while 'id="source"' not in lines[0]: lines.pop(0)

lines.pop(0)

count = 1
dur = 3
skip = False

for line in lines:
    if '</textarea>' in line: break
    if line in ('', '---') or line[0] == '>': continue
    if 'class:' in line: continue

    quote = '```' in line

    if not skip and not quote:
        t1 = count * dur
        t2 = (count + 1) * dur
        print(count)
        print('01:%02d:%02d,000 --> 01:%02d:%02d,000' % (t1 / 60, t1 % 60, t2 / 60, t2 % 60))
        print(line)
        print()
        count += 1

    skip = skip ^ quote
