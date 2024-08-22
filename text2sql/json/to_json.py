import csv 
import json 
import random

from table_info import TABLE_INFO

prompt = '''
你是一个数据库分析专家，可以根据提供的数据库表结构，使用正确的sql代码来回答用户问题。
数据库表结构如下：
{TABLE_INFO}
用户问题如下:
{question}
sql代码:
'''

def get_d(row):
    d = {}
    d['db_id'] = 'database'
    d['input'] = ''
    d['history'] = []

    question = row[4]
    sql = row[5]
    # if '今年' in question:
    #     if random.random() < 0.4:
    #         question = question.replace('今年', '')
    d['instruction'] = prompt.format(TABLE_INFO=TABLE_INFO, question=question)
    d['output'] = sql
    return d 

output = []

arr = []
with open('../newqs/newq.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        d = get_d(row)
        arr.append(d)
arr = arr * 3
output.extend(arr)
print('output len:', len(output))

arr = []
with open('../newqs/newqs.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        d = get_d(row)
        arr.append(d)
output.extend(arr)
print('output len', len(output))

random.shuffle(output)
print(output[0])
print(output[1])

with open('data_all.json', 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print('done')
