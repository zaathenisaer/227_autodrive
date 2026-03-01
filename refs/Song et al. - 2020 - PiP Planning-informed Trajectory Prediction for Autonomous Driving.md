# PiP: Planning-informed Trajectory Prediction for Autonomous Driving

**Authors:** Haoran Song, Wenchao Ding, Yuxuan Chen, Shaojie Shen, Michael Yu Wang, Qifeng Chen

**Date:** 2020


## Abstract

It is critical to predict the motion of surrounding vehicles for self-driving planning, especially in a socially compliant and flexible way. However, future prediction is challenging due to the interaction and uncertainty in driving behaviors. We propose planning-informed trajectory prediction (PiP) to tackle the prediction problem in the multi-agent setting. Our approach is differentiated from the traditional manner of prediction, which is only based on historical information and decoupled with planning. By informing the prediction process with the planning of ego vehicle, our method achieves the state-of-the-art performance of multi-agent forecasting on highway datasets. Moreover, our approach enables a novel pipeline which couples the prediction and planning, by conditioning PiP on multiple candidate trajectories of the ego vehicle, which is highly beneficial for autonomous driving in interactive scenarios.


---


## Full Text

<!-- Page 1 -->
PiP: Planning-informed Trajectory Prediction
for Autonomous Driving
Haoran Song1, Wenchao Ding1, Yuxuan Chen2, Shaojie Shen1,
Michael Yu Wang1, and Qifeng Chen1
1 The Hong Kong University of Science and Technology
2 University of Science and Technology of China
Abstract. It is critical to predict the motion of surrounding vehicles for
self-driving planning, especially in a socially compliant and ﬂexible way.
However, future prediction is challenging due to the interaction and un-
certainty in driving behaviors. We propose planning-informed trajectory
prediction (PiP) to tackle the prediction problem in the multi-agent set-
ting. Our approach is diﬀerentiated from the traditional manner of pre-
diction, which is only based on historical information and decoupled with
planning. By informing the prediction process with the planning of ego
vehicle, our method achieves the state-of-the-art performance of multi-
agent forecasting on highway datasets. Moreover, our approach enables
a novel pipeline which couples the prediction and planning, by condi-
tioning PiP on multiple candidate trajectories of the ego vehicle, which
is highly beneﬁcial for autonomous driving in interactive scenarios.
Keywords: Trajectory prediction · Autonomous driving
1
Introduction
Anticipating future trajectories of traﬃc participants is an essential capability of
autonomous vehicles. Since traﬃc participants (agents) will aﬀect the behavior
of each other, especially in highly interactive driving scenarios, the prediction
model is required to anticipate the social interaction among agents in the scene
to achieve socially compliant and accurate prediction.
Despite the fact that the interaction among traﬃc agents is being investi-
gated, far less attention is paid to how the uncontrollable (surrounding) agents
interact with the controlled (ego) agent. Diﬀerent future plans of the ego agent
will largely aﬀect the future behaviors of all surrounding agents, which leads to
a signiﬁcant diﬀerence in future predictions. Human drivers are accustomed to
imagining what the situation will be if they are going to act in diﬀerent ways.
For example, they speculate whether the other vehicles will leave space if they
insert aggressively or mildly, respectively. By considering the diﬀerent future sit-
uations from multiple “what-ifs”, human drivers are adept at negotiating with
other traﬃc participants while ﬂexibly adapting their own driving behaviors.
The key is that human drivers condition the prediction of surrounding vehicles
arXiv:2003.11476v2  [cs.CV]  18 Jan 2021

