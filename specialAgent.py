from state import State
from typing import Self
from stateMachine import StateMachine
import random
import time
import j2l.pytactx.agent as pytactx
import event

class SpecialAgent(StateMachine):

  def __init__(self,playerName:str, availableStates: list[str] = []) -> None:
    self.__playerInfo = { 
       "playerId": playerName,
       "currentPoint": [0,0]
      };
    self.__startedTracking = False
    super(SpecialAgent,self).__init__(None,availableStates)
    self.__stateMachine = super(SpecialAgent,self);
  

  @property
  def agent(self):
     return self.__stateMachine.agent;

  @agent.deleter
  def agent(self):
    del self.__stateMachine.agent;

    # event.unSubscribe(self.__agent)
  
  def stopTracking(self):
     self.__startedTracking = False
     
  def startTracking(self) -> Self:
    self.__startedTracking = True
    while  self.__startedTracking:
      if(not  self.__startedTracking):
        return self
      
      self.__stateMachine.moveToRandomPoint();
      if(not  self.__startedTracking):
         return self
      self.__stateMachine.followAndFireOnEnemy();
      
    return self
        
        

  def joinServer(self,area,login,password,server) -> Self:
    if(self.__stateMachine.agent):
       return self;
  
    self.__playerInfo["area"] = area
    self.__playerInfo["login"] = login
    self.__playerInfo["password"] = password
    self.__playerInfo["server"] = server
    self.__stateMachine.joinServer(self.__playerInfo["playerId"],area,login,password,server).generateRandomPoints();
    
    return self;


