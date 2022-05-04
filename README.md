# SWIM_Adaptation_Manager
A Simple external adaptation manager for the SWIM exemplar written using Python


## Installing SWIM
The SWIM exemplar is available in a Docker container. It can be installed by following the installation process described [here]https://github.com/cps-sei/swim#installation---install-docker) in the offical repository of SWIM. Make sure the port 4242 is mapped to the local port when running the SWIM container.

## Running SWIM to allow External Adaptation 

1. Once installed SWIM can be accessed via http://localhost:6901
2. Run SWIM in the external adaptation manager mode by following this [link](https://github.com/cps-sei/swim#how-to-run-simulation-with-another-external-adaptation-manager)

## Running SWIM_Adaptation_Manager

1. Clone this repository. Ensure that Python 3.7 is installed
2. Edit the host field in settings.conf file.
3. Once SWIM is running, start Monitor.py. This will run the adaptation engine
