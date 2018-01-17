from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import pylab
import numpy as np


import csv

totalcount = 0
x = []
y = []
with open("Loan_Training.csv") as in_file:
	reader = csv.DictReader(in_file)
	for fields in reader:		
		totalcount += 1
		x_a = []		
		y.append(int(fields["Status (Fully Paid=1, Not Paid=0)"]))

		for i in fields:

			


			if (i == "Debt-To-Income Ratio"):
				v = (50 - float(fields[i].strip('%')))
				x_a.append(v)

			elif (i == "FICO Range"):
				if (len(fields[i]) != 0):
					m = fields[i].split('-')
					v = (600 - int(m[0]) + int(m[1])) / 2
				else:
					v = 0
				x_a.append(v)

			elif (i == "Revolving Line Utilization"):
				if (len(fields[i]) != 0):
					v = float(fields[i].strip('%'))
				else:
					v = 0
				x_a.append(v)

			elif (i == "Home Ownership"):
				if (len(fields[i]) != 0):
					if (fields[i] == "OWN"):
						v = 1
					elif (fields[i] == "MORTGAGE"):
						v = 0
					elif (fields[i] == "RENT"):
						v = -1
					else:
						v = 0
				else:
					v = -1
				x_a.append(v)
			elif (i == "Inquiries in the Last 6 Months"):
				if (len(fields[i]) != 0):
					v = (float(fields[i]))
				else:
					v = 0
				x_a.append(v)


			elif (i == "Open CREDIT Lines"):
				if (len(fields[i]) != 0):
					v = float(fields[i])
				else:
					v = -1
				x_a.append(v)

			elif (i == "Total CREDIT Lines"):
				if (len(fields[i]) != 0):
					v = float(fields[i])
				else:
					v = 0
				x_a.append(v)

			elif (i == "Employment Length"):
				if (len(fields[i]) != 0):
					m = fields[i].split(' ')
					if (len(m) == 3):
						v = -1
					elif (len(m) == 2):
						if (m[0] == "10+"):
							v = 10
						else:
							v = int(m[0])
					else:
						v = -1
				else:
					v = -1
				x_a.append(v)


			elif (i == "Months Since Last Delinquency"):
				if (len(fields[i]) != 0):
					v = int(fields[i])
				else:
					v = 0
				x_a.append(v)

			elif (i == "Education"):
				if (len(fields[i]) != 0):
					v = 1
				else:
					v = -1
				x_a.append(v)

			elif (i == "Public Records On File"):
				if (len(fields[i]) != 0):
					v = int(fields[i])
				else:
					v = 0
				x_a.append(v)

			elif (i == "Loan Length"):
				if (fields[i] == "36 months"):
					v = 36
				else:
					v = 60
				x_a.append(v)


			elif (i == "Interest Rate"):
				if (len(fields[i]) != 0):
					v = float(fields[i].strip('%'))
				else:
					v = 0
				x_a.append(v)
			
		#x_a.append(1)
		x_a = np.array(x_a) / 10e2
		#print(x_a)
		x.append(x_a)


#print(x)
#print(y)

X_train = np.array(x)
y_train = np.array(y).T
X_test = np.array(x)
y_test = np.array(y).T

#X, y = make_moons(n_samples=5000, random_state=42, noise=0.1)
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42,test_size=0.3)

# pylab.scatter(X[:,0], X[:,1], c=y)
# pylab.show()

# There are only two features in the data X[:,0] and X[:,1]
n_feature = 13
# There are only two classes: 0 (purple) and 1 (yellow)
n_class = 2


def init_weights(n_hidden=100):
    # Initialize weights with Standard Normal random variables
    model = dict(
        W1=np.random.randn(n_feature + 1, n_hidden),
        W2=np.random.randn(n_hidden + 1, n_hidden),
        #W3=np.random.randn(n_hidden + 1, n_hidden),
        W3=np.random.randn(n_hidden + 1, n_class)
    )

    return model

# Defines the softmax function. For two classes, this is equivalent to the logistic regression
def softmax(x):
    #print(x)
    return np.exp(x) / np.exp(x).sum()

# For a single example $x$
def forward(x, model):
    x = np.append(x, 1)
    
    # Input times first layer matrix 
    z_1 = np.dot(x, model['W1'])

    # ReLU activation goes to hidden layer
    h_1 = z_1
    h_1[z_1 < 0] = 0
    #h_1 = 1 / (1 + np.exp(-z_1))

    # Add the 1 for the bias
    h_1 = np.append(h_1, 1)
    
    # HL 1 times weight matrix
    z_2 = np.dot(h_1, model['W2'])
    
    # ReLU
    h_2 = z_2
    h_2[z_2 < 0] = 0
    #h_2 = 1 / (1 + np.exp(-z_2))
    
    # Add the bias term
    h_2 = np.append(h_2, 1)


    # z_3 = np.dot(h_2, model['W3'])
    
    # # ReLU
    # h_3 = z_3
    # h_3[z_3 < 0] = 0
    # #h_2 = 1 / (1 + np.exp(-z_2))
    
    # # Add the bias term
    # h_3 = np.append(h_3, 1)
    
    # Hidden layer values to output
    hat_y = softmax(np.dot(h_2,  model['W3']))

    return h_1, h_2, hat_y