<!-- Page 2 -->
2
H. Song et al.
Traditional Pipeline 
Tracking
Prediction
Planning
Trajectory Generator
Cost func
Evaluator
Best 
Trajectory
PiP
Prediction
Tracking
Trajectory Generator
Planning
Cost func
Evaluator
Best 
Trajectory
Fig. 1. Comparison between the traditional prediction approach (left) and PiP (right)
under a lane merging scenario. Assume the ego vehicle (red) intends to merge to the
left lane. It is required to predict the trajectories of surrounding vehicles (blue). To
alleviate the uncertainty led by future interaction, PiP incorporates the future plans
(dotted red curve) of ego vehicle in addition to the history tracks (grey curve). While
the traditional prediction result is produced independently with the ego’s future, PiP
produces predictions one-to-one corresponding to the candidate future trajectories by
enabling the novel planning-prediction-coupled pipeline. Therefore, PiP evaluates the
planning safety more precisely and achieves more ﬂexible driving behavior (solid red
curve) compared with the traditional pipeline.
on their own future intention. In this paper, we want to inform the interaction-
aware prediction using the candidate plans of the controlled vehicle to mimic
this thinking process.
To this end, we propose a novel planning-informed prediction framework
(PiP). Note that PiP does not require the exact future trajectory, which is actu-
ally undetermined during prediction. PiP only conditions the prediction process
on the candidate future trajectories proposed by the trajectory generator, like
“insert aggressively” and “insert mildly” these kinds of “what-ifs”. Accordingly,
the best trajectory could be picked out after evaluating all the candidate plans
by their corresponding predictions in the planning module.
There are two signiﬁcant beneﬁts of PiP. First, by incorporating the addi-
tional planning information, the interaction among agents can be better cap-
tured, which leads to a considerable improvement in predictive accuracy. Sec-
ond, the planning-informed prediction will provide a highly valuable interface
for the planning module during system integration. Explicitly, instead of evalu-
ating multiple future plans under a ﬁxed prediction result as most autonomous
driving systems do, PiP conditions the prediction process on the ego vehicle’s
future plans, which uncovers how the other vehicles will interact with ego vehicle
if the ego vehicle executes any speciﬁc planning trajectory. The PiP pipeline is
especially suitable for planning in dense and highly interactive traﬃc (such as

<!-- Page 3 -->
PiP: Planning-informed Trajectory Prediction
3
merging into a congested lane), which is hard to be handled using traditional
decoupled prediction and planning pipeline. The comparison between the tradi-
tional pipeline for autonomous driving and PiP is illustrated in Fig. 1.
To eﬀectively achieve planning-informed prediction, we propose two mod-
ules, namely, planning-coupled module and target fusion module. The planning-
coupled module extracts the interaction features with a special channel for in-
jecting the future planning, while the target fusion module encodes and decodes
the tightly coupled future interaction among agents. PiP is end-to-end trainable.
The main contributions are listed as follows:
• Planning-coupled module is proposed to model the multi-agent interaction
from both the history time domain (history tracking of surrounding agents)
and future time domain (future planning of controlled agent). By introducing
the planning information into social context encoding, the uncertainty from
the multi-modality of driving behavior is alleviated and thus leads to an
improvement in predictive accuracy.
• Target fusion module is presented to capture the interdependency between
target agents further. Since all the future states of targets are linked up
together with the planning of the controlled agent, we apply a fully con-
volutional structure to model their future dependency at diﬀerent spatial
resolutions. The introduction of the target fusion module leads to further
improvement for multi-agent forecasting.
• Our model outperforms state-of-the-art methods for multi-agent forecast-
ing from tracking data. Moreover, the proposed planning-prediction-coupled
pipeline extends the operational domain of planning by the integration with
prediction, and some qualitative results are demonstrated.
2
Related Work
To accurately forecast the future trajectory of a speciﬁc vehicle, we need to
discover the clues from its past observation and corresponding traﬃc conﬁgura-
tion. In this paper, we focus on the data-driven trajectory prediction methods,
which essentially learn the relationship between future trajectory and past mo-
tion states. Since vehicle behaviors are often inter-related, especially in dense
traﬃc, it is crucial to consider interaction-aware trajectory prediction for au-
tonomous driving, namely, in a multi-agent setting. In this section, we provide
an overview of interaction-aware trajectory prediction methods and the common
practice of integrating prediction with planning, which motivates our planning-
informed prediction.
Interaction-aware trajectory prediction: Multi-agent learning and fore-
casting [9,16,18,28,30] is a challenging problem and Social LSTM [1] is one sem-
inal work. In [1], the spatial interaction among pedestrians is learned using the
proposed social pooling structure based on the hidden states generated by long
short-term memory (LSTM) network, and [5] improves the social pooling strat-
egy by applying convolutional layers. To better capture the multi-modal nature
of future behaviors, some non-deterministic generative models are adopted based

<!-- Page 4 -->
4
H. Song et al.
on generative adversarial network (GAN) [10,11,25], and variational autoencoder
(VAE) [14,17]. Besides learning the interaction among agents, the agent-scene
interaction is also modeled in [2,26,31]. The interaction-aware network structures
are further extended to heterogeneous traﬃc [3,20] and applied to autonomous
driving scenarios such as [5,6,17].
Trajectory prediction for control and planning: Targeting on the real-
time driving, the popularly used vehicle motion planners [8,21,22,27,29] follow
the workﬂow: ﬁrst roll out multiple candidate ego trajectories; then score them
using user-deﬁned functions, in which the future trajectories of other vehicles
predicted based on history tracks are considered; ﬁnally, pick out the best tra-
jectory to execute. Note that the prediction result of other vehicles is ﬁxed for
diﬀerent candidates from the trajectory generator of the ego vehicle. Namely,
the traditional pipeline does not make “what-ifs”, and think the reactions of
other vehicles will be the same even given diﬀerent ego actions. However, be-
cause the future planning of the ego vehicle in turn aﬀects the behaviors of
surrounding agents, the “predict-and-plan” workﬂow may be inadequate, espe-
cially in tightly coupled driving scenarios such as merging [13]. Diﬀerentiated
from the traditional decoupled pipeline, PiP can be incorporated into a novel
planning-prediction-coupled pipeline, which extends ﬂexibility in dense traﬃc.
Planning-informed trajectory prediction: Rhinehart [23] proposed con-
ditioning the prediction process on the goal of the ego vehicle, which is likely to
be the ﬁrst attempt to incorporating planning information into prediction. How-
ever, only the goal position information is utilized, which may pose restrictions.
For example, considering the scenario of controlling the ego vehicle to insert
into congested traﬃc, even given the same goal of the ego vehicle, the future
reaction of surrounding vehicles varies signiﬁcantly depending on the speciﬁc
time proﬁle of how the ego vehicle reaches the goal. This motivates us to inform
the prediction process with varying completeness of planning information (i.e.,
from several rough waypoints to a complete planned trajectory). In general, our
proposed method is capable of providing accurate interaction-aware trajectory
prediction for a large batch of diﬀerent candidate planned trajectories eﬃciently,
which facilitates planning in highly interactive environments [4,7].
3
Method
In PiP, the motion of each target vehicle is predicted by considering not only
its own state and the other agents’ states in the history time domain, but also
the ego vehicle’s planned trajectory. In this section, we ﬁrst formulate the prob-
lem in Sec. 3.1, and describe the details of PiP in the following structure: the
planning-coupled module which incorporates the ego vehicle’s planned trajec-
tory in the social tensors of neighboring vehicles’ past motions (Sec. 3.2), the
method of agent-centric target fusion (Sec. 3.3) and the maneuver-based de-
coding method for generating the probabilistic distribution of the location dis-
placement between future frames (Sec. 3.4). Some implementation details are
provided in Sec. 3.5.

