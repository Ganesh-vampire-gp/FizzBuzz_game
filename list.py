Name=["nithin","ganesh","siddu","padma","sai"]
print(Name)


Name.append("gani")
print(Name)

Name.insert(1,"science")
print(Name)

Name.count("sai")

for i in range(len(Name)):
    print(i,".",Name[i])


total_length=len(Name)
print(total_length)



print(Name[1:4])