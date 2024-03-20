import numpy as np
import matplotlib.pyplot as plt

def load_dataset():
	with np.load("C:/Users/toart/Documents/Importantly/Synopsis/mnist.npz") as f:
		# convert from RGB to Unit RGB
		x_train = f['x_train'].astype("float32") / 255 
		
		# reshape from (60000, 28, 28) into (60000, 784)
		x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))

		# labels
		y_train = f['y_train']
		
		# convert to output layer format
		y_train = np.eye(10)[y_train]

		return x_train, y_train

images, labels = load_dataset()

weights_input_to_hidden = np.random.uniform(-0.5, 0.5, (20, 784))
weights_hidden_to_output = np.random.uniform(-0.5, 0.5, (10, 20))
bias_input_to_hidden = np.zeros((20, 1))
bias_hidden_to_output = np.zeros((10, 1))

epochs = 3
e_loss = 0
e_correct = 0
learning_rate = 0.01

for epoch in range(epochs):
	print(f"Epoch №{epoch}")

	for image, label in zip(images, labels):
		image = np.reshape(image, (-1, 1))
		label = np.reshape(label, (-1, 1))

		# Forward propagation (to hidden layer)
		hidden_raw = bias_input_to_hidden + weights_input_to_hidden @ image
		hidden = 1 / (1 + np.exp(-hidden_raw)) # sigmoid

		# Forward propagation (to output layer)
		output_raw = bias_hidden_to_output + weights_hidden_to_output @ hidden
		output = 1 / (1 + np.exp(-output_raw))

		# Loss / Error calculation MSE
		e_loss += 1 / len(output) * np.sum((output - label) ** 2, axis=0)
		e_correct += int(np.argmax(output) == np.argmax(label))

		# Backpropagation (output layer)
		delta_output = output - label
		weights_hidden_to_output += -learning_rate * delta_output @ np.transpose(hidden)
		bias_hidden_to_output += -learning_rate * delta_output

		# Backpropagation (hidden layer)
		delta_hidden = np.transpose(weights_hidden_to_output) @ delta_output * (hidden * (1 - hidden))
		weights_input_to_hidden += -learning_rate * delta_hidden @ np.transpose(image)
		bias_input_to_hidden += -learning_rate * delta_hidden

		# DONE

	# print some debug info between epochs
	print(f"Loss: {round((e_loss[0] / images.shape[0]) * 100, 3)}%")
	print(f"Accuracy: {round((e_correct / images.shape[0]) * 100, 3)}%")
	e_loss = 0
	e_correct = 0

'''# CHECK CUSTOM
test_image = plt.imread("Py/custom.jpg", format="jpeg")

# Grayscale + Unit RGB + inverse colors
gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
test_image = 1 - (gray(test_image).astype("float32") / 255)

# Reshape
test_image = np.reshape(test_image, (test_image.shape[0] * test_image.shape[1]))

# Predict
image = np.reshape(test_image, (-1, 1))

# Forward propagation (to hidden layer)
hidden_raw = bias_input_to_hidden + weights_input_to_hidden @ image
hidden = 1 / (1 + np.exp(-hidden_raw)) # sigmoid
# Forward propagation (to output layer)
output_raw = bias_hidden_to_output + weights_hidden_to_output @ hidden
output = 1 / (1 + np.exp(-output_raw))

plt.imshow(test_image.reshape(28, 28), cmap="Greys")
plt.title(f"NN suggests the CUSTOM number is: {output.argmax()}")
plt.show()

# test version'''
'''

images, labels = load_dataset()

w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
w_h_o = np.random.uniform(-0.5, 0.5, (10, 20))
b_i_h = np.zeros((20, 1))
b_h_o = np.zeros((10, 1))

learn_rate = 0.01
nr_correct = 0
loss = 0
epochs = 3
for epoch in range(epochs):
    for img, l in zip(images, labels):
        img = np.reshape(img, (-1, 1))
        l = np.reshape(l, (-1, 1))

        # Forward propagation input -> hidden
        h_pre = b_i_h + w_i_h @ img
        h = 1 / (1 + np.exp(-h_pre))
        # Forward propagation hidden -> output
        o_pre = b_h_o + w_h_o @ h
        o = 1 / (1 + np.exp(-o_pre))

        # Cost / Error calculation
        loss += 1 / len(o) * np.sum((o - l) ** 2, axis=0)
        nr_correct += int(np.argmax(o) == np.argmax(l))

        # Backpropagation output -> hidden (cost function derivative)
        delta_o = o - l
        w_h_o += -learn_rate * delta_o @ np.transpose(h)
        b_h_o += -learn_rate * delta_o
        # Backpropagation hidden -> input (activation function derivative)
        delta_h = np.transpose(w_h_o) @ delta_o * (h * (1 - h))
        w_i_h += -learn_rate * delta_h @ np.transpose(img)
        b_i_h += -learn_rate * delta_h

    # Show accuracy for this epoch
    print(f"Loss: {round((loss[0] / images.shape[0]) * 100, 2)}%")
    print(f"Acc: {round((nr_correct / images.shape[0]) * 100, 2)}%")
    nr_correct = 0
    loss = 0

exit(0)

# Show results
while True:
    index = int(input("Enter a number (0 - 59999): "))
    img = images[index]
    plt.imshow(img.reshape(28, 28), cmap="Greys")

    img.shape += (1,)
    # Forward propagation input -> hidden
    h_pre = b_i_h + w_i_h @ img.reshape(784, 1)
    h = 1 / (1 + np.exp(-h_pre))
    # Forward propagation hidden -> output
    o_pre = b_h_o + w_h_o @ h
    o = 1 / (1 + np.exp(-o_pre))

    plt.title(f"Subscribe if its a {o.argmax()} :)")
    plt.show()
'''