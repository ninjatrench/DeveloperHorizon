from controller.conf import dbname

with open('%s' % dbname, 'w') as f:
    f.write('{}')
    f.close()