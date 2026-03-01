# Drive Like a Human: Rethinking Autonomous Driving with Large Language Models

**Authors:** Daocheng Fu, Xin Li, Licheng Wen, Min Dou, Pinlong Cai, Botian Shi, Yu Qiao

**Date:** 2023-07-14


## Abstract

In this paper, we explore the potential of using a large language model (LLM) to understand the driving environment in a human-like manner and analyze its ability to reason, interpret, and memorize when facing complex scenarios. We argue that traditional optimization-based and modular autonomous driving (AD) systems face inherent performance limitations when dealing with long-tail corner cases. To address this problem, we propose that an ideal AD system should drive like a human, accumulating experience through continuous driving and using common sense to solve problems. To achieve this goal, we identify three key abilities necessary for an AD system: reasoning, interpretation, and memorization. We demonstrate the feasibility of employing an LLM in driving scenarios by building a closed-loop system to showcase its comprehension and environment-interaction abilities. Our extensive experiments show that the LLM exhibits the impressive ability to reason and solve long-tailed cases, providing valuable insights for the development of human-like autonomous driving. The related code are available at https://github.com/PJLab-ADG/DriveLikeAHuman .


---


## Full Text

<!-- Page 1 -->
Drive Like a Human: Rethinking Autonomous Driving
with Large Language Models
Daocheng Fu1∗
Xin Li1,2∗
Licheng Wen1∗
Min Dou1
Pinlong Cai1
Botian Shi1† Yu Qiao1
1Shanghai AI Lab, 2East China Normal University
{fudaocheng, lixin, wenlicheng, doumin, caipinlong, shibotian, qiaoyu}@pjlab.org.cn
Abstract
In this paper, we explore the potential of using a large language model (LLM) to
understand the driving environment in a human-like manner and analyze its ability
to reason, interpret, and memorize when facing complex scenarios. We argue that
traditional optimization-based and modular autonomous driving (AD) systems
face inherent performance limitations when dealing with long-tail corner cases.
To address this problem, we propose that an ideal AD system should drive like a
human, accumulating experience through continuous driving and using common
sense to solve problems. To achieve this goal, we identify three key abilities
necessary for an AD system: reasoning, interpretation, and memorization. We
demonstrate the feasibility of employing an LLM in driving scenarios by building
a closed-loop system to showcase its comprehension and environment-interaction
abilities. Our extensive experiments show that the LLM exhibits the impressive
ability to reason and solve long-tailed cases, providing valuable insights for the
development of human-like autonomous driving. The related code are available at
https://github.com/PJLab-ADG/DriveLikeAHuman.
1
Introduction
Imagine if you are sitting behind the wheel waiting for the green light in front of a stop sign.
Meanwhile, a pickup truck carrying traffic cones is crossing the intersection ahead. As a human
driver, you can leverage your common sense knowledge to reason that these traffic cones are cargo on
a pickup truck, and it doesn’t mean the road is under construction. However, these scenarios, which
are easy for human drivers to handle, are long-tail corner cases for many existing autonomous driving
(AD) systems [6, 7, 8]. Although self-driving developers can address this case by hand-crafting rules
or collecting more data specifically about traffic cones on vehicles instead of on the ground to prevent
sudden braking, the algorithm would fail in the opposite cases when encountering on the ground
that marks a no-go zone. It’s like solving one problem only to find another cropping up, especially
with the infinite rare cases in the real world that are even beyond our imagination. This is why we
believe that traditional optimization-based and modular AD systems inherently face performance
bottlenecks [6, 17].
We rethink the storyboard of autonomous driving and clarify why conventional optimization-based
AD systems struggling with the challenging open world in Fig. 1 (a). Although the system that built
upon the optimization theory can easily divide the complex autonomous driving task into a set of
sub-tasks. The goal of optimizing the loss function tends to be trapped by local optimizations when
facing a complex scenario, which limits its generalization ability. Incorporating more data (green
*Equal contribution. Sorted alphabetically by surname.
†Corresponding author.
Preprint.
arXiv:2307.07162v1  [cs.RO]  14 Jul 2023

<!-- Page 2 -->
Human Driving Capability Domain
Known-
Safe
Known-
Unsafe
Unknown
-Unsafe
Collect 
More Data
Add Common 
Sense
Current Method 
Performance
Current Method 
Capability
Long-tailed 
Cases
(a)
(b)
Observation
Action
Evaluation
Feedback
Interaction flow
Reflection flow
Retrieve
Agent
Expert
Environment
Memory
Supervision flow
Condense
Figure 1: (a) The relationships between human driving and existing autonomous driving systems,
especially highlights the limitations of current approaches and why they cannot solve all long-tail
cases. (b) The schema of a system that can drive like a human. The agent can explore and interact
with the environment and conduct self-reflection based on the expert’s feedback, finally accumulating
the experience.
arrows in graph) can only reduce the performance gap between to current model (green ellipse) and
the maximum capacity of optimization-based methods (blue ellipse). This is mainly because the
optimization process focuses on learning the dominant patterns within the data, often overlooking
infrequent long-tail corner cases. Without the incorporation of common sense (blue arrows), the
capacity of the model (blue ellipse) cannot be prompted.
Moreover, there are always inexhaustible unknown long-tail cases during the continuous data collec-
tion. Compared with current solutions struggling to cope with these long-tail corner cases, humans
always can solve them with skill and ease via their experiences and common sense. A straightforward
idea comes out: Is it possible for us to make such a system that can drive like a human who
can accumulate experience through continuous driving instead of fitting the limited training
corpus?
According to the recent research [14, 32, 46, 39, 47], we think the previous modular AD systems can
be regarded as an Internet AI [7, 8, 23, 17] that is trained on task-specific corpus without advanced
intelligence like reasoning, interpretation and self-reflection. We claim that it is necessary to borrow
ideas from Embodied AI [31, 35] research if we want to get an agent that can drive a car like an
experienced human driver. Human learns to drive from interaction with the real environment and
gets feedback to refine the road sense by explaining, reasoning, and condensing the memory of
various scenarios and the corresponding operations. Furthermore, owing to their logical reasoning
ability, human drivers can use their common sense to summarize rules and apply them in more
general scenarios (inductive reasoning)[16]. Meanwhile, the previous experience can be aroused
subconsciously to handle unpredictable scenarios (deductive reasoning)[20].
Towards the goal of driving like a human, we identify three abilities that are necessary: 1) Reasoning:
Given a specific driving scenario, the model should be able to make decisions by reasoning via
common sense and experience. 2) Interpretation The decisions made by the agent should able to be
interpreted. This demonstrates the ability of introspection and the existence of declarative memory.
3) Memorization: After reasoning and interpreting scenarios, a memory mechanism is required to
remember previous experiences and enable the agent to make similar decisions once facing similar
situations.
Based on the above three properties, we refer to the paradigm of human learning to drive and condense
a canonical form of a driving system depicted in Fig. 1 (b). This schema includes four modules:
(1) Environment creates a stage that the agent can interact with by the interaction flow; (2) Agent
stands for a driver that can perceive the environment and make decisions utilizing its memory and
learning from expert advice; (3) Memory allows the agent to accumulate experience and perform
actions with it via the reflection flow; and (4) Expert provides advice on agent training and gives
feedback when it acts inconsistently, which forms the supervision flow. To be specific, as a universal
driving framework, the Environment, the Agent, and the Expert can be represented by the real world
or simulator, human drivers or driving algorithms, and simulator or instructor feedback, respectively.
Inspired by recent research, the large language model (LLM) can be considered as an early version of
Artificial General Intelligence (AGI)[4, 39, 47, 1, 34], owing to its remarkable emergent ability [40]
and new techniques like Instruct Following[27] and In-Context Learning (ICL)[3]. The extensive
2

