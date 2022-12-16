# Individual Assignment: Bayes Filter

Consider a household robot equipped with a camera. It operates in an apartment with two rooms: a living room and a bedroom. The robot runs an artificial neural network that can recognize a living room in the camera image. Further, the robot can perform a switch-room action, i.e., it moves to the living room if it is in the bedroom, and vice versa. Neither the recognition nor the motion controller is perfect. 

From previous experience, you know that the robot succeeds in moving from the living room to the bedroom with a probability of 0.7, and with a probability of 0.8 in the other direction:

p(x_t+1 = bedroom | x_t = living room, u_t = switch-room) = 0.7
p(x_t+1 = living room | x_t = bedroom, u_t = switch-room) = 0.8


The probability that the neural network indicates that the robot is in the living room although it is in the bedroom is given by p(z = living room| x = bedroom) = 0.3  , and the probability that the network correctly detects the living room is given by p(z = living room| x = living room) = 0.9.

Unfortunately, you have no knowledge about the current location of the robot.
However, after performing the switch-room action, the neural network indicates that the robot is not in the living room. After performing the switch-room action for the second time, the network again indicates not seeing a living room.

A. Use the Bayes filter algorithm to compute the probability that the robot is in the bedroom after performing the two actions. Use an appropriate prior distribution and justify your choice.
B. Which prior minimizes that probability? Briefly explain your answer.


# Group Assignment: Bayes Filter Assumptions

The recursive Bayes filter is a mathematical model, and as with all models, it is an idealized approximation of the real world.

For example, the Markov property is assumed. From that property, it follows that the measurement z_t is independent of all previous measurements given the state x_t. Can you think of an example in which a previous measurement actually interferes with the current one in the real world? You may also consider sensors other than LiDARs, for example, sonar sensors. Please describe such a situation in 2-3 sentences.

Further, find two other examples that show the difficulty of implementing a perfect Bayes filter in a real-world scenario and describe each in a couple of sentences. There are several hints in the slides.