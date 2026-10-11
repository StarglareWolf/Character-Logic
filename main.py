# from collections import deque
#
# print("本实验用以复刻刷新NPC的想法")
# n = int(input("设置NPC个数:"))
# dic = {}
# talked = {}
# for i in range(1, n+1):
#     name = input("输入他们的名字:")
#     dic[name] = [0, 0, 0, 0, 0]
#     talked[name] = False
#
# round = int(input("设置回合数:"))
#
# print("好感度分为三个阶段：5~10是熟悉,10~15是朋友,15及以上是挚友")
# print("每个回合你可以自主和任意角色互动,输入#结束")
#
# familiar = deque()
# friend = deque()
# closefriend = deque()
#
# trigger = 0
#
#
# for i in range(1, round + 1):
#     print(f"进行到第{i}回合,剩余{round - i}回合")
#     if trigger == 0:
#         if familiar and dic[familiar[0]][1] == 0:
#             print(f"{familiar[0]}来找你玩了!")
#             dic[familiar[0]][1] = 1
#             familiar.popleft()
#             trigger = 1
#         elif friend and dic[friend[0]][2] == 0:
#             print(f"{friend[0]}来找你玩了!")
#             dic[friend[0]][2] = 1
#             friend.popleft()
#             trigger = 1
#         elif closefriend and dic[closefriend[0]][3] == 0:
#             print(f"{closefriend[0]}来找你玩了!")
#             dic[closefriend[0]][3] = 1
#             dic[closefriend[0]][4] = 3
#             closefriend.popleft()
#             trigger = 1
#
#     character = input("和谁提升好感度:")
#     while character != "#":
#         if character in dic and talked[character] == False:
#             dic[character][0] += 2
#             talked[character] = True
#             if dic[character][0] >= 5 and dic[character][0] < 10:
#                 familiar.append(character)
#                 dic[character][4] = 1
#             elif dic[character][0] >= 10 and dic[character][0] < 15:
#                 friend.append(character)
#                 dic[character][4] = 2
#             elif dic[character][0] >= 15:
#                 closefriend.append(character)
#                 dic[character][4] = 3
#         elif character not in dic:
#             print("你没见过这个人!")
#         else:
#             print("当前回合已经聊过了，无法再继续")
#         character = input("和谁提升好感度:")
#
#     trigger = 0
#
#     for name in talked:
#         talked[name] = False
#
# print("总结")
# for name in dic:
#     if dic[name][4] == 0:
#         relation = "陌生"
#     elif dic[name][4] == 1:
#         relation = "熟悉"
#     elif dic[name][4] == 2:
#         relation = "朋友"
#     else:
#         relation = "挚友"
#     print(f"{name}:好感度-{dic[name][0]},关系-{relation}")


from Rebuild import System
Lucy = System()
Lucy.setup()
Lucy.play()