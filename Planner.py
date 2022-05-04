_Author_ = "Karthik Vaidhyanathan"

# The class for planning. This uses RL for selecting the actions

from Custom_Logger import logger
from Initializer_Class import Initialize
from Utility_Evaluator import Utility_Evaluator
from Executor import Executor
import json
import datetime
from datetime import datetime

'''
Possible actions are adaptation options which include
1. Add Server
2. Remove Server
3. increase dimer by 0.25
4. decrease dimer by 0.25
5. do nothing
6. Add server and increase dimer by 0.25
7. Add server and decrease dimer by 0.25
8. Remove server and increase dimer by 0.25
9. Remove server and decrease dimer by 0.25
'''

class Planner():

    def __init__(self,response_time,server_in_use, arrival_rate,dimmer_value,connection_obj):
        self.response_time = response_time
        self.server_in_use = server_in_use
        self.arrival_rate = arrival_rate
        self.dimmer_value = dimmer_value
        self.connection_obj = connection_obj


    def generate_adaptation_plan(self,count):
        # Use the reinforceer to generate the adaptation plan
        logger.info("Inside the planner: Generating the adaptation plan")

        util_obj = Utility_Evaluator(self.server_in_use,self.arrival_rate,self.dimmer_value)
        U_rt, U_ct, U_rt_star = util_obj.calculate_utility()

        # Check if server can be added

        adap_status_json = {}
        with open("adap_status.json", "r") as json_file:
            adap_status_json = json.load(json_file)

        server_add_time_string = adap_status_json["server_added_time"]
        server_count = adap_status_json["current_server_count"]
        server_added_time = datetime.strptime(server_add_time_string, '%Y-%m-%d %H:%M:%S')
        current_time = datetime.now()

        server_add_flag = True
        # Check if a server can be added by considering the latency of server addition
        if (current_time - server_added_time).seconds >= 80:
            server_add_flag = False

        # Check if dimmer can be increased or decreased
        dimmer_increase = True
        dimmer_decrease = True

        logger.info("Current dimmer value " + str(self.dimmer_value))

        if self.dimmer_value == 1.0:
            dimmer_increase = False
        elif self.dimmer_value == 0.0:
            dimmer_decrease = False

        print (" dimmer flag status, increase : decrease " + str(dimmer_increase) + " : " + str(dimmer_decrease))
        logger.info(" dimmer flag status, increase : decrease " + str(dimmer_increase) + " : " + str(dimmer_decrease))

        action = 0
        # Using a simple rule based approach for performing adaptation
        if server_count < 3 and server_add_flag is False:
            if dimmer_decrease is True:
                action = 7 # Add server and decrease dimmer
            elif dimmer_decrease is False:
                action = 1  # add server

        elif server_add_flag is True or server_count >= 3:
            if dimmer_decrease is True:
                action = 3
            elif dimmer_decrease is False:
                # There is nothing to be done cannot add server or cannot reduce dimmer
                action = 5





        execute_obj = Executor(self.dimmer_value,self.server_in_use,self.connection_obj)

        execute_obj.adaptation_executor(action)

        print (" Adaptation executed ")