<!-- Page 3 -->
GPT-3.5
GPT-3.5
Observaon
Percepon Tools

Get Available Acons

Get Available Lanes

Get Lane Involved Cars

……
Discrete Meta Acons

LANE_LEFT

IDLE

LANE_RIGHT

FASTER

SLOWER
Agent Prompts
 Chain of thoughts
 Traﬃc rules
 Decision cauons
 System message
 ……
Driving Environment
HighwayEnv
Thought 1: Since I am encounter such situ, the first thing to do is to 
check my available actions.
Act 1: Get_available_actions('ego')
Obs 1: [...] The vehicle can do IDLE, FASTER, SLOWER, LANE
CHANGE RIGHT actions. [...]
Thought 2: Now I need to check the status of 'ego' car.
Act 2: Get_available_lanes('ego')
Obs 2: [...] The 'ego' can drive on lane_3 and lane_2. Lane_3 is the 
curent lane and lane_2 is left lane.[...]
Thought 3: Now I need to check for acceleration action.
Act 3: Get_lane_cars('lane_3')
Obs 3: veh_6 is driving in front of 'ego' with 10.2m/s. [...]
Thought 4: I have to check if acceleration is safe with veh_6.
Act 4: Is_action_safe('acc','veh_6')
Obs 4:
Acceleration may be conflict with veh_6. [...]
Thought 8: [...] I suggest it's safe to keep lane with current speed
Act 8: Finish.
……
Final Answer:
Decision: IDLE
Explanation: Since the last step is ... I suggest...
(a)
(b)
Thought 5: Now I need to check for keep speed action.
Act 5: Get_lane_cars('lane_2')
Obs 5: veh_4 is driving in front of 'ego' with 13.89m/s on lane_2. [...]
Figure 2: GPT-3.5 closed-loop driving in HighwayEnv: (a) GPT-3.5 observes its environment in
HighwayEnv using perception tools and makes decisions to control vehicles, forming a closed
loop. (b) GPT-3.5 employs the ReAct strategy to plan actions and use tools, while perceiving its
surroundings through a cycle of thought, action, and observation
experimental results of recently released LLMs like ChatGPT [26] have demonstrated their ability of
reasoning, interpretation, and memorization [41]. Therefore, in this paper, we try to initially explore
the ability of LLM to understand driving traffic scenes like humans and analyze the LLM’s ability of
reasoning, interpretation and memorization in handling scenarios like long-tail corner cases through a
series of qualitative experiments. Specifically, we first build a closed-loop system to demonstrate the
comprehension and environment-interaction ability of an LLM (GPT-3.5) in driving scenarios. Then
we demonstrate the reasoning and memorization abilities by solving several typical long-tailed cases
that are difficult for modular AD systems to handle while easy for human drivers.
The main contributions of this paper are as follows:
1. We dive deep into how to make autonomous driving systems drive like a human to prevent
catastrophic forgetting of the existing AD systems when facing long-tail corner cases and
summarize into three key abilities to drive like a human: Reasoning, Interpretation and
Memorization.
2. We are the first to demonstrate the feasibility of employing LLM in driving scenarios and
exploit its decision-making ability in the simulated driving environment.
3. Extensive experiments in our study express impressive comprehension and the ability to
solve long-tailed cases. We hope that these insights will inspire academia and industry to
contribute to the development of human-like autonomous driving.
2
Closed-loop interaction ability in driving scenarios
The ability to interpret allows LLM to understand its driving environment, forming the basis for
its interaction with environments, and empowering its reasoning, and memorization abilities. We
conducted a closed-loop driving experiment on HighwayEnv* using GPT-3.5 to verify LLM’s
interpretation and environmental interaction abilities. As a text-only large language model, GPT-3.5
cannot directly interact with HighwayEnv, so we provided perception tools and agent prompts to
*https://github.com/Farama-Foundation/HighwayEnv
3

