from adventus import fetch

data = fetch(1,2015)
print(data.count("(") - data.count(")"))