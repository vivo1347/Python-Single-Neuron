The goal of this project is to go over the concepts of Machine Learning from scratch. Initially, I began with a simple Perceptron (neuron).
Below is the architecture that I'm basing my code on.
![IMG_97DB125C944B-1](https://github.com/user-attachments/assets/b4a5ba94-4a26-472b-9e67-9d1ada27f1eb)
As you can see above the neuron takes in the inputs/feautures (x1,x2) which represent 0's or 1's in our example. The inputs will have weights associated with each independently (w1,w2). Then the product of the inputs with their associated weights are summed Z=w1*x1+w2*x2+b.
(b) is the bias associated with the neuron itself, one can imagine b as if it were the value needed for the neuron to fire....or the weights are like slopes and the biases are like the y-intercepts (If you are graphically inclined as I am :) ). Then, the result (z) is processed through an activation function (a) that aligns with the application of our project.....something that produces 1's and 0's! One easy function is the sigmoidal function! (I like this function because its derivative is kinda cool).


![IMG_F65F55C9A970-1](https://github.com/user-attachments/assets/8c03b0de-3866-4c0f-9200-4ca074aaea41) 

Now our neuron can take any numerical input (our 0's and 1's to represent False and Truth respectively) and squish the output (via the activation) function to anything between 0 and 1! This simple pass through the neuron will be called a forward pass!


Cool!.................but how on earth will it learn!!!! or how is this Machine Learning???? Well, according to a cool computer scientist called Tom M. Mitchell:  "A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E." In our example, task T is predicting if a case is True or False (1 or 0 respectively). Experience E is simply the training data alongside the correct outputs. As for performance measure P.....well that's what we'll discuss.
The way we can assess the performance of our neurons is by computing how "wrong" they are when they make a prediction! In our case the measure of that error will be a simple Mean Square Error function (MSE), that measures the average difference between the outputs of the neuron and the correct values from the data (Labels).


![IMG_24345C4EFB87-1](https://github.com/user-attachments/assets/63f3e085-522a-4840-b5dc-5b20b16dfec0)

This performance measure is what we'll refer to as "Cost" and the function that computes it is a Cost function, and the lower our cost function's output is.....the more correct our neuron's answers are!!!

The goal of learning now is to somehow lower the cost with respect to w1,w2, and b. In short, this is an optimization problem! Let us imagine a graph of the cost function with w as its independent variable thus C(w). In this case, finding the lowest C(w) is basically finding the global minima in that graph......in calculus terms dc/dw =0!!!!


![IMG_FE42EF02D70E-1](https://github.com/user-attachments/assets/31111b2f-ba9c-4c81-80d0-051ebf46adcd) 


Don't let the 2D nature of that graph trick you!!! our C(w) is multidimensional or simply C(w1,w2,b), just keep that in mind. considering that the MSE/cost function doesn't necessarily contain either of those variables calculus provides us with a tool to work back words...or back propogate to relate the change of the cost to any of the 3 variables! First, we note that C = 1/N SUM(a-y)^2, where (a) is the output of the neuron or the output of its activation function. Then we also know a=1/(1+e^-z) and Z=w1*x1+w2*x2+b. Thus, using the chain rule dc/dw1 = dc/da * da/dz * dz/dw1 giving us dc/dw1 =-2(y-a) * a(1-a) * x1. Now, going back to that comment about the multidimensionality of this case, dc/dw1 should be changed in a way where it goes towards a minima in its complicated landscape.....to ensure this one takes the "Gradient" and to be specific the negative of the gradient which follows the fastest path to decreasing the cost!......thus gradient descent!


![IMG_08EA41BFA7D3-1](https://github.com/user-attachments/assets/4ce07725-5d90-4153-9e72-2bbffa421491)

Now that we've worked backwards through the chain rule, and know we need the negative of that derivative accumulated over the training set, at the end of each predefined training iteration, the variables will be updated, w1+1 = w1 - 1/N * SUM(dc/dw), remembering that the negative comes from us seeking the negative gradient. The issue is that we might end up skipping over the minima as we descend towards it! Thus, we need to go towards the minima (keeping the direction/gradient as is) but make smaller steps towards it to ensure we don't skip it. This added smaller stepping approach is called our learning rate! This learning rate (u) can be some value between 0 and 1, so now our variable updates end up looking like this:
![IMG_7701F8EACC63-1](https://github.com/user-attachments/assets/76e12b53-55ce-4aae-a270-012a2bab4e71)






