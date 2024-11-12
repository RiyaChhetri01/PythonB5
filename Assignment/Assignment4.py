import numpy as np

arr=np.array([1,2,3])
new_arr=np.append(arr,[5,6])#append is mainly used to add element in anarray
print(new_arr)





#3. Evaluate  y=2pi_omega_x


# Define constants and variables
pi = np.pi            # π (Pi) value
omega = 5             # Example value for ω (omega)
x = 3                 # Example value for x

# Evaluate y = 2 * pi * omega * x
y = 2 * pi * omega * x
print("y =", y)



import numpy as np

# Create an array for one hour with each second as an element
time_in_seconds = np.arange(0, 3600)

print(time_in_seconds)
