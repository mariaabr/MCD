import math
import random
import matplotlib.pyplot as plt
from bloom_filter import BloomFilter

# N = 100
# M = 10

# stream = [random.randint(0, N) for _ in range(M)] + [2 * N] + [random.randint(0, N) for _ in range(M)]
# stream = [random.randint(0, N) for _ in range(M)]

# (Ax + B) mod P mod N

class KIndependentHash:
    def __init__(self, k, p=2 ** 31 - 1):
        """
        Initialize a k-independent hash function.

        Parameters:
        k (int): The degree of independence (k-independence).
        p (int): A large prime number used for modulo operations (default is a prime near 2^31).
        """
        self.k = k
        self.p = p
        # Generate random coefficients for the polynomial hash function
        self.coefficients = [random.randint(1, p - 1) for _ in range(k)]

    def hash(self, x):
        """
        Compute the hash of an input x using the k-independent hash function.

        Parameters:
        x (int): The input value to hash.

        Returns:
        int: The hashed value.
        """
        hash_value = 0
        for i in range(self.k):
            hash_value += self.coefficients[i] * (x ** i)
        return hash_value % self.p

class BaseAlg:

    # Initialize the stream
    stream = []

    # Current element
    x = 0

    def __init__(self, size):
        # Initialize bloom filter
        self.bloom = BloomFilter(max_elements=size, error_rate=0.1)

        # Initialize the results
        self.results = {'found': []}

    def alg(self):

        # Check again if the element is in the bloom filter
        found = self.x in self.bloom

        # Add the result to the results
        self.results['found'].append(found)

        # Mark the element as seen
        self.bloom.add(self.x)

    def validate(self):

        # Check if the size of the results is the same as the stream
        if len(self.results['found']) != len(stream):
            print(f"len(self.results['found']) = {len(self.results['found'])}, len(stream) = {len(stream)}")
            print(f"results['found'] has the wrong size")

        else:

            foundL = []
            appeared = []

            # Check if the results are correct
            for x in self.stream:
                foundL.append(x in appeared)
                appeared.append(x)

            Fails = 0

            # Size of the stream
            sz = len(self.stream)

            for i in range(sz):
                if self.results['found'][i] != foundL[i]:
                    Fails += 1

            print(f"Fails = {Fails} ({Fails / sz * 100:.2f}%)")

            # Save the results
            self.results['Fails'] = Fails

    # def optimal_hash_functions_stream(M, N):
    #     """
    #     Calculate the optimal number of hash functions for a Bloom filter,
    #     where M is the size of the stream and N is the maximum value.
    #
    #     Parameters:
    #     M (int): Size of the Bloom filter (number of bits in the filter)
    #     N (int): Maximum value in the stream
    #
    #     Returns:
    #     int: Optimal number of hash functions
    #     """
    #     # Avoid division by zero if max value is zero
    #     if N == 0:
    #         return 1
    #
    #     k = (M / N) * math.log(2)
    #
    #     return max(1, int(k))  # Ensure at least 1 hash function


class StreamAlg(BaseAlg):

    def __init__(self, stream, size=6):

        print(f"stream: {stream}, len(stream): {len(stream)}")
        self.stream = stream
        self.size = size

        super().__init__(size)

        self.exec()
        self.validate()

    def exec(self):
        for v in self.stream:
            self.x = v
            self.alg()
        for key, value in self.results.items():
            print(f"streaming_{key}: {value}")


M_values = [i * 5 for i in range(1, 3)]
fails_values = []

for M in M_values:

    # Keep track of the number of fails
    current_fails = 0

    # Repeat the experiment 10 times
    for _ in range(10):

        N = 100
        stream = [random.randint(0, N) for _ in range(M)]

        SA = StreamAlg(stream, math.floor(0.3 * M))
        fails = SA.results['Fails']

        # Add the number of fails to the current fails
        current_fails += fails

    # Calculate the average number of fails
    fails_values.append(current_fails / 10)

    print(f"M = {M}, fails = {fails_values[-1]}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(M_values, fails_values, marker='o')
plt.title('Number of Fails vs Stream Size (M)')
plt.xlabel('Stream Size (M)')
plt.ylabel('Number of Fails')
plt.grid(True)
plt.show()