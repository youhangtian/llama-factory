import json
import random

data_path = '/file/tian/data/coco'

with open(f'{data_path}/annotations/instances_train2017.json') as f:
    anno_data = json.load(f)

cate = {}
for c in anno_data['categories']:
    cate[c['id']] = c['name']

anno = {}
for a in anno_data['annotations']:
    id = a['image_id']
    arr = anno.get(id, [])
    arr.append(cate[a['category_id']])
    anno[id] = arr 

print('anno data len:', len(anno_data['annotations']))
print('anno len:', len(anno))

output_arr = []
for k, v in anno.items():
    d = {}
    d['messages'] = []
    d['images'] = []

    d['messages'].append({'content': '图片里有哪些目标？', 'role': 'user'})
    d['messages'].append({
        'content': f'图片里有{len(v)}个目标，分别是{v}',
        'role': 'assistant'
    })

    d['images'].append(f'{data_path}/train2017/{k:0>12}.jpg')

    output_arr.append(d)

print('output len:', len(output_arr))
print(random.choices(output_arr))

with open('data.json', 'w') as f:
    json.dump(output_arr, f, indent=2, ensure_ascii=False)

print('done')
