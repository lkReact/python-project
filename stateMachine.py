from state import State
import j2l.pytactx.agent as pytactx
import random
import event
import time
from typing import Self

class StateMachine(State):


  def __init__(self, agent: pytactx.Agent, availableStates: list[str] = []) -> None:
    self.__points: list[list[int]] = []
    self.__currentPoints: object = None

    self.__onFire = False

    self.__agent = agent
    super(StateMachine,self).__init__(*availableStates)

  def fireOnEnemy(self) -> Self:
    if(not self.__agent): return self
    if (self.__agent.distance > 0 or self.__agent.range.__len__() > 0):
          self.__onFire = True
          self.__agent.fire(True)
          return self
  
    if(self.__onFire):
        self.__onFire = False
        self.__agent.fire(False)
    return self

  def moveAgent(self, x, y) -> Self:
    if(self.__agent):
       self.__agent.moveTowards(x, y)
       time.sleep(0.2)
    return self
  
  @property
  def agent(self):
     return self.__agent;

  @property
  def points(self):
     return self.__points;

  @property
  def currentPoints(self):
     return self.__currentPoints;

  def generateRandomPoints(self) -> Self:
    if(not self.__agent): return self;
    self.__points = [[
      random.randint(1, self.__agent.gridRows - 2),
      random.randint(1, self.__agent.gridColumns - 2)
    ] for x in range(random.randint(4, 8))]

  def followAndFireOnEnemy(self) -> Self:
    if(not self.__agent or self.__agent.range.__len__() <= 0): return self;
    self.__agent.setColor(128,92,92)
    lockedEnemy =  [*self.__agent.range.items()][0][1]

    while  self.__agent.range.__len__()  > 0 or (self.agent.x != lockedEnemy["x"] or self.agent.y != lockedEnemy["y"]):
      self.fireOnEnemy()
      if(not self.__onFire):
          self.moveAgent(lockedEnemy["x"],lockedEnemy["y"])
      self.agent.update();


     
  def moveToRandomPoint(self) -> Self:
      self.__agent.setColor(92,92,128)
      if(not self.__agent): return self;
      if(not self.__currentPoints):
        self.__currentPoints = {"index": 0,"points": self.__points[0]}
      else:
        newCurrentPointIndex = self.__currentPoints["index"] + 1
  
        if(newCurrentPointIndex == (self.__points.__len__()-1)):
             self.generateRandomPoints();
             newCurrentPointIndex = 0
        newCurrentPoint = self.__points[newCurrentPointIndex]
        self.__currentPoints = {"index": newCurrentPointIndex,"points": newCurrentPoint}
      
      while  (self.agent.x != self.__currentPoints["points"][0] or self.agent.y != self.__currentPoints["points"][1]):
            if (self.__agent.range.__len__() > 0):
                return self;
            self.moveAgent(*self.__currentPoints["points"])
            self.agent.update();
            if (self.__agent.range.__len__() > 0):
                return self;
      
      return self;

  def joinServer(self,playerId, area,login,password,server) -> Self:
    if(self.__agent):
       return self;
  
    self.__agent = pytactx.Agent(playerId=playerId,
                      arena=area,
                      username=login,
                      password=password,
                      server=server,
                      verbosity=2)
    
    event.subscribe(self.__agent)
    self.generateRandomPoints();
    
    return self;

  


