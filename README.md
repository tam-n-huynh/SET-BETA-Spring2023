HOW TO RUN THESE NODES
I began made these nodes and here I'm explaining how to run them and how they connect as far as I understand.

- Have ROS2 installed and call the local setup script "local_setup.bat"
- Navigate to ros2_ws folder and do "colcon build --merge-install"
	- This builds the available packages available in the folder
- Same folder, do "call install/setup.bat"
	- needed to identify packages and nodes
- Do "ros2 run [package name] [entry point]"
	- The file "setup.py" in the package folder labels entry points which are nodes
	- At this point, the package 'publisher' should be built from the colcon command
	- If I wanted to run the publisher node, I would do "ros2 run publisher talker"
	- 'talker' is the name of the entry point for the publisher_function node
	- If I wanted to run the servo node, I would do "ros2 run publisher servos"
	- 'servos' is the name of the entry point for the shoulder_servos node
- These nodes should be deployed in separate cmd shells
	- When both 'talker' and 'servos' are running, talker should be publishing a loop of 0, 45, 0, 45 and servos is able to read it. 
	- code for shoulder_servos is sending serial data to the arduino through COM15 port, arduino is coded to recieve serial data and change the angle of servo motor