<!-- Page 5 -->
PiP: Planning-informed Trajectory Prediction
5
3.1
Problem Formulation
Consider the driving scenario for an autonomous vehicle. The ego vehicle is
commanded by the planning module, and the perception module senses the
neighboring vehicles within a certain range. We formulate the trajectory pre-
diction problem in the multi-agent setting as estimating the future states of a
set of target vehicles around the ego vehicle vego conditioning on the tracking
history of all surrounding vehicles and the planned future of the controllable
ego vehicle. The objective is to learn the posterior distribution P(Y|X, I) of
multiple targets’ future trajectories Y = {Yi|vi ∈Vtar}, where Vtar is the set
of predicted targets selected within an ego-vehicle-centric area Atar. The con-
ditional items contain the future planning of ego vehicle I and the past tra-
jectories X = {Xi|vi ∈V }, where V denotes the set of all vehicles involved
around the ego vehicle, and (vego ∪Vtar) ⊆V as the ego vehicle is not re-
quired to be predicted. At any time t, the history trajectory and future tra-
jectory of an agent i are denoted as Xi =
n
xt−Tobs+1
i
, xt−Tobs+2
i
..., xt
i
o
and
Yi =
n
yt+1
i
, yt+2
i
..., yt+Tpred
i
o
, where the elements of xi, yi ∈R2 represent way-
point coordinates in the past and future, respectively, while Tobs and Tpred refer
to the number of frames for observation and prediction. Note that the planned
trajectory I = Yego =
n
yt+1
ego , yt+2
ego ..., yt+Tpred
ego
o
is also used as a conditional item,
since it’s generated from ego vehicle’s trajectory planner and thus can be acces-
sible during prediction. Moreover, the introduction of I enables the planning-
prediction-coupled pipeline as shown in Fig. 1.
3.2
Planning Coupled Module
In the planning coupled module, each predicted agent is processed in its own
centric area Anbr, in which the ego vehicle vego, the target vehicle vcent ∈Vtar
and the other neighboring vehicles Vnbrs ⊆V located within Anbr are included.
There involve three encoding streams: the dynamic property of the target itself,
the social interaction with the target’s neighboring vehicles, and the spatial de-
pendency with ego vehicle’s future planning. Consequently, a target encoding T
is generated by embedding these encodings together. In practice, we use relative
trajectories in an agent-centric manner for capturing interdependencies between
the centric agent and surrounding agents.
Trajectory Encoding: All trajectories contained in the planning coupled
module could be classiﬁed into two types: observable and controllable. The his-
tory trajectories of traﬃc participants could be observed, and the planned trajec-
tory to command the ego vehicle could be controlled. Before extracting the spa-
tially interactive relationship between traﬃc agents, all trajectories are encoded
independently to learn the temporal properties in their sequential locations. To
better accomplish this work, each trajectory is preprocessed by converting its
locations into relative coordinates with respect to the target vehicle and then fed
into a temporal convolutional layer to obtain a motion embedding. After that,
the Long Short-Term Memory (LSTM) networks are employed to encode the

<!-- Page 6 -->
6
H. Song et al.
Conv-1
MaxPool-1 Conv-2 MaxPool-2
Dynamics
Encoding
PlanningTraj Encoding
LSTM
1D
Conv
Skip Connections
Target 
Tensor
Fused Target 
Tensor
History Traj Encoding
1D
Conv
+
Social
Context 
Planning 
Tensor 
Observation 
Tensor 
Target Fusion Module
Planning Coupled Module
Ego Vehicle
Target Vehicle
Other Neighbor Vehicles
LSTM
Maneuver 
Based 
Decoder
SoftMax
(Lateral)
+
+
SoftMax
(Longitudinal)
Fully Connected
LSTM Decoder
Multi-Modal
Predictions
Maneuver
Probability
Fig. 2. The overview of PiP architecture: PiP consists of three key modules, including
planning coupled module, target fusion module, and maneuver-based decoding module.
Each predicted target is ﬁrstly encoded in the planning coupled module by aggregat-
ing all information within the target-centric area (blue square). A target tensor is then
set up within the ego-vehicle-centric area (red square) by placing the target encodings
into the spatial gird based on their locations. Afterward, the target tensors are passed
through the following target fusion module to learn the interdependency between tar-
gets, and eventually, a fused target tensor is generated. Finally, the prediction of each
target is decoded from the corresponding fused target encoding in the maneuver-based
decoding module. The target vehicle marked with an ellipse is exempliﬁed for planning
coupled encoding and multi-modal trajectories decoding.
motion property for trajectories, and the hidden state h(·) therein is regarded
as the motion encoding for the corresponding trajectory. Here, the LSTMs with
diﬀerent parameters are adopted for planned trajectory Yego and history tra-
jectories including Xego, Xcent and Xnbr, as they belong to the diﬀerent time
domains.
Planning and Observation Fusion: The use of LSTM encoder captures
the temporal structure from the trajectory sequence, while it fails to handle the
spatial interaction relationship with other agents in a scene. The social pooling
strategy, proposed in [1], addresses this issue by pooling LSTM states of spa-
tially proximal sequences in a target-centric grid named as “social tensor”. The
“convolutional social pooling” in [5] improves the strategy further by applying
convolutional and max-pooling layers over the social tensor. Both of the meth-
ods are proposed for learning the spatial relationship among trajectories that
takes place in the history period. In our proposed framework, we adopt the con-
volutional social pooling structure for modeling spatial interaction. In addition
to interdependencies between target and neighbors in the past time, the spatial
information of ego vehicle’s planning in the future time is counted in the plan-
ning coupled module as an improvement. Accordingly, three encoding branches
stemming from LSTM hidden states of all trajectories are included, as illustrated

