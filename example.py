from slayer import SlayerTool
import sys
from hiscores import Hiscores
from skill import Skill
# slayer tool testing
tr = SlayerTool(username='not poop')
tr.get_doable_assignments()
tr.set_account('not poop')
tr.reset_counter()
tr.create_graph()
tr.create_graph(master_name='sdfsdf', sample_size=1000)
str(tr)
repr(tr)


# hiscore testing
a = Hiscores('not poop')
b = Hiscores('jimbo jango')
try:
    d= Hiscores('mod asgggaaggda')
except Exception as e:
    print(e)
c=0
str(a)
repr(a)
a.skills_over(50)
a.skills_under(60)
print(a.closest_skill())
a.max_skill()
a.min_skill()
a==b
a!=b
a<b
a>b
a<=b
a>=b
a==c
a<c
a>c

# Skill testing
a.skills['prayer'].xp_tnl()
a.skills['attack'].xp_to(99)
try:
    a = Skill('Warding')
except Exception as e:
    print(e)
str(a.skills['attack'])
repr(a.skills['attack']) 
