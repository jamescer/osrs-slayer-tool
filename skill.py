import const


class Skill(object):
    def __init__(self, name, rank=0, level=0, xp=0):
        if name not in const.SKILLS_SET:
            raise Exception(str(name) + " is not a valid skill.")

        self.name = name
        self.rank = rank
        self.level = level
        self.xp = xp

    # xp to next level
    def xp_tnl(self):
        if self.level >= 99:
            return float('inf')
        else:
            return const.XP_TABLE[self.level] - self.xp

    def xp_to(self, level):
        return const.XP_TABLE[level - 1] - self.xp

    def __str__(self):
        return self.name+' - Rank: '+str(self.rank)+ ', Level: '+str(self.level)+ ', Exp: ' + str(self.xp)

    def __repr__(self):
        return self.__str__()


