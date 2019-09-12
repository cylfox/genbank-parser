from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import os
import pickle
from models import Annotation


static_path = os.getcwd() + '\\static\\'
annotations_path = static_path + '\\annotations\\'
output_path = static_path + '\\output\\'

annotation_file = [f.split('.')[0] for f in listdir(annotations_path) if isfile(join(annotations_path, f))]
print(annotation_file)
print(os.getcwd())

annotations = []

for genbank_file_name in listdir(annotations_path):
    if isfile(join(annotations_path, genbank_file_name)):
        print(genbank_file_name)
        species_name = genbank_file_name.split('.')[0]
        with open(annotations_path + genbank_file_name, 'r') as genbank_file, \
                open(output_path + 'pickle_' + species_name + '.o', 'wb') as output_file:
            # output_file.write(str(genbank_file_name) + '\n\n')
            total = 0
            sin_repetir = 0
            for index, record in enumerate(SeqIO.parse(genbank_file, 'genbank')):
                features = [feature for feature in record.features if feature.type == 'CDS']
                i = 0
                anterior_start = -1
                anterior_end = -1

                for feature in features:
                    # record.annotations['source']
                    # print feature.qualifiers
                    if anterior_start != int(feature.location.start) and \
                            anterior_end != int(feature.location.end):
                        sin_repetir += 1

                        try:
                            gene = feature.qualifiers['gene'][0]
                            #print(gene)
                        except KeyError:
                            gene = 'Unknown'
                            #print('!!!!!!!!!!!!!!!falta el gene')

                        try:
                            gene_synonym = feature.qualifiers['gene_synonym'][0]
                            #print('Sinonimos: ' + gene)
                        except KeyError:
                            gene_synonym = 'Unknown'
                            #print('Sin sinonimos')

                        try:
                            product = feature.qualifiers['product'][0]
                        except KeyError:
                            product = 'Unknown'
                            #print('!!!!!!!!!!!!!!!falta el producto')

                        try:
                            note = feature.qualifiers['note'][0].replace(
                                                 'Derived by automated computational analysis '
                                                 'using gene prediction method:', 'By')
                        except KeyError:
                            note = 'None'
                            #print('falta la nota')

                        try:
                            print('x1: %s x2: %s s: %s | gene: %s synonym: %s product: %s notes: %s' %
                                  (feature.location.start, feature.location.end, feature.location.strand, gene,
                                   gene_synonym, product, note))
                            ann = Annotation(species_name,
                                             int(feature.location.start),
                                             int(feature.location.end),
                                             int(feature.location.strand),
                                             product,
                                             note)
                            # output_file.write(str(ann) + '\n')
                            annotations.append(ann)
                        except Exception as e:
                            print('Exception: Cannot create annotation in position ' + str(i) + ' - e: ' + str(e))
                    anterior_start = int(feature.location.start)
                    anterior_end = int(feature.location.end)

                    i += 1

                total += i
                print('==> ANOTACIONES EN ' + record.id + ': ' + str(i))
            print('====> TOTAL ANOTACIONES: ' + str(total))
            print('====> TOTAL ANOTACIONES SIN REPETIR: ' + str(sin_repetir))
            print('====> SOBRAN: ' + str(total - sin_repetir))
            pickle.dump(annotations, output_file)


