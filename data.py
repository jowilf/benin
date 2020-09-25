new_data = []
with open('data','r') as f:
    for line in f.readlines():
        val = line.strip().replace(";","")
        if not val.startswith("ARROND:"):
            new_data.append(val+"\n")
    f.close()
with open('cotonou.data','w') as f:
    f.writelines(new_data)