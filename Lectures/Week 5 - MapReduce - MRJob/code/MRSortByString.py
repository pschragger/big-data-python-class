from mrjob.job import MRJob

class MRSortByString(MRJob):
    def mapper(self, _, line):
        """
        """
        l = line.split(' ')
        print l
        yield l[1], l[0]

    def reducer(self, key, val):
        yield key, [v for v in val][0]


if __name__ == '__main__':
    MRSortByString.run()