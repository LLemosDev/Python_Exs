digits = [1, 2, 4, 5]
target = 7

for d in range(0, len(digits)):
    for i in range(d + 1, len(digits)):
        sum = digits[d] + digits[i]

        if sum == target:
            print(f"Sucesso o índice {d} = {digits[d]} + índice {i} = {digits[i]} == {target}")