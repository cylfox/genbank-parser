
class Annotation:
    def __init__(self, species, gen_x1, gen_x2, strand, product, note):
        self.species = species
        self.gen_x1 = gen_x1
        self.gen_x2 = gen_x2
        self.strand = strand
        self.product = product
        self.note = note

    def __str__(self):
        return u'Species: %s | %s:%s(%s) | Product: %s | Note: %s' % (self.species, str(self.gen_x1), str(self.gen_x2),
                                                                      str(self.strand), self.product, self.note)


class Fragment:
    def __init__(self, Type, xStart, yStart, xEnd, yEnd, strand, block, length, score, ident, similarity, per_ident,
                 SeqX, SeqY):
        self.Type = Type
        self.xStart = int(xStart)
        self.yStart = int(yStart)
        self.xEnd = int(xEnd)
        self.yEnd = int(yEnd)
        self.strand = strand
        self.block = int(block)
        self.length = int(length)
        self.score = int(score)
        self.ident = int(ident)
        self.similarity = float(similarity)
        self.per_ident = float(per_ident)
        self.SeqX = int(SeqX)
        self.SeqY = int(SeqY)

    def __str__(self):
        return u'%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
            self.Type, str(self.xStart), str(self.yStart), str(self.xEnd), str(self.yEnd), self.strand,
            str(self.block), str(self.length), str(self.score), str(self.ident), str(self.similarity),
            str(self.per_ident), str(self.SeqX), str(self.SeqY))
