import pandas as pd
import math

#loading training file
#Below is an example of an AND gate training set. To change it to an OR training set simply change the output to [0,1,1,1]
data = {
    "x1": [0, 0, 1, 1],  # First input
    "x2": [0, 1, 0, 1],  # Second input
    "y": [0, 0, 0, 1]    # Output (AND of x1 and x2)
}

# Create a DataFrame from the data
truth_table = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_name = "truths.xlsx"
truth_table.to_excel(file_name, index=False)

print(f"Truth table saved to {file_name}")


data =pd.read_excel(file_name)


print(data.head())


x1= data['x1']
x2= data['x2']
y = data['y']


#Initializing the variables that will be used in the learning algorithm.
Epoch = 0
w1=1
w2=1
b1=1
b2=1
cost =10 #Assume any large cost to work in the while loop initially
lr=7 #Learning rate, increasing it may increase the learning progress but it may lead to some jumping around the local minima of the cost landscape.
while cost>0.00001:
    N =0 #I could have set N to simply 4 but one can play around with this to make the learning stochastic
    sum_cost=0
    sum_dcost_dw1=0
    sum_dcost_dw2=0
    sum_dcost_b1=0
    sum_dcost_b2=0
    for i, row in data.iterrows():
        x1_i=row['x1']
        x2_i=row['x2']
        y_i=row['y']
        z=(x1_i*w1+b1)+(x2_i*w2+b2)
        a=(1/(1+math.exp(-z)))
        N +=1
#Below are the dc/dx (x being any optimizable variable) sums. This is the gradient descent algorithm.
        sum_cost += ((y_i-a)**2)
        sum_dcost_dw1 +=(-2*(y_i-a)*a*(1-a)*x1_i)
        sum_dcost_dw2 +=(-2*(y_i-a)*a*(1-a)*x2_i)
        sum_dcost_b1+=(-2*(y_i-a)*a*(1-a)*1)
        sum_dcost_b2+=(-2*(y_i-a)*a*(1-a)*1)
    cost = sum_cost/N
#Below is where the neuron's weights and biases are being updated...The Learning!!!
    w1 -=(lr*sum_dcost_dw1)/N
    w2-=(lr*sum_dcost_dw2)/N
    b1-=(lr*sum_dcost_b1)/N
    b2-=(lr*sum_dcost_b2)/N
    Epoch+=1
    print(f"Epoch: {Epoch}, cost: {cost}, w1: {w1},w2: {w2},b1: {b1}, b2: {b2}")

#Testing the neuron!
X1_ask= 0
X2_ask= 1
z_ask=(X1_ask*w1+b1)+(X2_ask*w2+b2)
a_ask= (1/(1+math.exp(-z_ask)))
print(f"a: {a_ask:.2f}")

    