<!-- Page 4 -->
Figure 3: Driving behavior of RL-based and Search-based methods: (a) RL-based agents focus
solely on achieving the final reward, disregarding the intermediate steps. This allows them to take
unconventional actions, such as slowing down to fall behind other vehicles and then driving on an
open road to avoid collisions. (b) Search-based methods make decisions by optimizing objective
functions. They may pursue aggressive behavior by seeking max efficiency while ensuring safety.
aid its observation and decision-making. As shown in Fig. 2, the Agent Prompts provide GPT-3.5
with information about its current actions, driving rules, and cautions. GPT-3.5 employs the ReAct
strategy [42] to perceive and analyze its surrounding environment through a cycle of thought, action,
and observation. Based on this information, GPT-3.5 makes decisions and controls vehicles in
HighwayEnv, forming a closed-loop driving system.
Like humans, GPT-3.5 evaluates the potential consequences of its actions while driving and weighs
the outcomes to make the most sensible decision. Unlike widely used Reinforcement Learning
(RL)-based and Search-based approaches, GPT-3.5 not only interprets scenarios and actions but also
utilizes common sense to optimize its decision-making process.
Compared to the RL-based approach, GPT-3.5 achieve a zero-shot pass rate of over 60% in High-
wayEnv without any fine-tuning. In contrast, the RL-based approach is heavily dependent on
numerous iterations to achieve a competitive performance. For example, as Fig.3 (a) shows, due to the
severe penalty for collisions, the RL-based agent learned a policy that in order to prevent collisions it
will slow down at the beginning to create an extensive space for the subsequent accelerating. It shows
that the RL-based approach often produces such unexpected solutions.
The search-based approach makes decisions by optimizing an objective function, ignoring undefined
parts not mentioned in the function. As Fig.3 (b) shows, search-based agents may exhibit aggressive
lane changes to achieve high driving efficiency, thereby increasing the risk of collisions. Additionally,
the search-based approach may make meaningless lane changes even when no other vehicles are
ahead. This may be because, for search-based agents, lane changing and maintaining speed have equal
priority in the objective function under the premise of safety. As a result, the agent will randomly
choose one of the actions.
In summary, neither RL-based nor Search-based approaches can truly think and drive like humans
because they lack common sense, the ability to interpret scenarios, and the ability to weigh the
pros and cons. In contrast, GPT-3.5 can explain the consequences of each action, and by providing
prompts, we can make GPT-3.5 value-oriented and enable it to make more human-like decisions.
We present two examples that demonstrate the interpretation and interaction abilities of GPT-3.5 in
the HighwayEnv environment, as well as its consistency in decision-making during the closed-loop
process. The first case is depicted in Fig.4, involving a green ego car driving in the rightmost lane
lane_3. The ego car has been following its leading car veh4 on lane_3 for a while, while veh1 on
the left lane lane_2 has been travelling at a faster speed than veh4. GPT-3.5 then begins its ReAct
process. It first determines the actions that the ego car can currently perform, including accelerating,
decelerating, and maintaining speed in the current lane, as well as changing lanes to the left. However,
since the ego car is in the rightmost lane, it cannot continue to change lanes to the right. Next,
4

<!-- Page 5 -->
GPT-3.5
Thought 1: Ego car is currently in lane_3 with a speed of 16.02 and
its last decision was IDLE. [...] We need to check the acailable actions
for the ego car.
Act 1: Get_available_actions('ego')
Obs 1: [...] The ego car can take IDLE, FASTER, SLOWER, LANE
LEFT actions. [...]
Thought 2: I need to check the safety of the acceleration action with all
the vehicles affected by the decision.
Act 2: Is_acc_conflict_with('veh4')
Obs 2: Acceleration may be conflict with veh4.
Thought 3: Now I need to check the safety of the idle action with all
the vehicles affected by the decision.
Act 3: Is_idle_conflict_with('veh4')
Obs 3: Keep lane with current speed is safe with veh4.
···
Thought 8: Next, we need to compare the safety of all the possible
decisions and choose the safest one. We need to check the safety of
the lane change action to lane_2  with all the vehicles affected by the
decision. 
Act 8: Get_lane_invovled_car('lane_2')
Obs 8:  veh1 is driving on lane_2, and it's driving in front of ego car. 
Thought 9: We need to make sure that our lane change actions do not
conflict with veh1. 
Act 9: Is_lane_change_conflict('lane_2','veh1')
Obs 9:  Change lane to lane_2 is safe with veh1.
Thought 10: [...] we can choose the lane change action to `lane_2` as
the final decision.
Act 10: Finish.
Final Answer:
Decision: LANE_LEFT
Explanation: Changing to the left lane `lane_2` is
the safest decision. The idle action is also safe,
but changing lane can provide more flexibility and
avoid potential conflicts with other vehicles.
Acceleration is not safe with the presence of `veh4`.
lane_3
lane_2
lane_1
lane_0
veh4
veh1
ego
lane_3
lane_2
lane_1
lane_0
veh4
veh1
ego
Figure 4: The lane-change decision-making process by GPT-3.5
GPT-3.5
Thought 1: The ego car is currently in lane_3 with a speed of 15.42
and its last decision was FASTER. We need to check the available
actions and available lanes for the ego car. Then, we need to analyze
the possible actions and check their safety with all the vehicles affected
by the decision. [...]
Act 1: Get_available_actions('ego')
Obs 1: [...] The ego car can currently take IDLE, FASTER, SLOWER,
LANE _LEFT actions. [...]
···
Thought 3: I need to get the vehicles in the current lane first before
checking the safety of the acceleration action.
Act 3: Get_lane_invovled_car('lane_3')
Obs 3: veh2 is driving on lane_3, and it's driving in front of ego car.
You need to make sure that your actions do not conflict with each of the
vehicles mentioned.
Thought 4: Now that we know veh2 is in the same lane as the ego
car, we need to check the safety of the acceleration action with veh2.
Act 4: Is_acc_conflict_with('veh2')
Obs 4: Ego acceleration is safe with veh2. 
Thought 5: Now that we know acceleration is safe with veh2, we can
check the safety of the idle action.
Act 5: Is_idle_conflict_with('veh2')
Obs 5: Keep lane with current speed is safe with veh2.
Thought 6: We should choose the action that is consistent with the
previous decision, which was to accelerate. Therefore, we should
output the decision to accelerate.
Act 6: Finish.
Final Answer:
Decision: FASTER
Explanation: The acceleration action is safe with
veh2, and the IDLE action is also safe with veh2.
Since the previous decision was to accelerate, we
should continue to accelerate the vehicle.
lane_3
lane_2
lane_1
lane_0
lane_3
lane_2
lane_1
lane_0
veh2
ego
veh2
ego
Figure 5: The decision consistency during acceleration process
5

