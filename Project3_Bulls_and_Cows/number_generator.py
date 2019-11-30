import random
generated_number = [int(x) for x in range(10)]
secret = []

for i in generated_number:
    number = random.choice(generated_number)
    if len(secret) == 4:
        break
    else:
        secret.append(number)
        generated_number.remove(number)
print(secret)
