import xml.etree.ElementTree as ET
from os import getcwd

sets=['testing', 'training',  'validation']

classes = [ 'car', 'truck', 'van', 'longvehicle',
              'bus', 'airliner', 'propeller',
              'trainer', 'chartered',
              'fighter', 'others',
              'stairtruck', 'pushbacktruck',
              'helicopter', 'boat']


def convert_annotation(image_id, list_file):
    in_file = open('D:\GitHub上的SIMD\simd-master\simd\\annotations\pascal_voc\Annotations\%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        #difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = 'D:\GitHub上的SIMD\simd-master\simd'

for image_set in sets:
    image_ids = open('D:\GitHub上的SIMD\simd-master\simd\\%s.txt'%(image_set)).read().strip().split()
    #print(image_ids)
    list_file = open(wd+'\\data\\%s.txt'%( image_set), 'w')
    for image_id in image_ids:
        image_id = image_id.split('.')[1].split('/')[-1]
        print(image_id)
        list_file.write('C:\\Users\HTHT\Desktop\815\simd\images\%s.jpg'%( image_id))
        convert_annotation( image_id, list_file)
        list_file.write('\n')
    list_file.close()