<!-- Page 6 -->
GPT-3.5 checks the safety of each available action. The perception tools show that acceleration may
cause a potential collision with the front car veh4, while maintaining speed is quite safe. When
checking the change lane to the left action, GPT-3.5 first determines which vehicle will be affected
by such action on lane_2, and then learns that changing lanes to the left is safe with veh1. At this
point, GPT-3.5 has examined each action and made a final decision to change to the left lane. It
provides a mature and reasonable explanation, stating that although the idle and change lane actions
are both safe, changing to lane_2 is a better move since it provides more flexibility for the ego car.
Considering that veh1 has a faster speed, this decision can lead to better performance.
Closed-loop driving in HighwayEnv not only requires LLMs to make safe decisions at each time step
but also demands consistency between decisions and avoiding behaviors such as frequent acceleration
and deceleration and meaningless lane changes. In our framework, the decision result and explanation
from the previous frame are included as part of the agent prompts and input into GPT-3.5. We use the
second example in Fig. 5 to demonstrate that GPT-3.5 has such decision-making consistency.
In this example, the green ego car is on the rightmost lane and is following veh2 while maintaining
a relatively long distance. In the previous decision, GPT-3.5 determined that the distance from the
leading car was too far, so it decided to speed up to keep up with veh2. At the beginning of the ReAct
process, GPT-3.5 still uses the Get_available_action tool to obtain all four available actions in
the current time step. It then finds out that veh2 is still driving in front of the ego car, and both the
idle and acceleration actions are safe with the leading vehicle. The final decision made by GPT-3.5 is
to keep accelerating, since it "chooses the action that is consistent with the previous decision," as
explained in its final answer. As a result, the ego car shortens the distance with the front vehicle,
which is more conducive to the overall traffic flow. Compared with the first example, due to the
reference to the previous decision result, the number of tools invoked by GPT-3.5 and the reasoning
cost are significantly reduced.
3
Reasoning ability with common sense
While both human drivers and previous optimization-based AD systems possess basic driving skills,
a fundamental difference between them is that humans have a common sense understanding of the
world. Common sense is sound and practical judgement of what is going on around us, accumulated
from daily lives [11]. The common sense that contributes to driving can be derived from all aspects
of everyday life. When presented with a new driving situation, a human driver can quickly assess
the scenario based on common sense and make a reasonable decision. In contrast, conventional AD
systems may have experience in the driving domain, but they lack common sense and thus unable to
tackle such situations.
LLMs like GPT-3.5, have been trained on vast amounts of natural language data and are knowl-
edgeable about common sense [2]. This marks a significant departure from traditional AD methods
and empowers LLMs to reason through complex driving scenarios using common sense, much like
human drivers. In this section, we evaluate two typical long-tail cases in autonomous driving systems,
which involves a pickup truck carrying traffic cones as described at the beginning of Section1.
As depicted in Fig.6, two similar yet distinct photographs are fed into the LLMs. The first photo
portrays a pickup truck carrying several traffic cones in its truck-bed en route to their destination.
The second one also depicts a pickup with cones in its truck bed, yet with additional cones scattered
on the ground in the surrounding area. As GPT-3.5 lacks the ability to process multimodal inputs
including images, we employ the LLaMA-Adapter v2 [15] as an image processing front-end. We
instruct LLaMA-Adapter to describe the photo as details as possible. This description is then utilized
as an observation, and we ask GPT-3.5 to assess whether the scenario is potentially hazardous and to
make a decision for the ego car, which is assumed to be following behind the truck.
In the first case depicted in Fig.6(a), LLaMA-Adapter identified that the pickup truck in the photograph
is carrying multiple traffic cones and inferred that it may be transporting them to their destination.
Based on these observations, GPT-3.5 successfully analyzed the driving scenario. Instead of being
misled by the presence of traffic cones, GPT-3.5 deemed this scenario to be non-hazardous, based on
the common sense that a truck transporting its cargoes to their destination is a common occurrence.
GPT-3.5 advised the driver of the ego car that there was no need to slow down and cautioned that
unnecessary slowdowns could potentially be dangerous for traffic flow.
6

