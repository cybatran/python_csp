import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Column 2 from data table
A_input_chars = [1, 2, 3, 4]
B_input_chars = [1, 2, 3, 4, 5, 6, 7, 8]

# Column 3 and 4 from data table
# Replace list elements with your times
A_time = [0.00469899177551, 0.0213458538055, 0.175691127777, 1.175691127777] 
B_time = [0.00766396522522, 0.00855588912964, 0.0116171836853, 0.0217900276184, 0.0595681667328, 0.174690008163, 0.54566097259, 1.6501429081] 

fig, ax = plt.subplots(1,1)
# plot(x_list, y_list, "color and style")
ax.plot(A_input_chars, A_time, 'ro-', label='Algo. A') # red dots
ax.plot(B_input_chars, B_time, 'bo-', label='Algo. B') # blue dots

# Label and show
ax.set_xlabel ("Length of input in characters")
ax.set_ylabel("Execution time")
ax.set_title("Execution time vs. input length")
ax.legend(loc='center left') # Show and place the legend fig.set_facecolor('white')
fig.savefig('graph_data_2')
