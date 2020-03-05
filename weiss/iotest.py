import logging

logging.basicConfig(level=logging.INFO)

with open('/Users/siwei/sync_tb_job_log.sql', 'w') as f:
    f.write('hello,world')
    logging.info('success!')

with open('/Users/siwei/sync_tb_job_log.sql', 'r') as f:
    # for line in f.readlines(8):
    #     logging.info(line)

    logging.info(f.read())

with open('/Users/siwei/helloworld.txt','a+') as file:
    file.writelines('hello,world,create file\n')

from io import StringIO

f = StringIO()
f.writelines('hello')
f.writelines('world')
f.writelines('welcome')
# logging.info(f.getvalue())

f.flush()
f = StringIO('Hello!\nHi!\nGoodbye!')
line = f.readline()
while line != '':
    logging.error(line)
    line = f.readline()

from io import BytesIO
f=BytesIO()
f.write('中文'.encode('gbk'))
print(f.getvalue())

exit()