<!-- Page 7 -->
Front-cam View
LLaMA-Adapter
Question: Describe the picture as details as
possible, assume all vehicles are moving.
Answer: The image shows a white truck driving
down a road with a trailer full of orange traffic
cones. The truck is carrying a significant amount
of traffic cones, which are stacked on the back of
the trailer. The cones are arranged in various
positions, covering a significant portion of the
trailer's length. The truck is the main focus of the
image, and it appears to be moving down the
road, transporting the traffic cones to their
destination.
GPT-3.5
Obeservation:
1. There's a moving truck in front of 'ego' car, maintaining proper
distance.
2. The truck is carrying a significant amount of traffic cones, which are
stacked on the back of the trailer.
3. Truck is moving down the road, transporting the traffic cones to their
destination. 
Task : Analyse current scenario and make decision for ego car.
Answer: The current scenario is not dangerous. The truck in front of the
'ego' car is maintaining a proper distance and is carrying traffic cones,
which is a common occurrence on roads. The fact that the truck is
transporting the cones to their destination, which is a normal driving
situation.
The driver on 'ego' should not decide to decelerate the car because of
the current situation. The truck in front is maintaining a proper distance
and is driving safely. Additionally, the fact that the truck is carrying
traffic cones indicates that it is likely transporting them to a
construction or maintenance site, which is a normal driving situation.
Decelerating the car unnecessarily could cause disruption to the flow of
traffic and could potentially be dangerous.
(a) Decision when the cones are loaded on the truck-bed.
Front-cam View
LLaMA-Adapter
Question: Describe the picture as details
as possible, assume all vehicles are
moving.
Answer: The scene features a large truck
driving down a street, with a trailer full of
orange traffic cones attached to its
back. The cones are scattered all around
the truck, covering the ground and
extending beyond the truck's length.
There are several cars parked on the
side of the street.
GPT-3.5
Obeservation:
1. There's a moving truck in front of 'ego' car, maintaining proper distance.
2. The truck has a trailer full of orange traffic cones attached to its back.
3. The cones are scattered all around the truck, covering the ground and
extending beyond the truck's length.
Task : Analyse current scenario and make decision for ego car.
Answer: Based on the available information, the current scenario can be
considered potentially dangerous. The presence of the truck with a trailer
full of traffic cones scattered on the road can pose a hazard to the 'ego'
car. Therefore, the driver needs to be cautious and maintain a safe
distance from the truck to avoid any collisions with the cones.
The driver on 'ego' should decide to decelerate the car because of the
cones. The scattered cones around the truck can be a potential hazard,
and it's better to be cautious and slow down to avoid any accidents.  It is
important to prioritize safety over efficiency while driving, and the driver
should make decisions based on the available information and their
experience on the road.
(b) Decision when the cones are scattered on the ground.
Figure 6: Two similar long-tail cases with a pickup truck carrying traffic cones.
For the second case, depicted in Fig.6(b), traffic cones are not only inside the truck bed, but also
scattered on the ground, which accurately represented by LLaMA-Adapter. Despite the minor
difference from the first case, GPT-3.5’s response is diametrically opposed. It considered this scenario
to be potentially dangerous due to the scattered cones around the truck and advised the driver of the
ego car to decelerate and maitain a distance to avoid any collisions with those cones.
The above examples demonstrate LLM’s powerful zero-shot understanding and reasoning abilities
in driving scenarioes. The utilization of common-sense knowledge not only allows LLMs to better
comprehend the semantic information within the scenario but also enables them to make more
rational decisions, which are more compatible with human driving behavior. Therefore, possessing
common-sense knowledge increases the upper limit of an autonomous driving system’s capabilities,
enabling it to handle unknown long-tail cases and truly approach the driving capabilities of human
drivers.
4
Performance enhancement through memorization ability
Continuous learning [28] is another key aspect for human to drive. Novice drivers typically drive
cautiously due to their limited experience when encountering complex traffic situations. Over time,
as they gain more experience behind the wheel, drivers encounter new traffic scenarios, develop new
driving skills, and consolidate their previous experience, eventually becoming experienced drivers.
The optimization-based approach aims to imitate the process of continuous learning by acquiring
more and more failed cases and using them to retrain the neural network. However, this approach is
not only tedious and expensive but also fundamentally incapable of achieving continuous learning.
The distribution difference between regular driving and long-tail corner cases poses a significant
challenge for balancing the two, eventually resulting in catastrophic forgetting. Therefore, a more
effective approach is needed to achieve true continuous learning in autonomous driving systems.
7

