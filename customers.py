val = {
    name: eval(vals)
    for j in range(int(input()))
    for name, vals in [tuple(input().split())]
}
print(val)

pairs = dict()

keys = list(val.keys())

for i in range(k := len(val.keys())):
    for j in range(i + 1, k):
        pairs[(keys[i], keys[j])] = len(
            set(val[keys[i]]).intersection(set(val[keys[j]]))
        )
print(pairs)

pairs = list(i[::-1] for i in pairs.items())
pairs.sort(reverse=True)
print(*(f"{key[0]} - {key[1]} : {value}" for value, key in pairs), sep="\n")
