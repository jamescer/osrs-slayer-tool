from slayer import SlayerTool
import sys
from hiscores import Hiscores
from skill import Skill


def test_demo():
    # slayer tool testing
    tr = SlayerTool(username='jimbo jango')
    tr.get_doable_assignments()
    tr.create_graph(master_name='Vannaka', sample_size=1000)

    
    tr.reset_counter()
    tr.create_graph(master_name='sdfsdf', sample_size=1000)
    
    tr.set_account('not poop')
    print(str(tr),repr(tr))
    

    # hiscore testing
    a = Hiscores('not poop')
    b = Hiscores('jimbo jango')
    try:
        d = Hiscores('mod asgggaaggda')
    except Exception as e:
        print(e)
    c = 0

    print(str(a), repr(a))
    print(a.skills_over(50), a.skills_under(60), a.max_skill(), a.min_skill())

    print(a == b, a != b, a < b, a > b, a <= b, a >=
          b, a == c, a < c, a > c, a.closest_skill())

    # Skill testing
    print(a.skills['prayer'].xp_tnl(), a.skills['attack'].xp_to(99))

    try:
        a = Skill('Warding')
    except Exception as e:
        print(e)
    print(str(a.skills['attack']), repr(a.skills['attack']))


test_demo()
