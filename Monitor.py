_Author_ = "Karthik Vaidhyanathan"

import socket
from datetime import datetime
from datetime import timedelta
from Initializer_Class import Initialize
from Custom_Logger import logger
import json
import traceback
from Analyzer import Analyzer
from Knowledge import Knowledge


knowledge_obj = Knowledge()

# This is reponsible for continously fetching data from the SWIM simulator

start_adaptation = False
server_add_flag = False
server_remove_flag = False

init_obj = Initialize()
analyzer_obj = Analyzer()

class Monitor():


    def continous_monitoring(self):
        # The function continously monitors the data
        logger.info("running the adaptation effector module")
        start_time = datetime.now()
        new_time = datetime.now() + timedelta(minutes=1)
        monitor_dict = {} # This has to be sent to the analyze activity
        while (1):
            if (new_time - start_time).seconds >= 60:
                try:
                    print((new_time - start_time).seconds)
                    host = init_obj.host
                    port = init_obj.port  # The same port as used by the server
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    conn = s.connect((host, port))

                    s.sendall(b'get_basic_rt')
                    data = s.recv(1024)
                    response_time_base = str(data.decode("utf-8"))



                    s.sendall(b'get_opt_rt')
                    data = s.recv(1024)
                    response_time_opt = str(data.decode("utf-8"))

                    response_time = (float(response_time_base) + float(response_time_opt)) / 2.0
                    print (" Response time", response_time)
                    monitor_dict["response_time"] = response_time

                    # Get the arrival rate in the last 60 seconds

                    s.sendall(b'get_arrival_rate')
                    data = s.recv(1024)
                    arrival_rate = float(str(data.decode("utf-8")))
                    monitor_dict["arrival_rate"]  = arrival_rate


                    # get the dimmer value
                    s.sendall(b'get_dimmer')
                    data = s.recv(1024)
                    dimmer_value = float(str(data.decode("utf-8")))

                    print (" current dimmer ", str(dimmer_value))
                    monitor_dict["dimmer_value"] = dimmer_value


                    # Get the active number of servers in the system
                    s.sendall(b'get_active_servers')
                    data = s.recv(1024)
                    server_in_use = int(str(data.decode("utf-8")))
                    monitor_dict["active_servers"] = server_in_use
                    s.close()

                    # sending the monitored values to the Analyzer class

                    # the knowledge object will be the connection object inside analyzer
                    analyzer_obj.perform_analysis(monitor_dict,conn) # This will pass the control to the next class


                except Exception as e:
                    logger.error(e)
                    traceback.print_exc()

                start_time = datetime.now()

            new_time = datetime.now()

if __name__ == '__main__':
    monitor_obj = Monitor()
    monitor_obj.continous_monitoring()