<!-- Page 7 -->
PiP: Planning-informed Trajectory Prediction
7
in Fig. 2. The lower branch encodes the dynamics property of the target vehicle
by feeding its motion encoding h(Xcent) to a fully connected layer. The spatial
relationship between the target and its surrounding agents is captured in the
upper branches by building a grid centered at the location of the target vehicle.
Since the planned future trajectory and observed history trajectory belong to
diﬀerent time domain, the history information of h(Xnbr) and h(Xego) are placed
into a target-centric spatial grid termed as observation tensor with respect to
the corresponding locations at current time t, while the motion encoding of the
planned trajectory h(Yego) is placed similarly in another spatial grid to form the
planning tensor. It should be noted that the planning sequence is encoded in a
reversed order because the planning of the near future is more reliable, and thus
it should weight more in the encoding.
After that, both of the observation and planning tensors pass through con-
volutional layers and pooling layers in parallel and then are concatenated to-
gether before fed to the last max-pooling layer. Merging the information from
the planning of ego vehicle and observation of surrounding vehicles, the resulting
encoding S covers the social context for both the past and future time domain.
Finally, the merged social encoding S concatenates with the target’s dynamics
encoding D to form a target encoding T that aggregates all the information
accessible within the target-centric grid.
3.3
Target Fusion Module
In [1,5], the future states of each target is directly decoded from the agent-
centric encoding result that aggregates history information. In this way, each
trajectory is generated independently from the corresponding target encoding.
However, the future states of targets are highly correlated, which indicates that
the decoding process for a certain target also depends on the encoding of other
targets. Therefore, we further fuse the encoding among diﬀerent targets in the
scene and decode the ﬁnal trajectory from the fused encoding, which better
captures the dependencies of future states of diﬀerent targets in the same scene.
For jointly predicting the vehicles within the target area centered on the ego
vehicle’s location, each target vehicle vi ∈Vtar represented by its encoding Ti
is placed into an ego-vehicle-centric grid {Ti|vi ∈Vtar} based on their locations
at the last time step of history trajectories. Inspired by some popular CNN
architectures for segmentation [19,24] that produce correspondingly-sized output
with hierarchical inference, we adopt the fully convolutional network (FCN) to
learn the context of target tensor. The target tensor is fed into a symmetric
FCN structure for capturing the spatial dependencies between target agents
at diﬀerent grid resolutions, where the skip-connected layers are combined by
element-wise sum. The fused target tensor produced by this module retains its
spatial structure the same as before fusion, from which the fused target encoding
T +
i
of each target could be sliced out according to its grid location.

<!-- Page 8 -->
8
H. Song et al.
3.4
Maneuver Based Decoding
To address the inherent multi-modality nature of the driving behaviors, the ma-
neuver based decoder built upon [5] is applied to predict the future trajectory for
predeﬁned maneuver classes M = {mk|k = 1, 2, ..., 6} together with the proba-
bility of each maneuver P(mk). The maneuvers are classiﬁed by lateral behaviors
(including lane-keeping, left and right lane changes) and longitudinal behaviors
(including normal driving and braking). Thereupon, the fused target encoding
T +
i
of target vehicle vi ∈Vtar is ﬁrst fed into a pair of fully connected layers that
followed by soft-max layers to get the lateral and longitudinal behavior probabil-
ity respectively, and thus their multiplication produces the probability for each
maneuver P(mk|I, X). The trajectory under each maneuver class is generated
by concatenating the fused target encoding with one-hot vectors of lateral behav-
ior and longitudinal behavior together, followed by passing the resulted feature
vector through an LSTM decoder. Instead of directly generating absolute future
locations, our LSTM decoder operates in a residual learning manner that out-
puts displacement between predicted locations. The output vector contains the
displacement δyt+T
i
∈R2 between neighboring predicted locations, the standard
deviation vector σt+T
i
∈R2 and correlation coeﬃcient ρt+T
i
∈R of predicted lo-
cation ˆyt+T
i
at the future time step T ∈{1, 2, ..., Tpred}. The predicted location
could be accordingly represented by a bivariate Gaussian distribution
ˆyt+T
i
∼N(µt+T
i
, σt+T
i
, ρt+T
i
),
(1)
where the mean vector is given by summing up all displacements along the future
time steps T with the location at the last time step t of history trajectory
µt+T
i
= xt
i +
T
X
τ=1
δyt+τ
i
.
(2)
For brevity, the Gaussian parameters for all future time steps of target vi is
written as Θi. Finally, the posterior probability of all target vehicles’ future
trajectories could be estimated from
P(Y|X, I) =
Y
vi∈Vtar
|M|
X
k=1
PΘi(Yi|mk, X, I)P(mk|X, I).
(3)
3.5
Implementation Details
Our model is trained by minimizing the negative log likelihood of future trajec-
tories under the true maneuver class mtrue of all the target vehicles
−
X
vi∈Vtar
log (PΘi(Yi|mtrue, X, I)P(mtrue|X, I)) .
(4)
Each data instance contains a vehicle speciﬁed as the ego. The predicted
targets are the vehicles located within the ego-vehicle-centric area Atar with the

