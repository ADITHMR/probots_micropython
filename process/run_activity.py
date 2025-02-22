from activity1.pactivity import run_activity as run_activity1
from activity2.pactivity import run_activity as run_activity2
from activity3.pactivity import run_activity as run_activity3
from activity4.pactivity import run_activity as run_activity4
from activity5.pactivity import run_activity as run_activity5
from process.route_activity import route_activity
def run(project_name):
	A=route_activity(project_name)
	if A=='activity1':run_activity1(A)
	elif A=='activity2':run_activity2(A)
	elif A=='activity3':run_activity3(A)
	elif A=='activity4':run_activity4(A)
	elif A=='activity5':run_activity5(A)
