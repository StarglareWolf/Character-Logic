from GameChara import GameChara
from collections import deque

class System:
    USER_CHOICE = ["1", "2", "3", "4"]
    def __init__(self):
        self.characters = {}
        self.total_round = 0
        self.current_round = 1
        self.familiar = deque()
        self.friend = deque()
        self.close_friend = deque()

    def setup(self):
        set_round = int(input("请输入回合数:"))
        num = int(input("请输入角色数:"))
        self.total_round = set_round
        for i in range(1, num + 1):
            character = input("输入角色名:")
            gamechara = GameChara(character)
            self.characters[character] = gamechara

    def _name_in_chara(self, name):
        return name in self.characters

    def _reset_talked(self):
        for chara in self.characters.values():
            chara.begin_of_day()
        
    def _final_summary(self):
        for character in self.characters.values():
           print(character)

    def _up_to_relation_event(self, chara, character):
        if chara.favor >= chara.RELATION_LEVEL["熟悉"] and not chara.event["familiar_event"]:
            self.familiar.append(character)
            chara.event["familiar_event"] = True
        if chara.favor >= chara.RELATION_LEVEL["朋友"] and not chara.event["friend_event"]:
            self.friend.append(character)
            chara.event["friend_event"] = True
        if chara.favor >= chara.RELATION_LEVEL["挚友"] and not chara.event["close_friend_event"]:
            self.close_friend.append(character)
            chara.event["close_friend_event"] = True

    def _special_event_trigger(self):
        if self.familiar:
            print(f"{self.familiar.popleft()}来找你玩了!")

        elif self.friend:
            print(f"{self.friend.popleft()}来找你玩了!")

        elif self.close_friend:
            print(f"{self.close_friend.popleft()}来找你玩了!")

    def _make_decision(self, chara, user_choice):
        if user_choice not in self.USER_CHOICE:
            print("不存在该选项!")
            return
        if user_choice == "1":
            if not chara.interact["conversation"]:
               chara.conversation()
            else:
                print("和当前角色交流过了")
        elif user_choice == "2":
            if not chara.interact["consultation"]:
               chara.consultation()
            else:
                print("和当前角色请教过了")
        elif user_choice == "3":
            if not chara.interact["give_gift"]:
               chara.give_gift()
            else:
                print("今天送过礼物了")
        else:
            if not chara.interact["dating"]:
               chara.dating()
            else:
                print("已经约对方出去过了")


    def play(self):
        # 从熟悉到朋友，再到挚友，层层递进，采用熟悉优先级高的策略，防止某个关系进阶到朋友或挚友，导致原来熟悉关系的演出无法出现。一回合只来一个人
        while self.current_round <= self.total_round:
            print(f"进行到第{self.current_round}回合,剩余{self.total_round - self.current_round}回合")
            self.current_round += 1
            self._special_event_trigger()

            character = input("和谁提升好感度:")

            while character != "#":
                if self._name_in_chara(character) and (not self.characters[character].end_of_day()):
                    chara = self.characters[character]
                    print("1:conversation--2:consultation--3:give_gift--4:dating")
                    
                    user_choice = input("干什么好呢:")
                    self._make_decision(chara, user_choice)
                        
                    self._up_to_relation_event(chara, character)
                        
                elif not self._name_in_chara(character):
                    print("不存在这个角色!")
                    
                else:
                    print("当前回合已与该角色完整交互")

                character = input("和谁提升好感度:")

            self._reset_talked()

        self._final_summary()







