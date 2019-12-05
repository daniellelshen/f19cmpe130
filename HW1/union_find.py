"""
Danielle Shen
CMPE 130 F19

"""
# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression

import time
import random
import matplotlib.pyplot as plt


class UF(object):
    """Union Find class

    """

    def __init__(self):
        self.id = []
        # array counting number of elements in the tree rooted at its index
        # checks which tree is bigger or smaller
        self.sz = []

    def qf_init(self, N):
        """initialize the data structure

        """
        for x in range(N):
            self.id.append(x)
        self.sz = [1] * N

    def qf_union(self, p, q):
        """Union operation for Quick-Find Algorithm.

        connect p and q. You need to
        change all entries with id[p] to id[q]
        (linear number of array accesses)

        """
        # sets the value of p id to q id
        idp = self.id[p]
        idq = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == idp:
                self.id[i] = idq

    def qf_connected(self, p, q):
        """Find operation for Quick-Find Algorithm.
        simply test whether p and q are connected

        """
        # checks the id of p and q are the same
        return self.id[p] == self.id[q]

    def root(self, i):
        # finds the root by going through the parents
        while i != self.id[i]:
            i = self.id[i]
        return i

    def qu_union(self, p, q):
        """Union operation for Quick-Union Algorithm.
         connect p and q.

         """
        # p root points to q root
        root_p = self.root(p)
        root_q = self.root(q)
        self.id[root_p] = root_q

    def qu_connected(self, p, q):
        """Find operation for Quick-Union Algorithm.
         test whether p and q are connected

         """
        # Checks if root of p and q are the same
        return self.root(p) == self.root(q)

    def wqu_union(self, p, q):
        """Union operation for Weighted Quick-Union Algorithm.
         connect p and q.

         """
        rootp = self.root(p)
        rootq = self.root(q)
        if rootp == rootq:
            return
        if self.sz[rootp] < self.sz[rootq]:
            self.id[rootp] = rootq
            self.sz[rootq] += self.sz[rootp]
        else:
            self.id[rootq] = rootp
            self.sz[rootp] += self.sz[rootq]

    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected

         """
        # Checks if root of p and q are the same
        return self.root(p) == self.root(q)

    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

         """
        rootp = self.root(p)
        rootq = self.root(q)
        self.id[rootp] = rootq

    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        # Checks if root of p and q are the same
        return self.root(p) == self.root(q)

    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.

         """
        rootp = self.root(p)
        rootq = self.root(q)
        if self.sz[rootp] < self.sz[rootq]:
            self.id[rootp] = rootq
            self.sz[rootq] += self.sz[rootp]
        else:
            self.id[rootq] = rootp
            self.sz[rootp] += self.sz[rootq]

    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        # Checks if root of p and q are the same
        return self.root(p) == self.root(q)


if __name__ == "__main__":

    # iteration
    set_szs = [10 ** 1, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
    timing = []

    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.qf_union(rp, rq)

        t1 = time.time()
        # print (t0, t1)
        total_time = t1 - t0
        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, color='blue', label='quick-find union')

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!

    timing = []

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # quick-find connected
            inodes.qf_connected(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)
    plt.plot(set_szs, timing, color='green')

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # quick-union union
            inodes.qu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, color='red')

    timing = []

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # quick union connected
            inodes.qu_connected(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, color='magenta')

    timing = []

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # weighted quick union union
            inodes.wqu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, color='cyan')

    timing = []

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # weighted quick union connected
            inodes.wqu_connected(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, color='yellow')

    timing = []

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # path compressed quick union union
            inodes.pqu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, color='black')

    timing = []

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # path compressed quick union connected
            inodes.pqu_connected(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, color='#ffd6b1')

    timing = []

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # weighted path compressed quick union union
            inodes.wpqu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)

    plt.plot(set_szs, timing, color='#cdff00')

    timing = []

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            # weighted path compressed quick union connected
            inodes.wpqu_connected(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)
        print(total_time)

    print(timing)
    plt.plot(set_szs, timing, color='#ccccff')

    plt.legend(['qf union', 'qf connect', 'qu union', 'qu connect',
                'wqu union', 'wqu connect', 'pqu union', 'pqu connect',
                'wpqu union', 'wpqu connect'], loc='upper left')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('i = 1, 2, 3, 4, 5, 6, 7, 8, 9')
    plt.ylabel('some numbers')
    plt.show()
