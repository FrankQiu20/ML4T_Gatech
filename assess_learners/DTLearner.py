import numpy as np


class DTLearner(object):

    def __init__(self, leaf_size, verbose=False):
        self.leaf_size = leaf_size
        self.verbose = verbose

    def author(self):
        return 'yqiu322'

    def add_evidence(self, dataX, dataY):
        self.tree = self.build_tree(dataX, dataY)

    def query(self, points):
        result = []
        for point in points:
            node = 0
            while ~np.isnan(self.tree[node][0]):
                split_value = point[int(self.tree[node][0])]
                if split_value > self.tree[node][1]:
                    node = node + int(self.tree[node][3])
                else:
                    node = node + int(self.tree[node][2])
            pred = self.tree[node][1]
            result.append(pred)
        return np.asarray(result)


    def build_tree(self, dataX, dataY):
        dimx = dataX.shape[0]
        bfi = 0
        bcor = -1
        if dimx <= self.leaf_size:
            return np.asarray([np.nan, np.mean(dataY), np.nan, np.nan])

        if np.all(np.isclose(dataY, dataY[0])):
            return np.asarray([np.nan, dataY[0], np.nan, np.nan])

        dimxx = dataX.shape[1]

        for i in range(dimxx):
            std = np.std(dataX[:, i])
            if std == 0:
                cor = 0
            else:
                cor= np.corrcoef(dataX[:, i], dataY)[0, 1]
            if cor > bcor:
                bcor = cor
                bfi = i
        feature_index = bfi
        split_value = np.median(dataX[:, feature_index])

        left = dataX[:, feature_index] <= split_value
        left_m = left[0]
        meanY=np.mean(dataY)

        if np.all(np.isclose(left, left_m)):
            return np.asarray([np.nan, meanY, np.nan, np.nan])


        right = dataX[:, feature_index] > split_value

        left_tree = self.build_tree(dataX[left], dataY[left])
        right_tree = self.build_tree(dataX[right], dataY[right])

        if left_tree.ndim == 1:
            rot = np.asarray([feature_index, split_value, 1, 2])
        else:
            leftt = left_tree.shape[0] + 1
            rot = np.asarray([feature_index, split_value, 1, leftt])

        final_tree = np.row_stack((rot, left_tree, right_tree))

        return final_tree

if __name__ == "__main__":
    print("the secret clue is 'zzyzx'")