<!-- Page 9 -->
PiP: Planning-informed Trajectory Prediction
9
size of 60.96×10.67 meters (200×35 feet), discretized as 25×5 spatial grid. The
target-centric area Anbr of each predicted vehicle is deﬁned the same as Atar.
For the planning input I of the ego vehicle, its actual trajectory within the
prediction horizon is directly used in training. While in evaluation and testing, I
is ﬁtted from its downsampled actual trajectory. It is handled in this way because
we intend to restrict the prediction from accessing the complete information
of planning trajectory, instead only a limited number of waypoints could be
accessed. Furthermore, the ground-truth trajectories result from many planning
cycles, while in practice, prediction can only be based on the current planning
cycle. So the planning input is represented by a ﬁtted quintic spline, which
is a typically used representation for vehicle trajectory. This feature makes our
planning-informed method easy to deploy in a real autonomous system. Although
the ﬁtted planning input cannot perfectly ﬁt the actual future trajectory, it could
be examined if our method can generalize well in practical use.
4
Experiments
In this section, we evaluate our method on two publicly available vehicle trajec-
tory datasets, NGSIM [12] and HighD [15]. Firstly, we compare the performance
of our method against the existing state-of-the-art works quantitatively using
the metrics of root mean squared error (RMSE) and negative log-likelihood
(NLL). Next, as our method could anticipate diﬀerent future conﬁgurations by
performing diﬀerent plans under the same historical situation, we evaluate PiP
from more simulated future situations. Regarding the rationality and variety in
generating feasible vehicle trajectories, we employ a model-based vehicle plan-
ner MPDM [4] to generate diverse vehicle trajectories with diﬀerent lateral and
longitudinal behaviors. In Sec. 4.4, a user study is conducted by comparing our
generated results with the real situations to verify the rationalization of predicted
outcomes, and more results are provided in Sec. 4.5 for qualitative analysis.
4.1
Datasets
We split all the trajectories contained in NGSIM and HighD separately, in which
70% are used for training with 20% and 10% for testing and evaluation. Each
vehicle’s trajectory is split into 8s segments composed of 3s of past and 5s of
future positions at 5Hz. The 5s future of ego vehicle used as planning input is
further downsampled to 1Hz in testing and evaluation. The objective is to predict
all surrounding target vehicles’ future trajectories over 5s prediction horizon.
NGSIM: NGSIM [12] is a real-world highway dataset which is commonly
used in the trajectory prediction task. All vehicle trajectories over a 45-minute
time span are captured at 10Hz, with each 15-minute segment under mild, mod-
erate, and congested traﬃc conditions, respectively.
HighD: HighD [15] is a vehicle trajectories dataset released in 2018. The
data is recorded from six diﬀerent locations on Germany highways from the
aerial perspective using a drone. It is composed of 60 recordings over areas of
400 ∼420 meters span, with more than 110, 000 vehicles are contained.

<!-- Page 10 -->
10
H. Song et al.
4.2
Baseline Methods
We compare PiP with the following listed deterministic models and stochastic
models, and also ablate the planning coupled module and target fusion mod-
ule in PiP-noPlan and PiP-noFusion respectively, to study their eﬀectiveness in
improving predictive accuracy.
S-LSTM: Social LSTM [1] uses a fully connected layer for social pooling
and produces a uni-modal distribution of future locations.
CS-LSTM: Convolutional Social LSTM [5] uses convolutional layers with
social pooling and outputs a maneuver-based multi-modal prediction.
S-GAN: Social GAN [11] trains GAN based framework using the adversarial
loss to generate diverse trajectories for multi-agent in a spatial-centric manner.
MATF: MATF-GAN [31] models spatial interaction of agents and scene
context by convolutional fusion and uses GAN to produce stochastic predictions.
4.3
Quantitative Evaluation
Among all the above methods, S-GAN and MATF are stochastic models.3 We
report their RMSE by the best result among 3 samples (i.e., minRMSE). The
others are all deterministic models that generate Gaussian distributions for all
predicted locations along the trajectory, in which the means of Gaussian parame-
ters are used as the predicted locations when calculating the RMSE for each time
step t within the 5s prediction horizon: RMSE(t) =
q
1
|Vtar|
P
vi∈Vtar ∥yi −ˆyi∥2.
For multi-modal distribution output by CS-LSTM, PiP and its variants, RMSE
is evaluated using the predicted trajectory with the maximal maneuver proba-
bility P(mk). While RMSE is a concrete metric to measure prediction accuracy,
it is limited to some extent since it tends to average all the prediction results
and may fail to reﬂect the accuracy for distinct maneuvers. To overcome its
limitation in evaluating multi-modal prediction, we adopt the same way from
prior work [5] that additionally reports the negative log-likelihood (NLL) of the
true trajectories under the predictive results represented by either uni-modal or
multi-modal distributions.
The results of quantitative results are reported in Table 1. Our method signif-
icantly outperforms the deterministic models (S-LSTM and CS-LSTM) in both
RMSE and NLL metrics on both datasets. Although sampling more trajectories
and choosing the minimal error among all samples would undoubtedly lead to a
lower RMSE for stochastic models (S-GAN and MATF), our deterministic model
still achieves lower RMSE than stochastic models for sampling three times. The
reason for not setting a larger sampling number for the stochastic models is that
sampling too many times for prediction may not work well with planning and
decision making since the probability of each sample is actually unknown.
The consistent improvements on NLL and RMSE metrics conﬁrm that, by
introducing the planning of ego vehicle into the prediction model and captur-
ing the correlations between predictive targets, PiP gets better performance in
3 No NLL results of S-GAN and MATF, as they sample trajectories without generating
probability. No RMSE result of MATF on HighD dataset is reported in [31].

