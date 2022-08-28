from math import e,pow
#Equation: 4x1+5x2-9=score
#weights are 4,5 and bias is -9, find the sigmoid(x) = 1/(1+e-x).

features=[(1,1),(2,4),(5,-5),(-4,5)]
def linear_func(features):
    for x in features:
        score= 4*x[0]+ 5*x[1]-9
        y = 1 / (1 + pow(e,- score))
        print("X",x,score,y)
 #call the function
linear_func(features)