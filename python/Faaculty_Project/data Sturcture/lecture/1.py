# a = [int(x)for x in str(int(input()))]
# b = [int(x)for x in str(int(input()))]
# a1 = a.copy()
# a2 = a.copy()
# b1 = b.copy()
# b2 = b.copy()
# # global items_7_in_a
# # items_7_in_a = 0
# # global items_4_in_a
# # items_4_in_a = 0
# # global items_4_in_b
# # items_4_in_b = 0
# # global items_7_in_b
# # items_7_in_b = 0
# global items
# items = 0
# # for i in range(len(a)):
# #     if a[i] == 4:
# #         items_4_in_a += 1
# #     if a[i] == 7:
# #         items_7_in_a += 1
# #     if b[i] == 4:
# #         items_4_in_b += 1
# #     if b[i] == 7:
# #         items_7_in_b += 1
# if a == b:
#     print(items)
# else:
#     def replace_out_a(a1, b1):
#         items = 0
#         for i in range(len(a1)):
#             if a1[i] == b1[i]:
#                 continue
#             else:
#                 if a1[i] == 7:
#                     a1[i] = 4
#                     items += 1
#                     if a1 == b1:
#                         return items
#                 elif a1[i] == 4:
#                     items += 1
#                     a1[i] = 7
#                     if a1 == b1:
#                         return items
#         return 0

#     def replace_in_a(a2, b2):
#         items = 0
#         for i in range(len(a2)):
#             for j in range(i, len(a2)):
#                 if a2[i] != a2[j]:
#                     a2[i], a2[j] = a2[j], a2[i]
#                     items += 1
#                     if a2 == b2:
#                         return items
#                     a2[j], a2[i] = a2[i], a2[j]
#         return 0
#     q2 = replace_in_a(a2, b2)
#     q1 = replace_out_a(a1, b1)
#     if q1 == 0:
#         print(q2)
#     elif q2 == 0:
#         print(q1)
#     elif q1 < q2:
#         print(q1)
#     elif q1 > q2:
#         print(q2)