<!-- Page 11 -->
PiP: Planning-informed Trajectory Prediction
11
Table 1. Quantitative results on NGSIM and HighD datasets are reported by RMSE
and NLL metrics over 5s prediction horizon. The best results are marked by bold
numbers. Note that for the stochastic methods (S-GAN and MATF), the minimal
error from sampling three times reports their RMSE
Metric Dataset Time S-LSTM[1] CS-LSTM[5] S-GAN[11] MATF[31] PiP-noPlan PiP-noFusion PiP
RMSE (m)
NGSIM
1s
0.60
0.58
0.57
0.66
0.55
0.55
0.55
2s
1.28
1.26
1.32
1.34
1.20
1.19
1.18
3s
2.09
2.07
2.22
2.08
2.00
1.95
1.94
4s
3.10
3.09
3.26
2.97
3.01
2.90
2.88
5s
4.37
4.37
4.40
4.13
4.27
4.07
4.04
HighD
1s
0.19
0.19
0.30
-
0.18
0.17
0.17
2s
0.57
0.57
0.78
-
0.53
0.53
0.52
3s
1.18
1.16
1.46
-
1.09
1.05
1.05
4s
2.00
1.96
2.34
-
1.86
1.76
1.76
5s
3.02
2.96
3.41
-
2.81
2.63
2.63
Metric Dataset Time
S-LSTM
CS-LSTM
S-GAN
MATF
PiP-noPlan PiP-noFusion PiP
NLL (nats)
NGSIM
1s
2.38
1.91
-
-
1.68
1.71
1.72
2s
3.86
3.44
-
-
3.29
3.29
3.30
3s
4.69
4.31
-
-
4.20
4.17
4.17
4s
5.33
4.94
-
-
4.87
4.81
4.80
5s
5.89
5.48
-
-
5.42
5.33
5.32
HighD
1s
0.42
0.37
-
-
0.20
0.20
0.14
2s
2.58
2.43
-
-
2.28
2.28
2.24
3s
3.93
3.65
-
-
3.53
3.53
3.48
4s
4.87
4.51
-
-
4.39
4.37
4.33
5s
5.57
5.17
-
-
5.05
5.01
4.99
predictive accuracy. Additionally, the result of ablation studies shows that PiP-
noPlan performs worse than PiP-noFusion in most of the cases, which indicates
that the inclusion of the planning trajectory is more eﬀective in improving the
accuracy of multi-agent forecasting.
4.4
User Study
To investigate if our prediction model generalizes to various future plans (diﬀer-
ent maneuver classes and aggressiveness) under diﬀerent traﬃc conﬁgurations,
we have also simulated diverse future scenarios by performing diﬀerent planned
trajectories for the ego vehicle. Accordingly, we conduct the user study that com-
pares real and simulated traﬃc situations, as shown in the upper part of Fig. 3.
Each pair of videos are derived from a segment of 8s traﬃc sequence recorded
in the datasets. One video displays the complete recording of the real tracking
data, while the other video shares the same 3s history sequence, and contains a
diﬀerent sequence in the last 5s which is composed by the predicted trajectories
of targets (blue) under a diﬀerent plan performed by ego vehicle (red). The other
agents (no color) outside the predictive range are hidden in the last 5s. Note that
the same coloring scheme is used in the following experiments.
We display 20 pairs of videos with randomized order and ask participants to
select the one in which the target vesicles’ behavior looks unreasonable or against

<!-- Page 12 -->
12
H. Song et al.
50 m
100 m
150 m
50 m
100 m
150 m
10 m
20 m
10 m
20 m
CS-LSTM
PiP
CS-LSTM
PiP
50 m
100 m
150 m
200 m
50 m
100 m
150 m
200 m
10 m
20 m
0
1
2
3
4
5 (s)
Real 
Situation
Simulated
Situation
Fig. 3.
Upper: user study example of comparing the real and simulated situations.
Each comparison is visualized as video pair for users to choose the situation that vio-
lates their intuition. Lower: two example cases predicted by CS-LSTM and PiP. The
ground truth (blue), planning (red) and predicted trajectories (green) are visualized by
sets of locations with 0.2s time step. As both methods output maneuver-based multi-
modal distributions, only those trajectories with maneuver probability larger than 10%
are shown for each target. The green circle denotes the mean value of distribution on
each time step, and its radius is proportional to the maneuver probability of the corre-
sponding trajectory. The green shadow area represents the variance of the distribution.
common sense. Totally 25 people participated in the user study, and our simu-
lated results were selected as the unreasonable one with a rate of 52.2%(261/500),
a bit higher than 50%. One reason is that the ego vehicle’s planned trajectory
in the simulated results is generated oﬄine, but its real trajectory recorded in
the datasets is resulted from replanning adaptively from time to time. Then it
could be a clue for users to select the actual situation as the better one.
Nevertheless, our model still achieves a 47.8% rate of being selected as rea-
sonable. It could also be noted in the upper part of Fig. 3, we generate an agile
lane merging trajectory for the ego car, and the predicted outcome shows that
the following vehicle reacts with deceleration while the leading vehicles maintain
speed. Both of the forecastings make sense in real traﬃc, which indicates that
our proposed method could be generalized to diﬀerent plans.
4.5
Qualitative Analysis
In the following, we further investigate how the prediction is improved as well
as explore how PiP enables the planning-prediction-coupled pipeline.
Baseline Comparison: Since our method employs the same maneuver-
based decoding as in CS-LSTM [5], the predictive distribution under the same
traﬃc scenes is compared in the lower part of Fig. 3. In the left example, we

