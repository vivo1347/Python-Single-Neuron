import pandas as pd
import math

#loading training file

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



Epoch = 0
w1=1
w2=1
b1=1
b2=1
cost =10
lr=7
while cost>0.00001:
    N =0
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
        sum_cost += ((y_i-a)**2)
        sum_dcost_dw1 +=(-2*(y_i-a)*a*(1-a)*x1_i)
        sum_dcost_dw2 +=(-2*(y_i-a)*a*(1-a)*x2_i)
        sum_dcost_b1+=(-2*(y_i-a)*a*(1-a)*1)
        sum_dcost_b2+=(-2*(y_i-a)*a*(1-a)*1)
    cost = sum_cost/N
    w1 -=(lr*sum_dcost_dw1)/N
    w2-=(lr*sum_dcost_dw2)/N
    b1-=(lr*sum_dcost_b1)/N
    b2-=(lr*sum_dcost_b2)/N
    Epoch+=1
    print(f"Epoch: {Epoch}, cost: {cost}, w1: {w1},w2: {w2},b1: {b1}, b2: {b2}")


X1_ask= 0
X2_ask= 1
z_ask=(X1_ask*w1+b1)+(X2_ask*w2+b2)
a_ask= (1/(1+math.exp(-z_ask)))
print(f"a: {a_ask:.2f}")

    
