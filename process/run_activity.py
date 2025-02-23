try:
    from activity1.pactivity import run_activity as run_activity1
except:
    run_activity1=0
try:
    from activity2.pactivity import run_activity as run_activity2
except:
    run_activity2=0
try:
    from activity3.pactivity import run_activity as run_activity3
except:
    run_activity3=0
try:
    from activity4.pactivity import run_activity as run_activity4
except:
    run_activity4=0
try:
    from activity5.pactivity import run_activity as run_activity5
except:
    run_activity5=0
from process.route_activity import route_activity
def run(project_name):
	A=route_activity(project_name)
	if A=='activity1':run_activity1(A)
	elif A=='activity2':run_activity2(A)
	elif A=='activity3':run_activity3(A)
	elif A=='activity4':run_activity4(A)
	elif A=='activity5':run_activity5(A)
