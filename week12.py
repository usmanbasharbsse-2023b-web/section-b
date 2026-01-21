# # # list1 = [1, 3, 0.3, "Section B"]
# # # print(list1)
# # # print(list1[2])
# # # print(list1[-3])
# # # print(list1[:5])
# # # print(list1[:4])
# # # print(list1[2:])
# # # print(list1[-1:-5:-2])
# # # list1.append("SE")
# # # print(list1)
# # # list1.insert(0,"5th sem")
# # # print(list1)
# # # list1[1] = 11
# # # print(list1)
# # # list1.pop()
# # # print(list1)
# # # list1.remove("5th sem")
# # # print(list1)
# # # list1.reverse()
# # # print(list1)
# # # list1.clear()
# # # print(list1)
# # # del list1
# # # list2 = [9,1,4,2,7,3,5,0]
# # # list2.sort
# # # print(list2)
# # # list3 = ["AC","AB","C"]
# # # list3.sort()
# # # print(list3)

# # tuples=(1,2,"SE","section b")
# # print(tuples)
# # print(tuples[1])
# # print()
# # print(tuples[1:])
# # list1 = list(tuples)
# # list1.append("5 semester")
# # list1.insert(0,6)
# # list1.remove(1)
# # tuples =tuple(list1)
# # print(tuples)

# number = [5,2,1,3,"sec b"]
# print(number[-2:3:-2])
number ={2,1,5,4,0,False}
set2={9,8,1,2,7,6}
print(number)
number.add("5th semester")
print(number)
number.pop()
print(number)
number.remove(True)
print(number)
number.update(set2)
print(number)
number.union(set2)
print("union is",number)
set3= number.intersection(set2)
print("intersection",set3)

nums = [5, 10, 3, 8, 2]
print(nums)
print(sum(nums))
print(max(nums))
print(min(nums))