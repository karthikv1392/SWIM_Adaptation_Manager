_Author_ = "Karthik_Vaidhyanathan"


# Initalizing all basic configurations

from configparser import ConfigParser
import traceback
from Custom_Logger import logger

CONFIG_FILE = "settings.conf"
CONFIG_SECTION = "settings"
CONFIG_SECTION_SWIM = "swim"
CONFIG_SECTION_ADAPTATION = "adaptation"


class Initialize():
    def __init__(self):
        try:
            parser = ConfigParser()
            parser.read(CONFIG_FILE)

            # Swim related configurations
            self.host = parser.get(CONFIG_SECTION_SWIM, "host")
            self.port = int(parser.get(CONFIG_SECTION_SWIM,"port"))

            self.adaptation_type = parser.get(CONFIG_SECTION_ADAPTATION,"adaptation_type")
            self.swim_time_interval = int(parser.get(CONFIG_SECTION_ADAPTATION,"swim_time_interval"))
            self.r_opt = int(parser.get(CONFIG_SECTION_ADAPTATION,"r_opt_value"))
            self.r_man = int(parser.get(CONFIG_SECTION_ADAPTATION,"r_man_value"))

            self.swim_max_servers = int(parser.get(CONFIG_SECTION_ADAPTATION,"swim_max_servers"))
            self.swim_k_value =  int(parser.get(CONFIG_SECTION_ADAPTATION,"swim_k_value"))
            self.swim_response_time_threshold = float(parser.get(CONFIG_SECTION_ADAPTATION,"response_time_threshold"))
            self.swim_response_base_time = float(parser.get(CONFIG_SECTION_ADAPTATION,"response_time_base_threshold"))
            self.swim_latency =  int(parser.get(CONFIG_SECTION_ADAPTATION,"latency"))
            self.adaptation_db = parser.get(CONFIG_SECTION_ADAPTATION,"db_file")


        except Exception as e:
            traceback.print_exc()
            logger.error(" Error in Initializer, configurations parsing error")
            logger.error(e)

