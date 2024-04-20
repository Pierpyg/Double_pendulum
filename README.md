# Double Pendulum
#### Description:
#### Overwiew:

This program simulates a double pendulum in motion. After starting the program from the terminal, eight questions will appear on the screen. These questions relate to the initial conditions of the two pendulums, such as length, mass, initial angle, and initial angular velocity. Then, the program will calculate the angular acceleration of the two pendulums, integrate the result over a time interval, and return the animation of the two pendulums.

#### File:

##### 'project.py'

This is the main program, which I described in the Overview. At the beginning, the imported libraries are listed to ensure that the program functions: numpy, matplotlib, and scipy. Then, the four functions into which the program is divided are presented in order: 'main', 'create_animation', 'derivative', 'integrate'.

In 'main', there are the questions to ask the user, and a call to the 'integrate' function and one to the 'create_animation' function are made. Where the result of 'integrate' is solution and from the latter the animation is created; furthermore, 'main' is also divided into sub-functions: 'get_positive_float', 'get_angle', 'get_number'. 'get_positive_float' refers to the lengths and masses of the pendulums and serves to verify that the user's input is a positive number and not a letter or negative number, or zero. 'get_angle' refers to the initial angles of the two pendulums and serves to verify that the user's input is a number between -180 and 180 (I preferred this interval to 0-360 because I find it more intuitive), other numbers or letters are not acceptable. 'get_number' refers to the initial angular velocities, these have as the only condition being numbers. 'create_animation' is used to create the figure that will be animated, so a Cartesian reference system is created with the four quadrants, the axis length is equal to the sum of the lengths of the two pendulums, in this way regardless of the values of the pendulums, the graph will always contain them. I created two lines to represent the pendulums, of different and random colors to distinguish them. Within this function, there are two functions 'init' and 'animate', the first initializes black lines in the graph and the second calculates the position of the two pendulums, they are set up so that the end of the first pendulum coincides with the beginning of the second, in the end everything is animated, I set the values so that the animation is at 60 fps.

In 'derivative', the formulas are present that allow us to obtain the angular acceleration of the two pendulums, assuming that we are on Earth, I did not remember the formulas in question, so I helped myself both with a search on the internet and with the help of ChatGPT, however, I am not sure they are correct, but the program works. I will correct the program if I notice an error.

In 'integrate', the values obtained in 'derivative' are integrated over a time interval 0-20.

##### 'test_project.py'

Since the values are chosen by users to test the validity of the program, I have pre-set values for the lengths, masses, initial angles, and angular velocities of the two pendulums using the 'sample_solution' function. Meanwhile, the other three functions, 'test_create_animation', 'test_integrate', and 'test_derivate', test the respective functions in 'project.py' using the data from 'sample_solution' and create an animation.

##### 'requirements.txt'

The libraries to install in order to make the program work.
