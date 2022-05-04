_Author_ = "Karthik Vaidhyanathan"

from Custom_Logger import logger

from Initializer_Class import Initialize
# This class calculates the total utlity values

init_obj = Initialize()


class Utility_Evaluator():
    def __init__(self,server_in_use,arrival_rate,dimmer_value):
        self.s_star = 3 # the maximum number of servers
        self.server_in_use = server_in_use
        self.arrival_rate = arrival_rate
        self.dimmer_value = dimmer_value
        self.time_interval = 60
        self.cost = 1

    def calculate_utility(self):
        # Calcuate the two utility of cost and revenue here
        logger.info("calculating the utility values")
        U_rt = self.time_interval * self.arrival_rate * (self.dimmer_value * init_obj.r_opt + (1 - self.dimmer_value) * init_obj.r_man)
        U_ct = self.time_interval * self.cost * (self.s_star - self.server_in_use)
        U_rt_star = self.arrival_rate * self.time_interval * init_obj.r_opt
        return U_rt, U_ct, U_rt_star