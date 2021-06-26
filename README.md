# Python-Virtual-Robot-Representation

These four python files represent the operations of a "robot" that runs through a set of actions. Instead of controlling robot arms, the program just prints out the actions as they are preformed.

The robot must assemble kits in a factory consisting of red, green, and blue parts. To do so, it receives user inputs to determine the number of parts in the storage bins that it pulls from, the number of parts already in the kits, and the number of parts left to be placed in the kits. Then, it runs through a series of actions based on these inputs.

The actions the robot can do are as follows:
  1. Grip an item with one or both robot arms
  2. Move to and from the home, bin, or kit positions
  3. Place an item in a kit assembly

Using these actions and some calculations, the motion of the robot can be simulated and communicated by text.

Future iterations of this program can take the actions developed here and connect them to robotic systems either in ROS or in real-world applications to represent what the robot would actually do.
