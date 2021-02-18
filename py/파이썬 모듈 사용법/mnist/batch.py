from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./samples/MNIST_data/", one_hot=True)


print(len(mnist.test.images))#10000
print(len(mnist.test.images[0]))#784 = 28x28
print(len(mnist.test.labels))#10000
print(len(mnist.test.labels[0]))#10
print()
batch_xs, batch_ys = mnist.train.next_batch(100)
print(len(batch_xs)) # 100
print(len(batch_xs[0])) # 784
print(len(batch_ys)) # 100
print(len(batch_ys[0])) # 10
