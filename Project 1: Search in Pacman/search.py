# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #declaring stack for storing frontiers
    frontier=Stack()
    
    #explored = dict()
    explored=dict()

    #stroring current state in a variable
    position = problem.getStartState()
    
    vertex = {"from":None,"to":None,"current_pos":position}
    frontier.push(vertex)

    #till frontier is not empty iterate to find path
    while not frontier.isEmpty():

        #popping next vertex from frontier stack
	vertex = frontier.pop()
        current_pos = vertex["current_pos"]

        #if already explored then go to next vertex
	if explored.has_key(current_pos): 
		continue
        explored[current_pos] = True
        
	#if goal is reached then break loop			
	if problem.isGoalState(current_pos): 
		break
        
	#if goal not reached then see for next available paths		
	for next_state in problem.getSuccessors(current_pos):
            	#if this vertex is not already explored then add it to frontier
	    	if not explored.has_key(next_state[0]):	#gives next state
                	next_vertex = {"from":vertex,"to":next_state[1],"current_pos":next_state[0]}
                	frontier.push(next_vertex)

    #array for storing actions
    actions=[]
    while vertex["from"] != None:
	actions.insert(0, vertex["to"])
        vertex = vertex["from"]
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #declaring queue for storing frontiers
    frontier=Queue()
    
    #explored = dict()
    explored=dict()

    #stroring current state in a variable
    position = problem.getStartState()
    
    vertex = {"from":None,"to":None,"current_pos":position}
    frontier.push(vertex)

    #till frontier is not empty iterate to find path
    while not frontier.isEmpty():

        #popping next vertex from frontier queue
	vertex = frontier.pop()
        current_pos = vertex["current_pos"]

        #if already explored then go to next vertex
	if explored.has_key(current_pos): 
		continue
        explored[current_pos] = True
        
	#if goal is reached then break loop			
	if problem.isGoalState(current_pos): 
		break
        
	#if goal not reached then see for next available paths		
	for next_state in problem.getSuccessors(current_pos):
            	#if this vertex is not already explored then add it to frontier
	    	if not explored.has_key(next_state[0]):	#gives next state
                	next_vertex = {"from":vertex,"to":next_state[1],"current_pos":next_state[0]}
                	frontier.push(next_vertex)

    #array for storing actions
    actions=[]
    while vertex["from"] != None:
        actions.insert(0, vertex["to"])
        vertex = vertex["from"]
    return actions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #declaring priority queue for storing frontiers
    frontier=PriorityQueue()
    
    #explored = dict()
    explored=dict()

    #stroring current state in a variable
    position = problem.getStartState()
    
    vertex = {"from":None,"to":None,"current_pos":position,"cost":0}
    frontier.push(vertex,vertex["cost"])

    #till frontier is not empty iterate to find path
    while not frontier.isEmpty():

        #popping next vertex from frontier priority queue
	vertex = frontier.pop()
        current_pos = vertex["current_pos"]
	current_cost = vertex["cost"]
	
        #if already explored then go to next vertex
	if explored.has_key(current_pos): 
		continue
        explored[current_pos] = True
        
	#if goal is reached then break loop			
	if problem.isGoalState(current_pos): 
		break
        
	#if goal not reached then see for next available paths		
	for next_state in problem.getSuccessors(current_pos):
            	#if this vertex is not already explored then add it to frontier
	    	if not explored.has_key(next_state[0]):	#gives next state
                	next_vertex = {"from":vertex,"to":next_state[1],"current_pos":next_state[0],"cost":next_state[2]+current_cost}
                	frontier.push(next_vertex,next_vertex["cost"])

    #array for storing actions
    actions=[]
    while vertex["from"] != None:
        actions.insert(0, vertex["to"])
        vertex = vertex["from"]
    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #declaring priority queue for storing frontiers
    frontier=PriorityQueue()
    
    #explored = dict()
    explored=dict()

    #stroring current state in a variable
    position = problem.getStartState()
    
    vertex = {"from":None,"to":None,"current_pos":position,"cost":0,}
    frontier.push(vertex,vertex["cost"]+heuristic(position,problem))

    #till frontier is not empty iterate to find path
    while not frontier.isEmpty():

        #popping next vertex from frontier priority queue
	vertex = frontier.pop()
        current_pos = vertex["current_pos"]
	current_cost = vertex["cost"]
	
        #if already explored then go to next vertex
	if explored.has_key(current_pos): 
		continue
        explored[current_pos] = True
        
	#if goal is reached then break loop			
	if problem.isGoalState(current_pos): 
		break
        
	#if goal not reached then see for next available paths		
	for next_state in problem.getSuccessors(current_pos):
            	#if this vertex is not already explored then add it to frontier
	    	if not explored.has_key(next_state[0]):	#gives next state
                	next_vertex = {"from":vertex,"to":next_state[1],"current_pos":next_state[0],"cost":next_state[2]+current_cost}
			
                	frontier.push(next_vertex,next_vertex["cost"]+heuristic(next_state[0], problem))

    #array for storing actions
    actions=[]
    while vertex["from"] != None:
        actions.insert(0, vertex["to"])
        vertex = vertex["from"]
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
