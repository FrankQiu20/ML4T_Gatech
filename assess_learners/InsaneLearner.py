import numpy as np
import BagLearner as bl
import LinRegLearner as lrl
class BagLearner(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.learners = [bl.BagLearner(learner=lrl.LinRegLearner, kwargs={}, bags=20, boost=False, verbose=False)] * 20
    def author(self):
        return "yqiu322"  # replace tb34 with your Georgia Tech username
    def add_evidence(self, dataX, dataY):
        for learner in self.learners:
            learner.add_evidence(dataX, dataY)
    def query(self, points):
        predY = []
        for mylearner in self.learners:
            predY.append(mylearner.query(points))
        predY = np.array(predY)
        return predY.mean(axis=0)
if __name__ == "__main__":
    print("the secret clue is 'zzyzx'")
