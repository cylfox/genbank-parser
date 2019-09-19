from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import os
import csv
import pickle
from models import Annotation, Fragment, BlastResult

static_path = os.getcwd() + '\\static\\'
annotations_path = static_path + '\\pickle\\'
csv_path = static_path + '\\blast_results\\'
output_path = static_path + '\\output\\'


def filter_csv(csv_file_name, annotation_file_name):
    with open(csv_path + csv_file_name, 'r') as csv_file, \
            open(annotations_path + annotation_file_name, 'rb') as annotation_file, \
            open(output_path + 'output_' + csv_file_name, 'w') as output_file:

        # Primera parte:
        # filtrar los resultados para que no se repitan los mismos trozos
        visited_positions = []
        results = []

        # fragmentos
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            position = [row[8], row[9]]
            print(position)
            if position not in visited_positions:
                print('no está')
                visited_positions.append(position)

                blast_res = BlastResult(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                        row[10], row[11], row[12], row[13], row[14])
                results.append(blast_res)
                print(blast_res)
            line_count += 1
        print(str(line_count) + ' processed lines.')

        # 2a parte:
        # comparar con la bd y obtener resultados
        annotations = pickle.load(annotation_file)

        #para cada posiciones de la seq del resultado del blast se buscan las anotaciones contenidas en ellas
        for result in results:
            # que anotaciones están entre la s start y la s end?
            #

'''
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
'''

filter_csv('RM4VM3H5015-Alignment-HitTable.csv', 'pickle_HOMSA.o')
