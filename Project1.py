import numpy as np

# Step 1: Take 9 numerical inputs from the user
values = []

while len(values) < 9:
    entry_num = len(values) + 1
    user_input = input(f"Enter value {entry_num}: ")
    try:
        number = float(user_input)
        values.append(number)
    except:
        print("Invalid input. Please enter a number.")

# Step 2: Convert to 3x3 array
matrix = np.array(values).reshape(3, 3)

# Step 3: Do all calculations
results = {
    "Mean": [matrix.mean(axis=0), matrix.mean(axis=1), matrix.mean()],
    "Variance": [matrix.var(axis=0), matrix.var(axis=1), matrix.var()],
    "Standard Deviation": [matrix.std(axis=0), matrix.std(axis=1), matrix.std()],
    "Maximum": [matrix.max(axis=0), matrix.max(axis=1), matrix.max()],
    "Minimum": [matrix.min(axis=0), matrix.min(axis=1), matrix.min()],
    "Sum": [matrix.sum(axis=0), matrix.sum(axis=1), matrix.sum()]
}

# Step 4: Print results rounded to 2 decimal places
for name, values in results.items():
    rounded = []
    for item in values:
        if isinstance(item, np.ndarray):
            rounded.append([round(x, 2) for x in item])
        else:
            rounded.append(round(item, 2))
    print(f"{name}: {rounded}")