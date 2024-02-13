
from getpass import getpass
import time
import j2l.pytactx.agent as pytactx
from math import sqrt
import threading
import random
import string
import event
import random
from specialAgent import SpecialAgent

specialAgent = SpecialAgent("Rab");

specialAgent.joinServer("LaTerreDuMilieu","demo", "demo", "mqtt.jusdeliens.com")


specialAgent.startTracking();
