from slayer import SlayerTool
import sys
from hiscores import Hiscores
from skill import Skill


def test_demo():
    # slayer tool testing
    test = SlayerTool(username='not_poop')
    # tr.get_doable_assignments()
    test.create_graph(master_name='Vannaka',
                      sample_size=1000, show_figure=True)

    # tr.create_graph(master_name='sdfsdf', sample_size=1000)

#     tr.set_account('not_poop')
#     # print(str(tr), repr(tr))

#     # hiscore testing
#     a = Hiscores('not_poop')
#     # b = Hiscores('jimbo jango')

#     print(str(a), repr(a))
#     print(a.skills_over(50), a.skills_under(60), a.max_skill(), a.min_skill())

#     # Skill testing
#     print(a.skills['prayer'].xp_tnl(), a.skills['attack'].xp_to(99))

#     try:
#         a = Skill('Warding')
#     except Exception as e:
#         print(e)
#     print(str(a.skills['attack']), repr(a.skills['attack']))


# test_demo()
