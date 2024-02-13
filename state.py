from typing import Union

class State(object):
  globalState = []
  instances = []

  @staticmethod
  def addNewGlobalStates(*states:list[str], spread:bool=False):
      try:
        for state in states:
            State.globalState.append(state);
            if(spread):
              for instance in State.instances:
                  instance.addNewState(state)
        return True
      except:
         return False
  
  @staticmethod
  def removeGlobalStates(*states: list[str], spread:bool=False):
      try:
        for state in states:
            indexStates = list(filter(lambda state: state != None, [index if globalState == state else None for index,globalState in enumerate(State.globalState)]))
            for indexState in indexStates:
              del State.globalState[indexState];
              if(spread):
                for instance in State.instances:
                    instance.removeState(state)   
        return True
      except:
         return False
  
  
  @staticmethod
  def isSameState(state0, state1) -> bool:
     if(not isinstance(state0,State) or not isinstance(state1, State)): return False;
     return state0.currentState == state1.currentState;

  def __init__(self, *availableStates: list[str]) -> None:
    self.__states = {*availableStates}
    self.currentState = None
    State.instances.append(self);
    pass

  @property
  def states(self):
      return self.__states

  @states.deleter
  def states(self):
      del self.__states
      self.__states = [*State.globalState]

  def setCurrentState(self, state): 
     try:
      stateIndex = self.__states.index(state)
      if(stateIndex or stateIndex == 0):
          self.currentState = state
      return self;
     except:
      return self;

  def pushStates(self, *states):
      try:
        if(isinstance(states[0],State)):  
            self.__states = [ *states[0].states ];
            return;
        self.__states = [*self.__states, *states ];
        return True
      except:
         return False
  
  def popStates(self,*states:list[str]):
      try:
        for state in states:
          indexStates = list(filter(lambda state: state != None, [index if currentState == state else None for index,currentState in enumerate(self.__states)]))
          for indexState in indexStates:
              del self.__states[indexState]
        return True
      except:
         return False

