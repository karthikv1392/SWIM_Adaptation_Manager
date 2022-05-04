_Author_ = "Karthik Vaidhyanthan"

from Initializer_Class import Initialize
from Custom_Logger import logger
from Planner import Planner
# Analyzes the data to check if the reponse time is above the threshold
# When using machine learning this will use the ML models to predict the expected reponse time


init_obj = Initialize()

class Analyzer():
    def __init__(self):
        self.threshold = init_obj.swim_response_time_threshold
        self.count = 0


    def perform_analysis(self,monitor_dict,connection_obj):
        logger.info("Inside the Analyzer: Performing the analysis")
        monitor_response_time =  monitor_dict["response_time"]


        if monitor_response_time > self.threshold:
            logger.info(" The response time above threshold -- Initializing Planner")
            # call the planner class object
            server_in_use = monitor_dict["active_servers"]
            arrival_rate = monitor_dict["arrival_rate"]
            dimmer_value = monitor_dict["dimmer_value"]
            self.count += 1  # To check the number of adaptations as well as to check if it is the first run of the approach
            plan_obj = Planner(monitor_response_time, server_in_use, arrival_rate, dimmer_value, connection_obj)
            plan_obj.generate_adaptation_plan(self.count)

        else:
            print (" Below threshold -- Check for revenue")