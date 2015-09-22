from mrjob.job import MRJob

class MRSortByInt(MRJob):
    def mapper(self, _, line):
        """
        """
        l = line.strip('\n').split()
        yield '%01d'%int(l[1]), l[0]

    def reducer(self, key, val):
        yield int(key), int(list(val)[0])


if __name__ == '__main__':
    MRSortByInt.run()