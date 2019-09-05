from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import os
import csv
import pickle
from models import Annotation, Fragment

static_path = os.getcwd() + '\\static\\'
annotations_path = static_path + '\\pickle\\'
csv_path = static_path + '\\csv\\'
output_path = static_path + '\\output\\'


def overlap_percentage(x1, x2, y1, y2):
    intersection = min(x2, y2) - max(x1, y1)
    min_len = min(x2 - x1, y2 - y1)
    per = intersection / min_len
    if per < 0:
        per = 0
    #y = abs((min(x2, y2) - max(x1, y1)) / min(x2 - x1, y2 - y1))
    #x = abs((min(y2, x2) - max(y1, x1)) / min(y2 - y1, x2 - x1))
    return per


def filter_csv(csv_file_name, annotation_file_name):
    with open(csv_path + csv_file_name, 'r') as csv_file, \
            open(annotations_path + annotation_file_name, 'rb') as annotation_file, \
            open(output_path + 'output_' + csv_file_name, 'w') as output_file:

        # cargar anotaciones
        annotations = pickle.load(annotation_file)
        fragments = []

        # cargar csv
        # header
        csv_header = csv.reader(csv_file)
        for index, row in enumerate(csv_header):
            if index >= 14:
                break
            else:
                output_file.write(str(row[0]) + '\n')

        # fragmentos
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 14:
                # output_file.write(str(row) + '\n')
                print('Column names are ' + ", ".join(row))
            elif line_count > 14:
            # if line_count == 0:
                # print('Column names are ' + ", ".join(row))
                # line_count += 1
            #else:
                frag = Fragment(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                row[11], row[12], row[13])
                # print(frag)
                fragments.append(frag)
            line_count += 1
        print(str(line_count) + ' processed lines.')

        i = 0
        #  y manejar csv
        for frag in fragments:
            for ann in annotations:
                # overlap percentage
                overlap_per = overlap_percentage(float(ann.gen_x1), float(ann.gen_x2), float(frag.xStart), float(frag.xEnd))
                if overlap_per >= 0.5:
                    print(overlap_per)
                # check overlap
                if (ann.gen_x1 <= frag.xStart <= ann.gen_x2) or \
                        (frag.xStart <= ann.gen_x1 <= frag.xEnd) and \
                        overlap_per >= 0.8:
                    # if frag.xStart >= ann.gen_x1 and frag.xEnd <= ann.gen_x2:
                    output_file.write(str(frag) + '\n')
                    # print(str(ann) + ' overlap ' + str(frag))
                    i += 1
                    if i % 10000 == 0:
                        print(str(i) + ' fragments ovelapped.')
                    break
        print(str(i) + ' fragments ovelapped.')


filter_csv('homo_sapiens_chrX-pan_troglodytes_chrX-5000-95.csv', 'pickle_HOMSA.o')
