""" Activity Selection problem using Greedy Algorithm 
	
	You are given n activities with their start and finish times. 
	Select the maximum number of activities that can be performed by a 
	single person, assuming that a person can only work on a single 
	activity at a time.
"""

import unittest

def activity_selection(activities):
	""" Returns a list of activities which should be selected
		
		activities: an array of tuples [(start, finish), (...), ...]
	"""
	# base case
	if len(activities) < 1:
		return []

	# sorts the activities by their finishing time
	sorted_activities = sorted(activities, key=lambda x:x[1])
	todo = [sorted_activities[0]]

	for i in range(1, len(sorted_activities)):
		if todo[-1][1] <= sorted_activities[i][0]:
			todo.append(sorted_activities[i])

	return todo


class TestActivitySelection(unittest.TestCase):
	""" Test cases for activity selection """

	def test_empty_list(self):
		todo = activity_selection([])
		assert todo == []

	def test_single_activity(self):
		todo = activity_selection([(10, 30)])
		assert todo == [(10, 30)]

	def test_two_activities1(self):
		todo = activity_selection([(10, 30), (15, 40)])
		assert todo == [(10, 30)]

	def test_two_activities2(self):
		todo = activity_selection([(10, 30), (32, 50)])
		assert todo == [(10, 30), (32, 50)]

	def test_mulitple_activities1(self):
		todo = activity_selection([(10, 20), (12, 25), (20, 30)])
		assert todo == [(10, 20), (20, 30)]

	def test_multiple_activities(self):
		todo = activity_selection([(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)])
		assert todo == [(1, 2), (3, 4), (5, 7), (8, 9)]


if __name__ == "__main__":
	unittest.main()