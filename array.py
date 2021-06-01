#Array Practice
dict = {'January' :2200,
        'February': 2350,
        'March': 2600,
        'April': 2130,
        'May':  2190
}

print(dict['February']-dict['January'])

list = [2200, 2350, 2600, 2130, 2190]

print(list[1]-list[0])
print(list[0]+list[1]+list[2])

if 2000 in list:
    print("Spent 2000")
else:
    print("Not spent 2K")

list.append(1900)
print(list)

list[3]=list[3]-200
print(list)

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')

heros.insert(3,'black panther')
print(heros)

heros = [ele for ele in heros if ele!='thor' and ele!='hulk']
print(heros)

heros.append('Dr. Strange')

heros.sort()
print(heros)

n = int(input("Enter the max number"))

odd_list = []
for i in range(n):
    if i % 2 !=0:
        odd_list.append(i)
print(odd_list)