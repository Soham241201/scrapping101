import json
file = "results2.txt"
with open(file, "r") as handle : 
    data = handle.read()

processed = data.split("\n\n")
processed = [x.split("\n") for x in processed]
# proccesed_dict = dict()
# proessed_list = list()
rcds = dict()
processed_list = list()
count = 0
for x in processed:
    count+=1
#     if count==47:
#         break
    key, val = None, None
    cont_flag = False
    for y in x:
        if ":" in y:
            key = y.split(":")[0].strip()
            val = y.split(":")[1].strip()
            if val ==" Bark of the Town #MD18":
                print(f"COUNT: {count}")
            
        else:
            if val:
                cont_flag = True
                val + str(y.strip())
        if not cont_flag:
            rcds[key] = val.strip() if val else val
    if cont_flag:
        rcds[key] = val.strip() if val else val
    processed_list.append(rcds.copy())
    
    name_list = list()
del_index_list = list()
for idx, element in enumerate(processed_list):
    if element.get("Name") in name_list: del_index_list.append(idx)
    if element.get("Name"): name_list.append(element.get("Name"))
# for idx in del_index_list: processed_list.pop(idx)  

cleand_list = list()
for idx, element in enumerate(processed_list):
    if not idx in del_index_list:
        cleand_list.append(element.copy())
        
# print(cleand_list)
final  = json.dumps(cleand_list, indent=2)
# print(final)
with open("final.json", "w") as outfile:
    outfile.write(final)