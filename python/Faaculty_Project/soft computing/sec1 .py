import numpy as np

# AND logic function using  Pitts neuron

# >>>>>>>>>>>>>>> McCulloch >>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>    AND    >>>>>>>>>>>>>>>
# def MCP_AND(x1, x2):
#     w1, w2 = 1, 1
#     theta = 2  # calculated using θ ≥ n*w - p, where n=2, w=1, p=0
#     y_in = x1 * w1 + x2 * w2
#     return 1 if y_in >= theta else 0

# inputs = [(0,0), (0,1), (1,0), (1,1)]
# for x1, x2 in inputs:
#     print(f"Input: {x1}, {x2} -> Output: {MCP_AND(x1, x2)}")

# >>>>>>>>>>>>>>>    XOR    >>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>> x*x'+x'*x >>>>>>>>>>>>>>>

# def MCP_Neuron(w1, w2, x1, x2, theta):
#     y_in = x1 * w1 + x2 * w2
#     return 1 if y_in >= theta else 0

# def MCP_XOR(x1, x2):
#     z1 = MCP_Neuron(1, -1, x1, x2, 1)
#     z2 = MCP_Neuron(-1, 1, x1, x2, 1)
#     return MCP_Neuron(1, 1, z1, z2, 1)

# inputs = [(0,0), (0,1), (1,0), (1,1)]
# for x1, x2 in inputs:
#     print(f"Input: {x1}, {x2} -> Output: {MCP_XOR(x1, x2)}")

# >>>>>>>>>>>>>>> Hebbian Learning >>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>       AND        >>>>>>>>>>>>>>>


# X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
# y = np.array([1, -1, -1, -1])

# weights = np.zeros(2)
# bias = 0

# # Training using Hebb Rule
# for i in range(len(X)):
#     weights += X[i] * y[i]
#     bias += y[i]

# print("Final Weights:", weights)
# print("Final Bias:", bias)

# >>>>>>>>>>>>>>>    I O    >>>>>>>>>>>>>>>


# patterns = {
#     'I': np.array([1, 1, 1, -1, 1, -1, 1, 1, 1]),
#     'O': np.array([1, 1, 1, 1, -1, 1, 1, 1, 1])
# }

# targets = {'I': 1, 'O': -1}

# weights = np.zeros(9)
# bias = 0
# print("Initial Weights:", patterns.items())
# for letter, pattern in patterns.items():
#     weights += pattern * targets[letter]
#     bias += targets[letter]

# print("Trained Weights:", weights)
# print("Trained Bias:", bias)

# new_wight =0  
# input_new = np.array(list(map(int, input("Enter a pattern (9 values separated by spaces): ").split())))
# result = np.zeros(9)
# for i in range(len(input_new)):
#     new_wight += input_new[i] * weights[i]

# if   new_wight >= 0 :
#     print("'I'")
# else:
#     print("'O'")