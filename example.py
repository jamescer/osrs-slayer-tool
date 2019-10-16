from slayer import SlayerTool
import sys
from hiscores import Hiscores

# slayer tool testing
tr = SlayerTool(username='not poop')
tr.get_doable_assignments()
tr.set_account('not poop')
tr.reset_counter()
tr.create_graph(master_name=0, sample_size=1000)



# hiscore testing
a = Hiscores('not poop')
b = Hiscores('jimbo jango')
c=0
str(a)
repr(a)
a.skills_over(50)
a.skills_under(60)
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
a.skills['attack'].xp_tnl()
a.skills['attack'].xp_to(99)
str(a.skills['attack'])
repr(a.skills['attack']) 