<!-- Page 8 -->
Scenario Undersatnding
Answer: The ego car is currently moving
towards the vehicle on the same lane.
The relation between the ego car and
the vehicle is that they are both on the
same lane, moving in opposite directions
towards each other. The ego car being
closer to the starting point of the lane
and the vehicle being closer to the end
point of the lane.
No-memory Decision
Answer: Based on the information provided, it would be safest for the 'ego' car to stop and wait for the
other vehicle to pass through.  As they are moving towards each other on the same lane, there is a risk
of collision if they get too close to each other.
Human Driver Decision:
Actually, the driver keeps moving without slow down and nudges slightly to the left. After a while, the car and
the vehicle passed through the lane in opposite directions, with no collision.
Self-reflection
Question: Why you made a wrong decision?
Answer: Based on the width of the ego car and the
alley, it is possible that the driver chose to drive
forward because there was enough space for the car
to pass through without colliding with the vehicle. The
driver may have also judged that slowing down or
stopping could have caused more danger or
disruption to the flow of traffic. Additionally, the driver
may have felt confident in their ability to maneuver the
car safely through the narrow space. 
Situation:Two vehicles on the
same lane moving towards each
other;
Proper decision:Keep moving
without slowing down and nudged
slightly to the left;
Wrong decision:Slows down and
potentially stop and wait;
Memories
Decision with memories
Answer: Based on the past experience you provided, it seems that the situation is similar to
the one where two vehicles were on the same lane moving towards each other.
Therefore, based on this past experience, it may be safe for the ego car to keep moving
without slowing down and nudging slightly to the left, while the other vehicle can keep
driving without slowing down and nudging slightly to the right.
Ego Car
Other
Vehicle
Modified to a
similar case
Figure 7: An example of the self-reflection and memorization ability of LLM
As depicted in Fig.1(b), our proposed LLM-based approach closely follows the human through the
use of a separate memory module. The memory module records only the decision scenarios that
"deviate from the experts." The experts can be either the developer’s evaluation of the LLM decision
or the ground truth of human driver’s decision in the real world. Once expert feedback is obtained,
the LLM undergoes a self-reflection process to determine why its decision deviates from the expert’s.
It then summarizes the traffic situation into a decision scenario and adds it to the memory pool as a
new memory entry, along with the proper decision. When the next time a similar case is encountered,
the LLM can quickly retrieve this memory entry for reference and make an informed decision.
Fig.7 gives an example of the memorization process. The scenario involves an encounter between a
blue ego car and a yellow car travelling in opposite directions in a narrow lane that is slightly wider
than twice the width of the car. After converting the scene into structured text for input into GPT-3.5,
we find that the model understood the scene well, including the states, orientation and destination
of the vehicles. However, when we asked it to make a decision about the scenario, GPT-3.5 gave a
safe but overly cautious advice that the ego car should stop and wait for the other vehicle to pass
first. To improve the LLM’s performance, the expert gives practical advice on how a human driver
would handle the situation, which involves keeping the car moving and nudging it slightly to the
left. The LLM then recognises that there is enough space for both vehicles to pass and that slowing
down could disrupt the flow of traffic. It summarizes the situation as "two vehicles in the same lane
moving towards each other" and records the memory along with the proper decision. Using these
memories, we input another scenario about two cars meeting in a narrow alleyway at different speeds
and positions, and asked the LLM to make a decision. The LLM successfully recognises that this is
just another variant of the "two cars in the same lane moving towards each other" decision scenario,
and advises that it is safe for the ego car to keep going instead of slowing down and waiting.
The memorization ability continuously collects driving cases to gain experience and assists decision-
making by retrieving existing memory, endowing LLM with the capability of continuous learning in
the field of autonomous driving. Furthermore, this significantly reduces the decision cost of LLM in
similar scenarios and improves its practical performance.
8

<!-- Page 9 -->
5
Related work
Self-driving Autonomy. Autonomous vehicles encompasses two main paradigms: modular [37, 12]
and end-to-end [5, 17, 33, 36]. The modular approach involves a stack of interconnected components
that handle various sub-tasks, such as perception [23, 24, 43], planning [21, 44], and control [30, 19].
This architecture offers enticing features like modularity and versatility. However, tuning the pipeline
and managing error propagation can pose challenges. In contrast, end-to-end autonomy directly maps
sensor input to planner or controller commands. These methods are typically easier to develop but
lack interpretability, making it difficult to diagnose errors, ensure safety, and incorporate traffic rules.
Nevertheless, recent advancements in end-to-end learnable pipeline autonomy have shown promising
outcomes by combining the strengths of both paradigms [17, 5]. Despite significant progress being
made in these two paradigms of self-driving, there are often observed that they become fragile when
handling long-tail data or out-of-distribution scenarios that occur in a real-world environment [22],
which poses challenges to safety-critical autonomous driving.
Advanced tasks with Large Language Models. The success of Large Language Models (LLM) is
undoubtedly exciting as it demonstrates the extent to which machines can learn human knowledge.
Recent efforts in LLM have shown impressive performance in zero-shot prompting and complex
reasoning [2, 25, 9, 27, 10], embodied agent research [39, 47, 38, 13, 42] and addressing key
transportation problems [45]. PaLM-E [13] employ fine-tuning techniques to adapt pre-trained LLM
for supporting multimodal prompts. Reflexion [34] incorporates self-reflection to further enhance the
agent’s reasoning abilities with the chain-of-thought prompting [27] to generate both reasoning traces
and task-specific actions using LLM. VOYAGER [39] presents lifelong learning with prompting
mechanisms, skill library, and self-verification, which are based on LLM. These three modules aim
to enhance the development of more complex behaviors of agents. Generative Agents [29] employ
LLM to store complete records of an agent’s experiences. Over time, these memories are synthesized
into higher-level reflections and dynamically retrieved to plan behavior. Instruct2Act [18] introduces
a framework that utilizes Large Language Models to map multi-modal instructions to sequential
actions for robotic manipulation tasks.
6
Conclusion
In this paper, we present our idea of building a system that can drive like a human. We reckon that
previous optimization-based autonomous driving systems have their limits when dealing with long-tail
corner cases due to the catastrophic forgetting of global optimization. Therefore, we summarize three
necessary abilities that an AD system should have to defeat imperfections including (1) Reasoning, (2)
Interpretation, and (3) Memorization. Then we design a new paradigm following these three creeds
that mimics the process of human learning to drive. Finally, with the hope of a primary artificial
general intelligence, we try to use GPT-3.5 as our LLM test-bed and show an impressive ability of
understanding traffic scenarios. As a preliminary work, we have only scratched the surface of LLMs’
potential in closed-loop driving to highlight the benefits and opportunities of adopting this technology,
rather than using the LLMs as a driving agent. Our aspiration is that this research will serve as a
catalyst for both academia and industry to innovate and construct an AGI-based autonomous driving
system that can drive like a human.
References
[1] Michael Ahn, Anthony Brohan, Noah Brown, Yevgen Chebotar, Omar Cortes, Byron David, Chelsea Finn,
Chuyuan Fu, Keerthana Gopalakrishnan, Karol Hausman, et al. Do as i can, not as i say: Grounding
language in robotic affordances. arXiv preprint arXiv:2204.01691, 2022.
[2] Ning Bian, Xianpei Han, Le Sun, Hongyu Lin, Yaojie Lu, and Ben He. Chatgpt is a knowledgeable but
inexperienced solver: An investigation of commonsense problem in large language models, 2023.
[3] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners.
Advances in neural information processing systems, 33:1877–1901, 2020.
[4] Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar,
Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence: Early
experiments with gpt-4. arXiv preprint arXiv:2303.12712, 2023.
9

