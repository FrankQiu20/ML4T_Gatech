""""""  		  	   		  	  		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
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
  		  	   		  	  		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		  	  		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		  	  		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  	  		  		  		    	 		 		   		 		  
"""  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  	  		  		  		    	 		 		   		 		  
import pandas as pd
import matplotlib.pyplot as plt
  		  	   		  	  		  		  		    	 		 		   		 		  
def author():  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  	  		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    return "yqiu322"  # replace tb34 with your Georgia Tech username.
  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def gtid():  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  	  		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    return 903758951  # replace with your GT ID number
  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  	  		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  	  		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  	  		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    result = False  		  	   		  	  		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  	  		  		  		    	 		 		   		 		  
        result = True
    return result  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def test_code():  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    win_prob = 18/38  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		  	  		  		  		    	 		 		   		 		  
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		  	  		  		  		    	 		 		   		 		  
    # add your code here to implement the experiments  		  	   		  	  		  		  		    	 		 		   		 		  
def gambling_sim(win_prob):
    episode_winnings = 0
    result = np.full((1001),80)
    spin = 0
    result[0] = 0
    while episode_winnings < 80 and spin < 1000:
        bet_amount = 1
        won = False
        while not won:
            spin = spin + 1
            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
            result[spin] = episode_winnings
    return result

win_prob = 18/38


def plot_exp1(win_prob):
   plt.ylim([-256,100])
   plt.xlim([0,300])
   plt.ylabel("Episode Winnings")
   plt.xlabel("spin")
   plt.title("Figure 1 - 10 simulation")
   for trial in range(1,11,1):
       episode_t = gambling_sim(win_prob)
       plt.plot(episode_t, label= '%s simulation' % trial)
   plt.legend()
   plt.savefig("Figure1.png")
   plt.clf()

plot_exp1(win_prob)


###Get data for figure 2 and 3 in Experiment 1
array_data = np.full((1000,1001),80)
for trial in range(1000):
    episode_t = gambling_sim(win_prob)
    array_data[trial] = episode_t

mean_data = np.mean(array_data,axis=0)
median_data =np.median(array_data,axis=0)
std_data = np.std(array_data,axis=0)
upper_bound = mean_data + std_data
lower_bound = mean_data - std_data
upper_bound_2 = median_data + std_data
lower_bound_2 = median_data - std_data

#### plot graph 2
plt.ylim([-256, 100])
plt.xlim([0, 300])
plt.ylabel("Episode Winnings")
plt.xlabel("spin")
plt.title("Figure 2")
plt.plot(mean_data,label = "mean")
plt.plot(upper_bound, label ="mean + std")
plt.plot(lower_bound,label= "mean - std")
plt.legend()
plt.savefig("Figure2.png")
plt.clf()


### plot graph 3
plt.ylim([-256, 100])
plt.xlim([0, 300])
plt.ylabel("Episode Winnings")
plt.xlabel("spin")
plt.title("Figure 3")
plt.plot(median_data,label = "median")
plt.plot(upper_bound_2, label ="median + std")
plt.plot(lower_bound_2,label= "median - std")
plt.legend()
plt.savefig("Figure3.png")
plt.clf()


#### experiment 2
def gambling_sim2(win_prob,bankroll):
    episode_winnings = 0
    result = np.full((1001),80)
    result[0] = 0
    spin = 0
    while episode_winnings < 80 and spin < 1000:
        won = False
        bet_amount = 1
        while not won and spin < 1000:
            spin = spin + 1
            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
                if episode_winnings == -bankroll:
                    result[spin:] = episode_winnings
                    return result
                current_amount = episode_winnings + bankroll
                if current_amount <= bet_amount:
                    bet_amount = current_amount
            result[spin] = episode_winnings
    return result

bankroll=256



###Get data for figure 4 and 5 in Experiment 2
array_data2 = np.full((1000,1001),-bankroll)
for trial in range(1000):
    episode_t = gambling_sim2(win_prob,bankroll)
    array_data2[trial] = episode_t

mean_data2 = np.mean(array_data2,axis=0)
median_data2 =np.median(array_data2,axis=0)
std_data2 = np.std(array_data2,axis=0)
upper_bound = mean_data2 + std_data2
lower_bound = mean_data2 - std_data2
upper_bound_2 = median_data2 + std_data2
lower_bound_2 = median_data2 - std_data2

#### plot graph 4
plt.ylim([-256, 100])
plt.xlim([0, 300])
plt.ylabel("Episode Winnings")
plt.xlabel("spin")
plt.title("Figure 4")
plt.plot(mean_data2,label = "mean")
plt.plot(upper_bound, label ="mean + std")
plt.plot(lower_bound,label= "mean - std")
plt.legend()
plt.savefig("Figure4.png")
plt.clf()


### plot graph 2
plt.ylim([-256, 100])
plt.xlim([0, 300])
plt.ylabel("Episode Winnings")
plt.xlabel("spin")
plt.title("Figure 5")
plt.plot(median_data2,label = "median")
plt.plot(upper_bound_2, label ="median + std")
plt.plot(lower_bound_2,label= "median - std")
plt.legend()
plt.savefig("Figure5.png")
plt.clf()


  		  	   		  	  		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  	  		  		  		    	 		 		   		 		  
    test_code()  		  	   		  	  		  		  		    	 		 		   		 		  

