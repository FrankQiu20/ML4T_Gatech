import numpy as np

class BagLearner(object):
    def __init__(self, learner, kwargs, bags, boost = False, verbose =False):
        self.verbose = verbose
        self.boost = boost
        self.learners = []
        for i in range(bags):
            self.learners.append(learner(**kwargs))

    def author(self):
        return "yqiu322"

    def add_evidence(self, dataX, dataY):
        dimx =dataX.shape[0]
        for learner in self.learners:
            bag_num = np.random.choice(range(dimx), dimx, replace=True)
            bag_y = dataY[bag_num]
            bag_x = dataX[bag_num]
            learner.add_evidence(bag_x, bag_y)

    def query(self,points):
        out = []
        for learner in self.learners:
            out.append(learner.query(points))
        out = np.array(out)
        return out.mean(axis=0)
        #sum(out) / len(out)
if __name__ == "__main__":
    print("the secret clue is 'zzyzx'")