<!-- Page 10 -->
[5] Sergio Casas, Abbas Sadat, and Raquel Urtasun. Mp3: A unified model to map, perceive, predict and
plan. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
14403–14412, 2021.
[6] Long Chen, Yuchen Li, Chao Huang, Bai Li, Yang Xing, Daxin Tian, Li Li, Zhongxu Hu, Xiaoxiang Na,
Zixuan Li, et al. Milestones in autonomous driving and intelligent vehicles: Survey of surveys. IEEE
Transactions on Intelligent Vehicles, 8(2):1046–1056, 2022.
[7] Long Chen, Yuchen Li, Chao Huang, Yang Xing, Daxin Tian, Li Li, Zhongxu Hu, Siyu Teng, Chen Lv,
Jinjun Wang, et al. Milestones in autonomous driving and intelligent vehicles—part 1: Control, computing
system design, communication, hd map, testing, and human behaviors. IEEE Transactions on Systems,
Man, and Cybernetics: Systems, 2023.
[8] Long Chen, Siyu Teng, Bai Li, Xiaoxiang Na, Yuchen Li, Zixuan Li, Jinjun Wang, Dongpu Cao, Nanning
Zheng, and Fei-Yue Wang. Milestones in autonomous driving and intelligent vehicles—part ii: Perception
and planning. IEEE Transactions on Systems, Man, and Cybernetics: Systems, 2023.
[9] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts,
Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm: Scaling language
modeling with pathways. arXiv preprint arXiv:2204.02311, 2022.
[10] Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi
Wang, Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned language models. arXiv
preprint arXiv:2210.11416, 2022.
[11] Common sense. Common sense — Wikipedia, the free encyclopedia, 2023. [Online; accessed 3-July-2023].
[12] Jonathan Daudelin, Gangyuan Jing, Tarik Tosun, Mark Yim, Hadas Kress-Gazit, and Mark Campbell. An
integrated system for perception-driven autonomy with modular robots. Science Robotics, 3(23):eaat4983,
2018.
[13] Danny Driess, Fei Xia, Mehdi SM Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan
Wahid, Jonathan Tompson, Quan Vuong, Tianhe Yu, et al. Palm-e: An embodied multimodal language
model. arXiv preprint arXiv:2303.03378, 2023.
[14] Jiafei Duan, Samson Yu, Hui Li Tan, Hongyuan Zhu, and Cheston Tan. A survey of embodied ai: From
simulators to research tasks. IEEE Transactions on Emerging Topics in Computational Intelligence,
6(2):230–244, 2022.
[15] Peng Gao, Jiaming Han, Renrui Zhang, Ziyi Lin, Shijie Geng, Aojun Zhou, Wei Zhang, Pan Lu, Conghui
He, Xiangyu Yue, Hongsheng Li, and Yu Qiao. Llama-adapter v2: Parameter-efficient visual instruction
model, 2023.
[16] Brett K Hayes, Evan Heit, and Haruka Swendsen. Inductive reasoning. Wiley interdisciplinary reviews:
Cognitive science, 1(2):278–292, 2010.
[17] Yihan Hu, Jiazhi Yang, Li Chen, Keyu Li, Chonghao Sima, Xizhou Zhu, Siqi Chai, Senyao Du, Tianwei
Lin, Wenhai Wang, et al. Planning-oriented autonomous driving. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pages 17853–17862, 2023.
[18] Siyuan Huang, Zhengkai Jiang, Hao Dong, Yu Qiao, Peng Gao, and Hongsheng Li. Instruct2act: Mapping
multi-modality instructions to robotic actions with large language model, 2023.
[19] Michael A Johnson and Mohammad H Moradi. PID control. Springer, 2005.
[20] Philip N Johnson-Laird. Deductive reasoning. Annual review of psychology, 50(1):109–135, 1999.
[21] Alonzo Kelly and Bryan Nagy. Reactive nonholonomic trajectory generation via parametric optimal
control. The International Journal of Robotics Research, 22(7-8):583–601, 2003.
[22] Lingdong Kong, Youquan Liu, Xin Li, Runnan Chen, Wenwei Zhang, Jiawei Ren, Liang Pan, Kai Chen,
and Ziwei Liu. Robo3d: Towards robust and reliable 3d perception against corruptions. arXiv preprint
arXiv:2303.17597, 2023.
[23] Xin Li, Tao Ma, Yuenan Hou, Botian Shi, Yuchen Yang, Youquan Liu, Xingjiao Wu, Qin Chen, Yikang
Li, Yu Qiao, et al. Logonet: Towards accurate 3d object detection with local-to-global cross-modal
fusion. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
17524–17534, 2023.
[24] Zhiqi Li, Wenhai Wang, Hongyang Li, Enze Xie, Chonghao Sima, Tong Lu, Yu Qiao, and Jifeng Dai.
Bevformer: Learning bird’s-eye-view representation from multi-camera images via spatiotemporal trans-
formers. In European conference on computer vision, pages 1–18. Springer, 2022.
[25] John J Nay. Law informs code: A legal informatics approach to aligning artificial intelligence with humans.
Nw. J. Tech. & Intell. Prop., 20:309, 2022.
[26] OpenAI. Introducing chatgpt. https://openai.com/blog/chatgpt/, 2023.
10

