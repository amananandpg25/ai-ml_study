with open('/Users/amananand/Downloads/SDE/ai:ml/week8.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('subgraph BiologicalNeuron')
if idx != -1:
    print("Found bio neuron at index:", idx)
    print(repr(content[idx-100:idx+500]))
else:
    print("Bio neuron not found")

idx2 = content.find('subgraph AND')
if idx2 != -1:
    print("Found AND gate at index:", idx2)
    print(repr(content[idx2-100:idx2+500]))
else:
    print("AND gate not found")
