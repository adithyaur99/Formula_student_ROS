import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class compute:
	def _init_(self):
        	self.res = None
        	self.y = None
        	self.x = None
	def copy_exp(self,res,x,y):
		self.res=res
		self.x=x
		self.y=y
	def draw(self,title='Plot 1', xlabel='', ylabel=''):
    		fig, ax = plt.subplots()
        	ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
        
        	ax.plot(self.x, self.y)

        # finally plot
        	plt.show()





def gen():
    t = [float(i)/10 for i in range(-100, 100, 1)]
    return t

def lamb(t):

	res=3 * np.pi * np.exp(-1 * (5 * np.sin(2 * np.pi * t)))
	return res

def main():
    t = np.array(gen())
    y=lamb(t)
    plot=compute()
    plot.copy_exp(res=t,x=t,y=y)
    plot.draw(title='KTHFS Exercise 2 Plotter', xlabel='time(s)', ylabel='Data')

main()