<!-- Page 11 -->
[27] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with
human feedback. Advances in Neural Information Processing Systems, 35:27730–27744, 2022.
[28] German I Parisi, Ronald Kemker, Jose L Part, Christopher Kanan, and Stefan Wermter. Continual lifelong
learning with neural networks: A review. Neural networks, 113:54–71, 2019.
[29] Joon Sung Park, Joseph C O’Brien, Carrie J Cai, Meredith Ringel Morris, Percy Liang, and Michael S
Bernstein. Generative agents: Interactive simulacra of human behavior. arXiv preprint arXiv:2304.03442,
2023.
[30] Xue Bin Peng, Marcin Andrychowicz, Wojciech Zaremba, and Pieter Abbeel. Sim-to-real transfer of
robotic control with dynamics randomization. In 2018 IEEE international conference on robotics and
automation (ICRA), pages 3803–3810. IEEE, 2018.
[31] Rolf Pfeifer and Fumiya Iida. Embodied artificial intelligence: Trends and challenges. In Embodied
Artificial Intelligence: International Seminar, Dagstuhl Castle, Germany, July 7-11, 2003. Revised Papers,
pages 1–26. Springer, 2004.
[32] Santhosh K Ramakrishnan, Dinesh Jayaraman, and Kristen Grauman. An exploration of embodied visual
exploration. International Journal of Computer Vision, 129:1616–1649, 2021.
[33] Abbas Sadat, Sergio Casas, Mengye Ren, Xinyu Wu, Pranaab Dhawan, and Raquel Urtasun. Perceive,
predict, and plan: Safe motion planning through interpretable semantic representations. In Computer
Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part
XXIII 16, pages 414–430. Springer, 2020.
[34] Noah Shinn, Beck Labash, and Ashwin Gopinath. Reflexion: an autonomous agent with dynamic memory
and self-reflection. arXiv preprint arXiv:2303.11366, 2023.
[35] Linda Smith and Michael Gasser. The development of embodied cognition: Six lessons from babies.
Artificial life, 11(1-2):13–29, 2005.
[36] Ardi Tampuu, Tambet Matiisen, Maksym Semikin, Dmytro Fishman, and Naveed Muhammad. A survey
of end-to-end driving: Architectures and training methods. IEEE Transactions on Neural Networks and
Learning Systems, 33(4):1364–1384, 2020.
[37] Sebastian Thrun, Mike Montemerlo, Hendrik Dahlkamp, David Stavens, Andrei Aron, James Diebel,
Philip Fong, John Gale, Morgan Halpenny, Gabriel Hoffmann, et al. Stanley: The robot that won the darpa
grand challenge. Journal of field Robotics, 23(9):661–692, 2006.
[38] Sai Vemprala, Rogerio Bonatti, Arthur Bucker, and Ashish Kapoor. Chatgpt for robotics: Design principles
and model abilities. Microsoft Auton. Syst. Robot. Res, 2:20, 2023.
[39] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima
Anandkumar. Voyager: An open-ended embodied agent with large language models. arXiv preprint
arXiv:2305.16291, 2023.
[40] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
Maarten Bosma, Denny Zhou, Donald Metzler, et al. Emergent abilities of large language models. arXiv
preprint arXiv:2206.07682, 2022.
[41] Lilian Weng. Llm-powered autonomous agents. lilianweng.github.io, Jun 2023.
[42] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React:
Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.03629, 2022.
[43] Tianwei Yin, Xingyi Zhou, and Philipp Krahenbuhl. Center-based 3d object detection and tracking. In
Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 11784–11793,
2021.
[44] Chris Zhang, Runsheng Guo, Wenyuan Zeng, Yuwen Xiong, Binbin Dai, Rui Hu, Mengye Ren, and Raquel
Urtasun. Rethinking closed-loop training for autonomous driving. In European Conference on Computer
Vision, pages 264–282. Springer, 2022.
[45] Ou Zheng, Mohamed Abdel-Aty, Dongdong Wang, Zijin Wang, and Shengxuan Ding. Chatgpt is on the
horizon: Could a large language model be all we need for intelligent transportation?, 2023.
[46] Hao Zhu, Raghav Kapoor, So Yeon Min, Winson Han, Jiatai Li, Kaiwen Geng, Graham Neubig, Yonatan
Bisk, Aniruddha Kembhavi, and Luca Weihs. Excalibur: Encouraging and evaluating embodied exploration.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14931–
14942, 2023.
[47] Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Weijie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei
Lu, Xiaogang Wang, et al. Ghost in the minecraft: Generally capable agents for open-world enviroments
via large language models with text-based knowledge and memory. arXiv preprint arXiv:2305.17144,
2023.
11