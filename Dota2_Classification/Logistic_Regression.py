
import numpy as np
import pylab
import math
import random
import Generate_xy

xy_list=Generate_xy.generate_xy()

x=xy_list[0]

y=xy_list[1]

feature_dimen=len(x[0])

sample_num=len(x)

print sample_num

t=list()
for i in range(feature_dimen):
        t.append(0)

grad=list()
for i in range(feature_dimen):
        grad.append(0)

dev=list()

def h(i):
        z=sum([t[k]*x[i][k] for k in range(feature_dimen)])

        """
        for k in range(feature_dimen):
                z=z+t[k]*x[i][k]
        """
        
        h=1/(1+math.exp(-z))
        
        return h

def gradient_descent(alpha, x, y, ep, max_iter,h):
    converged = False
    iter=0
    m=len(x) # number of samples
    n=len(t) # number of theta

    # total error, J(theta)
    J=sum([y[i]*math.log(h(i))+(1-y[i])*math.log(1-h(i)) for i in range(m)])
    
    # Iterate Loop
    while not converged:
        #for each training sample, compute the gradient (d/d_theta J(theta))
        for k in range(n):
            grad[k]=sum([(h(i)-y[i])*x[i][k] for i in range(m)])
        for k in range(n):
            t[k]-=alpha*grad[k]

        e = sum([y[i]*math.log(h(i))+(1-y[i])*math.log(1-h(i)) for i in range(m)])
        #print(e)
        
        dev.append(e) # obtain dev for plotting

        if abs(J-e) <= ep:
            converged= True

        J = e #update error
        iter +=1   # update iter

        if iter == max_iter:
            converged = True

    return t

if __name__=='__main__':

    gradient_descent(0.00000000001, x, y, 0.00001, 10000000,h)

    print('theta0 = %s theta1 = %s theta2 = %s') %(t[0], t[1], t[2])

    marker_y=[h(i) for i in range(sample_num)]

    marker_x=[sum([t[k]*x[i][k] for k in range(feature_dimen)]) for i in range(sample_num)]

	
    for i in range(sample_num):
            marker_y[i]=1/(1+math.exp(-marker_x[i]))
		
    pylab.plot(marker_x,marker_y,'ro')
    #pylab.axis([-200,200,-5,5])
    pylab.show()
    
    #pylab.plot(dev)
    #pylab.show()
    print "Done!"
            
    
