
class Memory_Leak_Config:

    memory_leak_delay = None
    trigger_threshold = None
    memory_threshold = None
    additional_details = None

    @staticmethod
    def get_memory_leak_delay():
        return Memory_Leak_Config.memory_leak_delay

    @staticmethod
    def set_memory_leak_delay(x):
        Memory_Leak_Config.memory_leak_delay = x

    @staticmethod
    def get_trigger_threshold():
        return Memory_Leak_Config.trigger_threshold

    @staticmethod
    def set_trigger_threshold(x):
        Memory_Leak_Config.trigger_threshold = x

    @staticmethod
    def get_memory_threshold():
        return Memory_Leak_Config.memory_threshold

    @staticmethod
    def set_memory_threshold(x):
        Memory_Leak_Config.memory_threshold = x

    @staticmethod
    def get_additional_details():
        return Memory_Leak_Config.additional_details

    @staticmethod
    def set_additional_details(x):
        Memory_Leak_Config.additional_details = x
