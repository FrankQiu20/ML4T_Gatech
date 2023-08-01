""""""  		  	   		  	  		  		  		    	 		 		   		 		  
"""  		  	   		  	  		  		  		    	 		 		   		 		  
Test a learner.  (c) 2015 Tucker Balch  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  	  		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  	  		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  	  		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  	  		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  		  		  		    	 		 		   		 		  
or edited.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  	  		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  	  		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  	  		  		  		    	 		 		   		 		  
"""  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
import math  		  	   		  	  		  		  		    	 		 		   		 		  
import sys  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
import numpy as np
import math
import LinRegLearner as lrl
import DTLearner as dtl
import RTLearner as rtl
import BagLearner as bl
import InsaneLearner as il
import matplotlib.pyplot as plt
import time
import sys


########
test_x, test_y, train_x, train_y = None, None, None, None

f = 'Data/Istanbul.csv'
datafile = 'Istanbul.csv'
data = np.genfromtxt(f, delimiter=",")

if datafile == "Istanbul.csv":
    data = data[1:, 1:]
train_rows = int(0.6 * data.shape[0])
test_rows = data.shape[0] - train_rows

train_x = data[:train_rows, 0:-1]
train_y = data[:train_rows, -1]
test_x = data[train_rows:, 0:-1]
test_y = data[train_rows:, -1]

leaf_range = range(1, 50)
in_sample_rsmes = []
out_sample_rsmes = []


### Experiment 1 ####
ismes = []
osmes = []

for leaf in range(1, 51):
    learner = dtl.DTLearner(leaf_size = leaf,verbose = False)
    learner.add_evidence(train_x, train_y)
    pred_in = learner.query(train_x)
    in_rmse = math.sqrt(((train_y - pred_in) ** 2).sum()/train_y.shape[0])

    pred_out = learner.query(test_x)
    out_rmse = math.sqrt(((test_y - pred_out) ** 2).sum()/test_y.shape[0])

    ismes.append(in_rmse)
    osmes.append(out_rmse)

xrange = range(1, 51)
plt.plot(xrange, ismes, label = "in sample")
plt.plot(xrange, osmes, label = "out sample")

plt.title("Figure 1 ")
plt.xlabel("Leaf Size")
plt.ylabel("RMSE")
plt.legend()
plt.savefig("figure1.png")
plt.close()


#######Experiment 2 ###


#### 15 bags
ismes = []
osmes = []

for leaf in range(1, 51):
    learner = bl.BagLearner(learner=dtl.DTLearner, kwargs={"leaf_size": leaf}, bags=15, boost=False,
                                verbose=False)
    learner.add_evidence(train_x, train_y)
    pred_in = learner.query(train_x)
    in_rmse = math.sqrt(((train_y - pred_in) ** 2).sum() / train_y.shape[0])

    pred_out = learner.query(test_x)
    out_rmse = math.sqrt(((test_y - pred_out) ** 2).sum() / test_y.shape[0])

    ismes.append(in_rmse)
    osmes.append(out_rmse)

xrange = range(1, 51)
plt.plot(xrange, ismes, label="in sample")
plt.plot(xrange, osmes, label="out sample")

plt.title("Figure 2")
plt.xlabel("Leaf Size")
plt.ylabel("RMSE")
plt.legend()
plt.savefig("figure2.png")
plt.close()


### 30 bags ####
ismes = []
osmes = []

for leaf in range(1, 51):
    learner = bl.BagLearner(learner=dtl.DTLearner, kwargs={"leaf_size": leaf}, bags=30, boost=False,
                                verbose=False)
    learner.add_evidence(train_x, train_y)
    pred_in = learner.query(train_x)
    in_rmse = math.sqrt(((train_y - pred_in) ** 2).sum() / train_y.shape[0])

    pred_out = learner.query(test_x)
    out_rmse = math.sqrt(((test_y - pred_out) ** 2).sum() / test_y.shape[0])

    ismes.append(in_rmse)
    osmes.append(out_rmse)

xrange = range(1, 51)
plt.plot(xrange, ismes, label="in sample")
plt.plot(xrange, osmes, label="out sample")

plt.title("Figure 3")
plt.xlabel("Leaf Size")
plt.ylabel("RMSE")
plt.legend()
plt.savefig("figure3.png")
plt.close()


#####Experiment 3##
###MAE
omae_dt = []
omae_rt = []

for leaf in range(1, 51):
    learner = dtl.DTLearner(leaf_size=leaf, verbose=False)
    learner.add_evidence(train_x, train_y)
    pred_out = learner.query(test_x)
    omae = np.mean(np.abs((np.asarray(test_y) - np.asarray(pred_out))))
    omae_dt.append(omae)

    learner = rtl.RTLearner(leaf_size=leaf, verbose=False)
    learner.add_evidence(train_x, train_y)
    pred_out = learner.query(test_x)
    omae = np.mean(np.abs((np.asarray(test_y) - np.asarray(pred_out))))
    omae_rt.append(omae)

xrange = range(1, 51)
plt.plot(xrange, omae_dt, label="Decision Tree")
plt.plot(xrange, omae_rt, label="Random Tree")
plt.title("Figure 4")
plt.xlabel("Leaf Size")
plt.ylabel("Mean Absolute Error")
plt.legend()
plt.savefig("figure4.png")
plt.close()


### running time ####

msize = train_x.shape[0]
time_dt = []
time_rt = []

for training_size in range(100, msize+1, 10):
    trainX = train_x[:training_size]
    trainY = train_y[:training_size]

    learner = dtl.DTLearner(leaf_size=1, verbose=False)
    start = time.time()
    learner.add_evidence(trainX, trainY)
    end = time.time()
    timet = end - start
    time_dt.append(timet)

    learner = rtl.RTLearner(leaf_size=1, verbose=False)
    start = time.time()
    learner.add_evidence(trainX, trainY)
    end = time.time()
    timet = end - start
    time_rt.append(timet)

xrange = range(100, msize + 1, 10)
plt.plot(xrange, time_dt, label="Decision Tree")
plt.plot(xrange, time_rt, label="Random Tree")
plt.title("Figure 5")
plt.xlabel("Trainning Sizes")
plt.ylabel("Trainning Time in second")
plt.legend()
plt.savefig("figure5.png")
plt.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python testlearner.py <filename>")
        sys.exit(1)
    inf = open(sys.argv[1])
    data = np.array(
        [list(map(float, s.strip().split(","))) for s in inf.readlines()]
    )

    # compute how much of the data is training and testing
    train_rows = int(0.6 * data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    train_x = data[:train_rows, 0:-1]
    train_y = data[:train_rows, -1]
    test_x = data[train_rows:, 0:-1]
    test_y = data[train_rows:, -1]

    print(f"{test_x.shape}")
    print(f"{test_y.shape}")

    # create a learner and train it
    learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner
    learner.add_evidence(train_x, train_y)  # train it
    print(learner.author())

    # evaluate in sample
    pred_y = learner.query(train_x)  # get the predictions
    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    print()
    print("In sample results")
    print(f"RMSE: {rmse}")
    c = np.corrcoef(pred_y, y=train_y)
    print(f"corr: {c[0, 1]}")

    # evaluate out of sample
    pred_y = learner.query(test_x)  # get the predictions
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    print()
    print("Out of sample results")
    print(f"RMSE: {rmse}")
    c = np.corrcoef(pred_y, y=test_y)
    print(f"corr: {c[0, 1]}")



