from idlestate import IdleState
from processingstate import ProcessingState
from dispensingstate import DispensingState
from outofservicestate import OutOfServiceState

class VendingMachine:
    def __init__(self):
        self.__idle_state = IdleState(self)
        self.processing_state

