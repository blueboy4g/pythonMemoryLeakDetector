import threading
import time
from multiprocessing.managers import BaseManager
import tkinter as tk
from tkinter import *
from MemoryLeakDetectionPrototype.adapters.memory_leak_scanner import analyze
from MemoryLeakDetectionPrototype.config.memory_leak_config import Memory_Leak_Config

#TESTING SCENARIOS
from MemoryLeakDetectionPrototype.code_comparison.plag import plag
from MemoryLeakDetectionPrototype.code_comparison.unique import unique
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_1 import start_memory_leak_1
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_2 import start_memory_leak_2
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_3 import start_memory_leak_3
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_4 import start_memory_leak_4
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_5 import start_memory_leak_5
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_6 import start_memory_leak_6
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_7 import start_memory_leak_7
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_8 import start_memory_leak_8
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_9 import start_memory_leak_9
from MemoryLeakDetectionPrototype.memory_leak_tests.memory_leak_10 import start_memory_leak_10

class Memory_Detector_App:

    def __init__(self, root):
        super().__init__()
        self.root = root
        memory_leak_config = manager.Memory_Leak_Config()
        self.config = memory_leak_config
        self.setup_gui()
        self.create_widgets()
        self.build_gui()

    def setup_gui(self):
        root.title('Prototype')

    def create_widgets(self):
        self.left_side_section = tk.Frame()
        self.right_side_section = Frame()
        self.left_side_section_bottom = Frame()
        self.right_side_section_bottom = Frame()
        self.button_border = tk.Frame(root, highlightbackground="black", highlightthickness=2, bd=0)

        self.window_name = Label(text="Memory Leak Prototype", font='Helvetica 12 bold')
        self.prototype_label = Label(text="Delay for memory leak snapshots in seconds:")
        self.prototype_label1 = Label(text="Threshold for number of triggers to cause alert:")
        self.prototype_label2 = Label(text="Threshold for memory variance (in KB):")
        self.debug_tools = Label(text="Run Additional Analytics", font='Helvetica 12 bold')
        self.small_spacer_1 = Label(text='', font="Helvetica 3 bold")
        self.small_spacer_2 = Label(text='', font="Helvetica 1 bold")
        self.blank_spacer = Label(self.right_side_section_bottom, text='', font="Helvetica 9 bold")
        self.quit_gui_button = Button(self.right_side_section_bottom, text="Quit", width=16, height=2)
        self.stop_gui_button = Button(self.left_side_section_bottom, text="Stop", width=16, height=2)
        self.start_button = Button(self.button_border, text="Start Memory Leak Detector", width=28, height=5, bg='gray')

        self.run_additional_logs = IntVar()
        self.memory_leak_delay = Scale(root, from_=5, to=10000, orient=HORIZONTAL)
        self.trigger_threshold = Scale(root, from_=25, to=500, orient=HORIZONTAL)
        self.memory_threshold = Scale(root, from_=1, to=10000, orient=HORIZONTAL)
        self.analytics_check = Checkbutton(self.left_side_section, text="Run Additional Analytics", variable=self.run_additional_logs, onvalue=1,
                                          offvalue=0)

    def build_gui(self):
        print("Loading up gui...")
        root.attributes('-topmost', 'true')
        self.start_button.bind("<Button-1>", self.run_analyzer)
        self.stop_gui_button.bind("<Button-1>", self.stop_analyzer)
        self.quit_gui_button.bind("<Button-1>", self.quit_app)
        self.run_additional_logs.set(1)
        self.memory_leak_delay.set(10)
        self.trigger_threshold.set(30)
        self.memory_threshold.set(2)
        self.pack_and_start_gui()

    def pack_and_start_gui(self):
        self.window_name.pack()
        self.prototype_label.pack()
        self.memory_leak_delay.pack()
        self.prototype_label1.pack()
        self.trigger_threshold.pack()
        self.prototype_label2.pack()
        self.memory_threshold.pack()
        self.left_side_section.pack(anchor=W)
        self.right_side_section.pack(anchor=E)
        self.analytics_check.pack()
        self.button_border.pack()
        self.start_button.pack()
        self.stop_gui_button.pack()
        self.quit_gui_button.pack() #(padx=(6, 0), pady=(2, 10))
        self.small_spacer_1.pack()
        self.small_spacer_2.pack()
        self.left_side_section_bottom.pack(side=LEFT)
        self.right_side_section_bottom.pack(side=RIGHT)
        root.mainloop()

    def run_analyzer(self, event):
        print('Starting Detector...')
        #TODO all these
        self.config.set_memory_leak_delay(self.memory_leak_delay.get()) #time delay
        Memory_Leak_Config.set_memory_leak_delay(self.memory_leak_delay.get())
        print("Time delay between snapshots is set to: " + str(self.config.get_memory_leak_delay()))

        self.config.set_memory_threshold(self.memory_threshold.get()) #memory threshold
        Memory_Leak_Config.set_memory_threshold(self.memory_threshold.get())
        print("The memory threshold set to: " + str(self.config.get_memory_threshold()))

        self.config.set_trigger_threshold(self.trigger_threshold.get()) #trigger threshold
        Memory_Leak_Config.set_trigger_threshold(self.trigger_threshold.get())
        print("The threshold to alert user about memroy leak is set to: " + str(self.config.get_trigger_threshold()))


        self.config.set_additional_details(self.run_additional_logs.get()) #additional details
        Memory_Leak_Config.set_additional_details(self.run_additional_logs.get())
        print("The addition details are boolean set to: " + str(self.config.get_additional_details()))

        # Start the thread
        stop_event = threading.Event()
        self.start_detector_thread = threading.Thread(target=self.run_code, args=(stop_event,))
        self.start_detector_thread.start()

        self.start_script_thread = threading.Thread(target=self.run_memory_leak)
        self.start_script_thread.start()


    def stop_analyzer(self, event):
        pass

    def quit_app(self, event):
        root.destroy()

    def run_code(self, stop_event):
        analyze()

    def run_memory_leak(self):
        # start_time = time.time()
        # loop=2000
        # i=1
        # while i <= loop:
        #     plag.run()
        #     #unique.run()
        #     i+=1
        # unique.run()
        # time.sleep(2)
        #plag.run()
        start_memory_leak_10()
        # end_time = time.time()
        # print("Runtime:", end_time - start_time, "seconds")
        # time.sleep(10)
        # start_memory_leak_2()
        # start_memory_leak_3()
        # start_memory_leak_4()
        # start_memory_leak_5()

class MyManager(BaseManager):
    pass

if __name__ == "__main__":
    MyManager.register('Memory_Leak_Config', Memory_Leak_Config)
    manager = MyManager()
    manager.start()
    root = tk.Tk()
    app = Memory_Detector_App(root)
    time.sleep(1)
    root.mainloop()