<!-- Page 13 -->
PiP: Planning-informed Trajectory Prediction
13
50 m
100 m
150 m
(a)
(b)
0
1
2
3
4
5 (s)
collision point
*
(c)
20 m
10 m
20 m
10 m
20 m
10 m
Fig. 4. Prediction results of performing diverse planned trajectories by ego vehicle: the
history trajectories (grey) are from a traﬃc scene in NGSIM, and the future trajectories
are visualized by gradient color varying over time. The target vehicle that collides with
ego vehicle is marked with a star symbol, and the collision point is annotated by a
cross symbol.
notice that CS-LSTM outputs similar maneuver probability of keeping the lane
and turning right for the left-rear target. At the same time, our method is more
conﬁdent to target’s actual maneuver of turning right. It is because that ego
vehicle is planned to go straight under certain velocity, thereby leaving enough
space for the target to merge to its right lane. By the same token, our method
precisely predicts the right-rear target will keep lane but not turn left in the right
example. At that moment, the ego vehicle intends to merge to the right lane
gradually in a moderate manner, which blocks the way for the right-rear target
to turn left in the near future. Both examples demonstrate that the planning-
informed approach leads the prediction to be more accurate.
Active Planning: With PiP, it is feasible to explore how to plan in dif-
ferent traﬃc situations actively. In the following, we illustrate some challenging
scenarios with history states acquired from datasets, and PiP produces diverse
future states under diﬀerent plans generated by the ego vehicle.
Fig. 4 (a,b) shows prediction results when performing a moderate and ag-
gressive lane changing in dense traﬃc. It could be noticed that the aggressive
behavior in Fig. 4 (b) is risky as it is very close to the preceding vehicle after
merging. Notably, when it merges aggressively a bit faster, as shown in Fig. 4
(c), a collision is forecasted between the controlled vehicle and the target with a
star mark. The ability of forecasting collision further veriﬁes the generalization
of our network as no collision occurred in the traﬃc recordings where the PiP
model is trained.

<!-- Page 14 -->
14
H. Song et al.
Fig. 5. Prediction results of performing diverse planned trajectories by ego vehicle:
the history trajectories are from a highway scene in HighD. All the annotations are
same with Fig. 4. The predicted future is shown with a collision in (a, b) and safe lane
changing in (c,d).
Fig. 5 shows another example from HighD dataset in which the vehicles go
much faster than that in NGSIM dataset. In this case, turning right is chal-
lenging. In Fig. 5 (a) the ego vehicle is planned to turn right and follow the
right-front target. A prompt deceleration may cause the rear vehicle to fail to
respond and results in a rear-end collision. PiP also anticipates in Fig. 5 (b)
that a collision will occur if the ego vehicle plans to turn right and overtakes the
right-font target. Nevertheless, it is still possible to ﬁnd a proper way of merging
to the right lane, as shown in Fig. 5 (c). Additionally, we also show a result of
changing to the left lane in Fig. 5 (d), which is relatively easier as there exists
larger space on the left for lane changing.
5
Conclusion
In this work, we present PiP for predicting future trajectories in a planning-
informed approach. Leveraging on the fact that all traﬃc agents are tightly cou-
pled throughout the time domain, the future prediction on surrounding agents is
informed by incorporating history tracks with future planning of the controllable
agent. PiP outperforms the state-of-the-art works for multi-agent forecasting on
highway datasets. Furthermore, PiP enables a novel planning-prediction-coupled
pipeline that produces future predictions one-to-one corresponding to candidate
trajectories, and we demonstrate that it could act as a highly usable interface
for planning in dense or fast-moving traﬃc. In the future, we plan to extend our
approach to work under imperfect tracking or detection information, which is
common in the perception module. Further, the future prediction and trajectory
generation could be integrated into a motion planner that learns to generate
optimal planning under interactive scenarios.

<!-- Page 15 -->
PiP: Planning-informed Trajectory Prediction
15
References
1. Alahi, A., Goel, K., Ramanathan, V., Robicquet, A., Fei-Fei, L., Savarese, S.: Social
lstm: Human trajectory prediction in crowded spaces. In: Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition (CVPR). pp. 961–971
(2016)
2. Bartoli, F., Lisanti, G., Ballan, L., Del Bimbo, A.: Context-aware trajectory pre-
diction. In: 2018 24th International Conference on Pattern Recognition (ICPR).
pp. 1941–1946. IEEE (2018)
3. Chandra, R., Bhattacharya, U., Bera, A., Manocha, D.: Traphic: Trajectory predic-
tion in dense and heterogeneous traﬃc using weighted interactions. In: Proceedings
of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR).
pp. 8483–8492 (2019)
4. Cunningham, A.G., Galceran, E., Eustice, R.M., Olson, E.: Mpdm: Multipolicy
decision-making in dynamic, uncertain environments for autonomous driving. In:
Proc. IEEE Int.Conference on Robotics and Automation. pp. 1670–1677. IEEE
(2015)
5. Deo, N., Trivedi, M.M.: Convolutional social pooling for vehicle trajectory predic-
tion. In: Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition Workshops (CVPR). pp. 1468–1476 (2018)
6. Ding, W., Chen, J., Shen, S.: Predicting vehicle behaviors over an extended horizon
using behavior interaction network. In: Proc. IEEE Int.Conference on Robotics and
Automation. pp. 8634–8640. IEEE (2019)
7. Ding, W., Zhang, L., Chen, J., Shen, S.: Safe trajectory generation for complex
urban environments using spatio-temporal semantic corridor. IEEE Robotics and
Automation Letters (2019)
8. Fan, H., Zhu, F., Liu, C., Zhang, L., Zhuang, L., Li, D., Zhu, W., Hu, J., Li,
H., Kong, Q.: Baidu apollo em motion planner. arXiv preprint arXiv:1807.08048
(2018)
9. Felsen, P., Lucey, P., Ganguly, S.: Where will they go? predicting ﬁne-grained ad-
versarial multi-agent motion using conditional variational autoencoders. In: Pro-
ceedings of the European Conference on Computer Vision (ECCV). pp. 732–747
(2018)
10. Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair,
S., Courville, A., Bengio, Y.: Generative adversarial nets. In: Advances in neural
information processing systems. pp. 2672–2680 (2014)
11. Gupta, A., Johnson, J., Fei-Fei, L., Savarese, S., Alahi, A.: Social gan: Socially
acceptable trajectories with generative adversarial networks. In: Proceedings of
the IEEE Conference on Computer Vision and Pattern Recognition (CVPR). pp.
2255–2264 (2018)
12. Halkias, J., Colyar, J.: Next generation simulation fact sheet. Tech. rep., Federal
Highway Administration (FHWA) (2006), fHWA-HRT-06-135
13. Hubmann, C., Schulz, J., Xu, G., Althoﬀ, D., Stiller, C.: A belief state planner
for interactive merge maneuvers in congested traﬃc. In: 2018 21st International
Conference on Intelligent Transportation Systems (ITSC). pp. 1617–1624. IEEE
(2018)
14. Kingma, D.P., Welling, M.: Auto-encoding variational bayes. arXiv preprint
arXiv:1312.6114 (2013)
15. Krajewski, R., Bock, J., Kloeker, L., Eckstein, L.: The highd dataset: A drone
dataset of naturalistic vehicle trajectories on german highways for validation of

