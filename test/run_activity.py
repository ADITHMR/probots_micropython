

from activity1.pactivity import run_activity as run_activity1
from activity2.pactivity import run_activity as run_activity2
from activity3.pactivity import run_activity as run_activity3
from activity4.pactivity import run_activity as run_activity4
from activity5.pactivity import run_activity as run_activity5
from activity1 import *
# project=None
# with open('activity1/config.txt', 'r') as f:
#             data = json.load(f)
# project=data["project_name"]
# function=data["function_name"]
# print(function)

# globals()[function]()


def run(activity):
    if activity=="activity1":
        run_activity1()
    elif activity=="activity2":
        run_activity2()
    elif activity=="activity3":
        run_activity3()
    elif activity=="activity4":
        run_activity4()
    elif activity=="activity5":
        run_activity5()