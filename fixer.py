def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def fixFile(name):
    with open(name, 'rb') as f:
        lin = ''
        fixed_csv = []
        headers = 'threadnumber, no, now, time, comment, subject, replies, uniqueips, name, id, country, imagefile'
        lines = [x.decode('utf8', 'replace').strip() for x in f.readlines()]
        lin = lines[0].strip()
        for lina in lines[1:]:
            if lina != "":
                splits = lina.split(',')
                if is_number(splits[0]) == False:
                    lin += lina + ' '
                else:
                    fixed_csv.append(lin)
                    lin = lina.strip()
        fixed_csv.append(lin)
    print('Fixed lines, exporting....')
    w = open('fixed_' + name, 'w')
    fmt = '%s\n'
    w.write(fmt % headers)
    for fx in fixed_csv:
        w.write(fmt % fx)
    w.close()
    print('exporting completed')

if __name__ == '__main__':
    fixFile('07-01-2018-15-00-00.csv')
