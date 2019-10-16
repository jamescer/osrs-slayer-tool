from slayer import SlayerTool
import sys
tr = SlayerTool(username='not poop')


tr.get_doable_assignments()
tr.set_account('not poop')
tr.reset_counter()

tr.create_graph(master_name=0,sample_size=1000)
