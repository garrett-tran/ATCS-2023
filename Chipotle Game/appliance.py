from fsm import FSM
class Appliance:
    #States
    COOKING = "ck"
    READY = "rdy"
    EMPTY = "mt"

    #Inputs
    START_COOKING = "sc"
    PICK_UP = "pu"

    def __init__(self, time, food, name):
        self.time = time 
        self.food = food
        self.name = name

        self.fsm = FSM(self.EMPTY)
        self.init_fsm()

    def init_fsm(self):
        """
        Adds all states to the FSM
        """
        

    def cook(self):
        self.fsm.process(self.START_COOKING)

    def pick_up(self):
        self.fsm.process(self.PICK_UP)