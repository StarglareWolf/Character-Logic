class GameChara:
    RELATION_LEVEL={
        "熟悉":5,
        "朋友":10,
        "挚友":15
    }

    def __init__(self, name, favor = 0):
        self.name = name
        self.favor = favor
        self.event = {"familiar_event":False, "friend_event":False, "close_friend_event":False}
        self.interact = {"conversation":False, "consultation":False, "give_gift":False, "dating":False}

    def __str__(self):
        return f"姓名-{self.name}:好感度-{self.favor}:关系-{self.relation}"

    @property
    def relation(self):
        if self.favor >= self.RELATION_LEVEL["挚友"]: name = "挚友"
        elif self.favor >= self.RELATION_LEVEL["朋友"]: name = "朋友"
        elif self.favor >=self.RELATION_LEVEL["熟悉"]: name = "熟悉"
        else: name = "陌生"
        return name

    def _add_favor(self, delta):
        #提升好感度
        self.favor = max(0, min(self.favor + delta, 30))

    def conversation(self):
        self._add_favor(2)
        self.interact["conversation"] = True

    def consultation(self):
        self._add_favor(3)
        self.interact["consultation"] = True

    def give_gift(self):
        self._add_favor(5)
        self.interact["give_gift"] = True

    def dating(self):
        self._add_favor(10)
        self.interact["dating"] = True
        
    def begin_of_day(self):
        self.interact["conversation"] = False
        self.interact["consultation"] = False
        self.interact["give_gift"] = False
        self.interact["dating"] = False
        
    def end_of_day(self):
        return self.interact["conversation"] and self.interact["consultation"] and self.interact["give_gift"] and self.interact["dating"]