<!-- Page 16 -->
16
H. Song et al.
highly automated driving systems. In: 2018 21st International Conference on In-
telligent Transportation Systems (ITSC). pp. 2118–2125. IEEE (2018)
16. Le, H.M., Yue, Y., Carr, P., Lucey, P.: Coordinated multi-agent imitation learning.
In: Proceedings of the 34th International Conference on Machine Learning-Volume
70. pp. 1995–2003. JMLR. org (2017)
17. Lee, N., Choi, W., Vernaza, P., Choy, C.B., Torr, P.H., Chandraker, M.: Desire: Dis-
tant future prediction in dynamic scenes with interacting agents. In: Proceedings
of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR).
pp. 336–345 (2017)
18. Lee, N., Kitani, K.M.: Predicting wide receiver trajectories in american football.
In: 2016 IEEE Winter Conference on Applications of Computer Vision (WACV).
pp. 1–9. IEEE (2016)
19. Long, J., Shelhamer, E., Darrell, T.: Fully convolutional networks for semantic
segmentation. In: Proceedings of the IEEE Conference on Computer Vision and
Pattern Recognition (CVPR). pp. 3431–3440 (2015)
20. Ma, Y., Zhu, X., Zhang, S., Yang, R., Wang, W., Manocha, D.: Traﬃcpredict:
Trajectory prediction for heterogeneous traﬃc-agents. In: Proceedings of the AAAI
Conference on Artiﬁcial Intelligence. vol. 33, pp. 6120–6127 (2019)
21. McNaughton, M., Urmson, C., Dolan, J.M., Lee, J.W.: Motion planning for
autonomous driving with a conformal spatiotemporal lattice. In: Proc. IEEE
Int.Conference on Robotics and Automation. pp. 4889–4895. IEEE (2011)
22. Pivtoraiko, M., Knepper, R.A., Kelly, A.: Diﬀerentially constrained mobile robot
motion planning in state lattices. Journal of Field Robotics 26(3), 308–333 (2009)
23. Rhinehart, N., McAllister, R., Kitani, K., Levine, S.: Precog: Prediction condi-
tioned on goals in visual multi-agent settings. In: Proceedings of the IEEE Inter-
national Conference on Computer Vision (ICCV). pp. 2821–2830 (2019)
24. Ronneberger, O., Fischer, P., Brox, T.: U-net: Convolutional networks for biomedi-
cal image segmentation. In: International Conference on Medical image computing
and computer-assisted intervention. pp. 234–241. Springer (2015)
25. Sadeghian, A., Kosaraju, V., Sadeghian, A., Hirose, N., Rezatoﬁghi, H., Savarese,
S.: Sophie: An attentive gan for predicting paths compliant to social and physi-
cal constraints. In: Proceedings of the IEEE Conference on Computer Vision and
Pattern Recognition (CVPR). pp. 1349–1358 (2019)
26. Sadeghian, A., Legros, F., Voisin, M., Vesel, R., Alahi, A., Savarese, S.: Car-net:
Clairvoyant attentive recurrent network. In: Proceedings of the European Confer-
ence on Computer Vision (ECCV). pp. 151–167 (2018)
27. Schwarting, W., Alonso-Mora, J., Rus, D.: Planning and decision-making for au-
tonomous vehicles. Annual Review of Control, Robotics, and Autonomous Systems
(2018)
28. Sun, C., Karlsson, P., Wu, J., Tenenbaum, J.B., Murphy, K.: Stochastic pre-
diction of multi-agent interactions from partial observations. arXiv preprint
arXiv:1902.09641 (2019)
29. Werling, M., Ziegler, J., Kammel, S., Thrun, S.: Optimal trajectory generation
for dynamic street scenarios in a frenet frame. In: Proc. IEEE Int.Conference on
Robotics and Automation. pp. 987–993. IEEE (2010)
30. Zhan, E., Zheng, S., Yue, Y., Sha, L., Lucey, P.: Generative multi-agent behavioral
cloning. arXiv (2018)
31. Zhao, T., Xu, Y., Monfort, M., Choi, W., Baker, C., Zhao, Y., Wang, Y., Wu, Y.N.:
Multi-agent tensor fusion for contextual trajectory prediction. In: Proceedings of
the IEEE Conference on Computer Vision and Pattern Recognition (CVPR). pp.
12126–12134 (2019)