def backward(model, xs, h1s, h2s, errs):
    """xs, hs, errs contain all information (input, hidden state, error) of all data in the minibatch"""
    # errs is the gradients of output layer for the minibatch
    # dW4 = (np.dot(h3s.T, errs))/xs.shape[0]

    # # Get gradient of hidden layer
    # dh_3 = np.dot(errs,  model['W4'].T)
    # dh_3[h3s <= 0] = 0
    
    # # The bias "neuron" is the constant 1, we don't need to backpropagate its gradient
    # # since it has no inputs, so we just remove its column from the gradient
    # dh_3 = dh_3[:, :-1]
    
    # Gradient for weights H1 -> H2
    dW3 = (np.dot(h2s.T, errs)) / xs.shape[0]

    dh_2 = np.dot(errs,  model['W3'].T)
    dh_2[h2s <= 0] = 0
    
    # The bias "neuron" is the constant 1, we don't need to backpropagate its gradient
    # since it has no inputs, so we just remove its column from the gradient
    dh_2 = dh_2[:, :-1]
    
    # Gradient for weights H1 -> H2
    dW2 = (np.dot(h1s.T, dh_2)) / xs.shape[0]
    
    # Gradient of h1
    dh_1 = np.dot(dh_2, model['W2'].T)
    dh_1[h1s <= 0] = 0

    # Again, drop the bias column
    dh_1 = dh_1[:, :-1]
    
    # Add the 1 to the data, to compute the gradient of W1
    ones = np.ones((xs.shape[0], 1))
    xs = np.hstack([xs, ones])

    dW1 = (np.dot(xs.T, dh_1))/xs.shape[0]

    return dict(W1=dW1, W2=dW2, W3=dW3)

def get_gradient(model, X_train, y_train):
    xs, h1s, h2s, h3s,  errs = [], [], [], [], []

    for x, cls_idx in zip(X_train, y_train):
        h1, h2, y_pred = forward(x, model)

        # Create one-hot coding of true label
        y_true = np.zeros(n_class)
        y_true[int(cls_idx)] = 1.

        # Compute the gradient of output layer
        err = y_true - y_pred

        # Accumulate the informations of the examples
        # x: input
        # h: hidden state
        # err: gradient of output layer
        xs.append(x)
        h1s.append(h1)
        h2s.append(h2)
        #h3s.append(h3)
        errs.append(err)

    # Backprop using the informations we get from the current minibatch
    return backward(model, np.array(xs), np.array(h1s), np.array(h2s), np.array(errs))

def gradient_step(model, X_train, y_train, learning_rate = 1e-3):
    grad = get_gradient(model, X_train, y_train)
    model = model.copy()

    # Update every parameters in our networks (W1 and W2) using their gradients
    for layer in grad:
        # Careful, learning rate should depend on mini-batch size
        model[layer] += learning_rate * grad[layer]

    return model

def gradient_descent(model, X_train, y_train, no_iter=10):

    minibatch_size = 100
    
    for iter in range(no_iter):
        print('Iteration (epoch) {}'.format(iter))

        ## MINI-BATCH: Shuffles the training data to sample without replacement
        indices = list(range(0,X_train.shape[0]))
        np.random.shuffle(indices)
        X_train = X_train[indices,:]
        y_train = y_train[indices]

        for i in range(0, X_train.shape[0], minibatch_size):
            # Get pair of (X, y) of the current mini-batch
            X_train_mini = X_train[i:i + minibatch_size]
            y_train_mini = y_train[i:i + minibatch_size]

            model = gradient_step(model, X_train_mini, y_train_mini, learning_rate = 1e-1)

    return model

no_iter = 10

# Reset model
model = init_weights()

# Train the model
model = gradient_descent(model, X_train, y_train, no_iter=no_iter)

y_pred = np.zeros_like(y_test)

accuracy = 0

for i, x in enumerate(X_test):
    # Predict the distribution of label
    _, _, prob = forward(x, model)
    # Get label by picking the most probable one
    y = np.argmax(prob)
    y_pred[i] = y

    # Accuracy of predictions with the true labels and take the percentage
    # Because our dataset is balanced, measuring just the accuracy is OK
    accuracy = (y_pred == y_test).sum() / y_test.size

print('Accuracy after {} iterations: {}'.format(no_iter,accuracy))
