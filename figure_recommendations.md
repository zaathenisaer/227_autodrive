# 综述图表建议报告

**文档说明：** 本报告针对综述 `revised.tex`（《Multi-Agent Autonomous Driving: A Structured Survey of Learning, Interaction, and Cognitive Paradigms》）提出 12 幅 AI 生成图表的具体建议，包括每幅图的**插入位置**（附 LaTeX 代码片段）、**图表设计说明**，以及可直接用于 DALL·E 3、Midjourney、Stable Diffusion 或 Adobe Firefly 等工具的**详细生成 Prompt**。

---

## 图表总览

| 编号 | 图表名称 | 插入章节 | 类型 |
|------|----------|----------|------|
| Fig. 1 | 三范式演进时间线 | § 1 Introduction | 时间线 / 信息图 |
| Fig. 2 | 综述三层分类体系全图 | § 1.1 Scope and Contributions | 层次结构图 |
| Fig. 3 | POMDP 与 POSG 架构对比 | § 2 Background | 双栏架构图 |
| Fig. 4 | DAVE-2 端到端 CNN 架构 | § 3.1 DAVE-2 | 神经网络结构图 |
| Fig. 5 | ChauffeurNet 扰动训练管道 | § 3.2 ChauffeurNet | 流程图 |
| Fig. 6 | Social LSTM 社会池化机制 | § 4.1.1 Social LSTM | 网格示意图 |
| Fig. 7 | VectorNet 两级 GNN 架构 | § 4.1.2 VectorNet | 图神经网络结构图 |
| Fig. 8 | PiP 预测–规划双向反馈环 | § 4.1.3 PiP | 双向流程图 |
| Fig. 9 | MADDPG 集中训练分散执行 | § 4.2.2 MADDPG | 多智能体架构图 |
| Fig. 10 | V2VNet V2X 特征融合 | § 4.3 V2VNet | 车联网通信图 |
| Fig. 11 | LLM 认知驾驶智能体对比 | § 5 LLM-Based Cognitive Agents | 四象限对比图 |
| Fig. 12 | LanguageMPC 双层次控制架构 | § 5.4 LanguageMPC | 层次架构图 |

---

## Fig. 1：三范式演进时间线

### 插入位置

在 `\section{Introduction}` 内、第三个段落（Paradigm 3 的结束处）之后、`\subsection{Scope and Contributions}` 之前，约第 145 行后插入：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/fig1_paradigm_timeline.pdf}
  \caption{自动驾驶研究的三大范式演进时间线。从 2016 年基于行为克隆的端到端学习，到 2017--2021 年以多智能体交互与协作为核心的第二范式，再到 2023 年至今以大语言模型为驱动的认知智能体第三范式，每一次跃迁均由前一范式的核心局限所驱动。}
  \label{fig:paradigm_timeline}
\end{figure}
```

同时，在 Introduction 段落文本中，将 `\paragraph{Paradigm 3 -- LLM-Based Cognitive Agents.}` 结尾添加引用：`（见图~\ref{fig:paradigm_timeline}）`。

### 图表设计说明

- **形式**：横向时间线，左端为 2016 年，右端为 2025 年。
- **分层**：时间线分三条泳道（Paradigm 1 / 2 / 3），每条泳道用不同颜色（蓝/绿/橙）标识。
- **节点**：每篇关键论文对应一个带图标的节点（如神经网络图标代表 DAVE-2，多辆汽车代表 MADDPG，大脑图标代表 LLM 方法）。
- **箭头**：范式之间用弯曲虚线箭头标注"局限 → 动机"关系（如 covariate shift → ChauffeurNet）。
- **配色**：蓝色系（单智能体），绿色系（多智能体），橙/金色系（LLM 认知）。
- **风格**：学术信息图，白底，无渐变阴影，矢量级清晰度，适合学术论文印刷。

### AI 生成 Prompt

**（适用于 DALL·E 3 / GPT-4o Image Generation）**

```
Create a clean, academic-style horizontal timeline infographic for an autonomous driving survey paper. The timeline spans from 2016 to 2025 and is divided into three horizontal swim lanes:

Lane 1 (blue, bottom): "Paradigm 1: Single-Agent Imitation Learning" — contains nodes for DAVE-2 (2016, neural network icon) and ChauffeurNet (2018, car with perturbation arrows).

Lane 2 (green, middle): "Paradigm 2: Multi-Agent Interaction & Coordination" — contains nodes for Social LSTM (2016, pedestrian grid), VectorNet (2020, graph nodes), MADDPG (2017, multiple agents), V2VNet (2020, two communicating cars), SMARTS (2020, training environment icon), and NuPlan (2021, benchmark icon).

Lane 3 (orange, top): "Paradigm 3: LLM-Based Cognitive Agents" — contains nodes for Drive Like a Human (2023, brain+car), DiLu (2023, memory bank icon), GPT-Driver (2023, text tokens), LanguageMPC (2025, hierarchical layers).

Between lanes, draw curved dashed arrows labeled with the core limitation that motivated the transition: "Covariate Shift" (between lanes 1 and 2), "Long-Tail Failure" (between lanes 2 and 3).

Style: white background, flat design, vector-art quality, academic journal ready, no gradients, crisp borders, small icons for each paper node, legend at bottom. Font: sans-serif. Color palette: cool blue (#2E6DB4), green (#2E8B57), amber (#E07B39).
```

**（适用于 Midjourney / Stable Diffusion，需配合 ControlNet 或结构化描述）**

```
/imagine prompt: academic timeline infographic, horizontal layout, three color-coded swim lanes (blue, green, orange), paper nodes with small technical icons, curved arrows between lanes showing causal transitions, white background, clean vector style, sans-serif labels, 2016 to 2025 time axis, autonomous driving research paradigms --ar 3:1 --style raw --v 6
```

---

## Fig. 2：综述三层分类体系全图

### 插入位置

在 `\subsection{Scope and Contributions}` 与 `\subsection{Paper Organization}` 之间（约第 157 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/fig2_taxonomy.pdf}
  \caption{本综述三层分类体系总览。第一层为单智能体学习基础（行为克隆与策略优化），第二层为多智能体交互与协调（表示学习、策略训练与协作感知），第三层为基于 LLM 的认知智能体（链式推理、记忆增强与神经符号控制）。}
  \label{fig:taxonomy}
\end{figure}
```

### 图表设计说明

- **形式**：自顶向下的三层树形结构（树状图 / 思维导图风格）。
- **根节点**：中央大圆形，标注"Multi-Agent Autonomous Driving"。
- **第一层**：三个主分支，分别对应论文的三大章节，用颜色区分（蓝/绿/橙）。
- **第二层**：每个主分支下展开子节点，对应各方法（如 DAVE-2、VectorNet、DiLu 等），节点内标注论文作者年份。
- **图标**：每个叶节点旁配一个微型技术图标（CNN 示意、图网络、LLM 对话气泡等）。
- **连线**：实线表示"包含"关系，虚线表示"方法演进"关系。

### AI 生成 Prompt

```
Create a hierarchical taxonomy diagram for an academic survey paper on multi-agent autonomous driving. 

Root node (center, dark navy circle): "Multi-Agent Autonomous Driving (MAAD)"

Three main branches:
1. [Blue branch, left] "Layer 1: Single-Agent Foundations"
   - DAVE-2 (Bojarski 2016): CNN icon, "End-to-End BC"
   - ChauffeurNet (Bansal 2018): augmentation arrows icon, "Synthesized Perturbation"
   - PPO (Schulman 2017): policy gradient icon, "Clipped Surrogate Objective"

2. [Green branch, center-right] "Layer 2: Multi-Agent Interaction & Coordination"
   - Social LSTM (Alahi 2016): occupancy grid, "Social Pooling"
   - VectorNet (Gao 2020): graph nodes, "Vectorized GNN"
   - PiP (Song 2020): bidirectional arrow, "Prediction-Planning Loop"
   - MADDPG (Lowe 2017): centralized/decentralized icon, "CTDE"
   - Safety RL (Shalev 2016): shield icon, "RSS Hierarchical"
   - MACAD-Gym (Palanisamy 2020): simulator icon
   - SMARTS (Zhou 2020): diverse agents icon
   - V2VNet (Wang 2020): V2X communication icon

3. [Orange branch, right] "Layer 3: LLM-Based Cognitive Agents"
   - Drive Like a Human (Fu 2023): chain-of-thought icon
   - DiLu (Wen 2023): memory bank icon
   - GPT-Driver (Mao 2023): text tokens icon
   - LanguageMPC (Sha 2025): two-level hierarchy icon

Style: white background, clean academic infographic, flat design with subtle drop shadows, rounded rectangles for leaf nodes, colored connecting lines matching branch color, small gray monochrome icons on each leaf node, sans-serif font. Suitable for printing in a journal paper.
```

---

## Fig. 3：POMDP 与 POSG 架构对比

### 插入位置

在 `\subsection{Multi-Agent Extension: POSG}` 结尾、`\subsection{Architectural Dichotomy}` 之前（约第 228 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/fig3_pomdp_vs_posg.pdf}
  \caption{POMDP（单智能体，左）与 POSG（多智能体，右）决策框架对比。POSG 在 POMDP 基础上引入多个具有独立动作空间 $\mathcal{A}^i$、观察空间 $\mathcal{O}^i$ 和奖励函数 $R^i$ 的智能体，联合转移函数 $T$ 依赖所有智能体的联合动作，导致非平稳性挑战。}
  \label{fig:pomdp_posg}
\end{figure}
```

### 图表设计说明

- **左侧（POMDP）**：单个 Agent 节点 → 动作 $a_t$ → 环境 → 状态 $s_{t+1}$ → 观察 $o_t$ → 奖励 $r_t$，循环箭头。
- **右侧（POSG）**：$N$ 个 Agent 节点（Agent 1, Agent 2, …, Agent N）各自发出动作 $a^i_t$，汇入共享环境方块；环境返回各自的 $o^i_t$ 和 $r^i_t$；Agent 间有虚线"交互感知"箭头。
- **中间分隔**：一条灰色竖线，标注"Non-stationarity emerges"。
- **颜色**：POMDP 侧蓝色调，POSG 侧绿色调。

### AI 生成 Prompt

```
Create a two-panel academic comparison diagram for a research paper.

LEFT PANEL — "Single-Agent: POMDP":
- One circular agent node labeled "Agent" in the center
- Arrow from Agent to a rectangle labeled "Environment (T, R, Ω)"
- Arrow labeled "action aₜ" from Agent to Environment
- Arrow labeled "observation oₜ" and "reward rₜ" from Environment back to Agent
- A self-loop labeled "maximize E[Σγᵗ R(sₜ,aₜ)]"
- Blue color scheme

RIGHT PANEL — "Multi-Agent: POSG":
- Three circular agent nodes labeled "Agent 1", "Agent 2", "Agent N" (with ellipsis)
- All three agents send arrows labeled "a¹ₜ, a²ₜ, ..., aᴺₜ" to a central rectangle "Shared Environment"
- Environment sends back individual arrows "o¹ₜ, r¹ₜ" to Agent 1, "o²ₜ, r²ₜ" to Agent 2, etc.
- Dashed bidirectional arrows between the agents labeled "policy interaction"
- A warning label: "Non-stationarity: T depends on all agents' actions"
- Green color scheme

Dividing the two panels: a vertical gray dashed line labeled "Multi-agent extension →"

Style: clean, academic, flat design, white background, sans-serif font, box arrows with clear labels, suitable for a journal paper figure.
```

---

## Fig. 4：DAVE-2 端到端 CNN 架构

### 插入位置

在 `\subsection{End-to-End Behavior Cloning: DAVE-2}` 内、`\paragraph{Technical Significance.}` 之前（约第 282 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.85\linewidth]{figures/fig4_dave2_architecture.pdf}
  \caption{DAVE-2 端到端 CNN 架构示意。三路前向摄像头图像经归一化后输入九层卷积网络（约 2700 万参数），网络自动学习车道线、道路边界等特征，最终输出连续转向角命令。合成视角扰动（Synthetic Viewpoint Perturbation）在训练阶段生成侧向偏移的恢复行为数据，以缓解协变量偏移。}
  \label{fig:dave2}
\end{figure}
```

### 图表设计说明

- **输入**：左侧三个小矩形代表"Left Camera"、"Center Camera"、"Right Camera"，箭头汇聚后输入网络。
- **网络层**：从左到右依次画出 5 个卷积层（逐渐缩小的矩形体，注明核大小 5×5, 5×5, 5×5, 3×3, 3×3）和 3 个全连接层（竖向方块）。
- **输出**：最右侧一个单一节点标注"Steering Angle"，旁有小方向盘图标。
- **扰动标注**：在输入图像旁画一个小插图，显示车辆偏移 + 修正箭头，标注"Synthetic Perturbation"。
- **风格**：深蓝/灰色渐变的网络层，白色文字标注，背景浅灰。

### AI 生成 Prompt

```
Create a clean neural network architecture diagram for an academic paper, showing the NVIDIA DAVE-2 end-to-end autonomous driving CNN.

Layout (left to right):
1. INPUT: Three stacked small rectangles labeled "Left Cam", "Center Cam", "Right Cam" — arrow merges into "3×66×200 normalized input"
2. CONVOLUTIONAL LAYERS: Five 3D rectangular blocks with decreasing spatial size, labeled:
   - Conv1: 24 filters, 5×5, stride 2
   - Conv2: 36 filters, 5×5, stride 2
   - Conv3: 48 filters, 5×5, stride 2
   - Conv4: 64 filters, 3×3
   - Conv5: 64 filters, 3×3
3. FLATTEN: A thin rectangle labeled "Flatten → 1164"
4. FULLY CONNECTED LAYERS: Three vertical blocks labeled FC1(100), FC2(50), FC3(10)
5. OUTPUT: A single circle labeled "Steering Angle θ" with a small steering wheel icon

Add a callout box near the input labeled "Synthetic Viewpoint Perturbation: lateral offset ±2m → corrective steering target" with a small diagram showing a car drifting left and an arrow pointing back to center lane.

Style: dark blue gradient blocks for conv layers, lighter gray for FC layers, white text labels, clean academic diagram, white background, no photorealistic elements, suitable for journal publication.
```

---

## Fig. 5：ChauffeurNet 扰动训练管道

### 插入位置

在 `\subsection{Overcoming Covariate Shift: ChauffeurNet}` 内、聚合损失公式（编号为第 2 个方程式）之后、`\paragraph{Residual Limitation.}` 之前（约第 324 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/fig5_chauffeurnet_pipeline.pdf}
  \caption{ChauffeurNet 训练管道示意。系统以渲染的中层场景表示（路网、边界框、交通灯）为输入，通过几何扰动（轨迹偏移）和环境 dropout（随机遮蔽物体）合成对抗场景，并以碰撞惩罚与偏路惩罚辅助损失联合训练，使智能体能够学习从分布外状态恢复的策略。}
  \label{fig:chauffeurnet}
\end{figure}
```

### 图表设计说明

- **三大模块**：左侧"Real Expert Demos"（正常驾驶日志）→ 中间"Perturbation Engine"（扰动引擎，内部分三个子操作）→ 右侧"ChauffeurNet Policy Network"（RNN 策略网络）。
- **扰动引擎内部**：展示三种操作的图标：①轨迹弯曲箭头（Geometric Perturbation），②方块被删除（Environment Dropout），③碰撞感叹号（Collision / Off-road Loss）。
- **损失函数标注**：在策略网络右侧展示汇总损失 $\mathcal{L} = \mathcal{L}_{\text{imitation}} + \lambda_c \mathcal{L}_{\text{collision}} + \lambda_r \mathcal{L}_{\text{road}} + \lambda_g \mathcal{L}_{\text{geometry}}$（可手写或文字块展示）。
- **中层表示**：在输入侧配一个鸟瞰视角小图，标注"Bird's-Eye Rendered Scene"（彩色道路 + 边界框）。

### AI 生成 Prompt

```
Create a flowchart diagram for an academic paper illustrating the ChauffeurNet training pipeline for autonomous driving.

Left section — "Real Expert Demonstrations":
- A small bird's-eye view diagram of a road with colored bounding boxes (pink for vehicles, blue for road boundaries, green for traffic light status)
- Label: "Mid-level scene representation (30M clips)"

Center section — "Perturbation Engine" (orange background rectangle):
Three rows inside:
1. "Geometric Perturbation": diagram of a trajectory being warped/bent with a curved arrow
2. "Environment Dropout": road scene with some bounding boxes crossed out / hidden
3. "Loss on Events": red collision icon + orange off-road warning icon → "auxiliary loss signals"

Right section — "ChauffeurNet Policy Network":
- A recurrent neural network block (RNN/LSTM symbol) labeled "ChauffeurNet (RNN)"
- Input: bird's-eye view frame sequence
- Output: "Future Trajectory Waypoints"

Below the network: a small loss equation box showing:
L = L_imitation + λ_c·L_collision + λ_r·L_road + λ_g·L_geometry

Arrows: left → center → right, with a feedback arrow from Loss box back to the perturbation engine labeled "trains agent to recover"

Style: clean flowchart, academic, white background, sans-serif font, flat design with colored region backgrounds (light blue for input, light orange for perturbation, light green for network), journal-quality.
```

---

## Fig. 6：Social LSTM 社会池化机制

### 插入位置

在 `\subsubsection{Social LSTM: Spatiotemporal Social Pooling}` 内、社会池化公式之后、`\paragraph{Significance and Limitations.}` 之前（约第 396 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.82\linewidth]{figures/fig6_social_lstm.pdf}
  \caption{Social LSTM 社会池化机制示意。每个行人由独立 LSTM 追踪，社会池化层将邻居隐状态 $h_{j,t-1}$ 投影至以当前智能体为中心的占用网格（$m \times n$ 格），通过按元素最大操作聚合后拼接至本智能体的 LSTM 输入，实现隐式社会规范的学习。}
  \label{fig:social_lstm}
\end{figure}
```

### 图表设计说明

- **布局**：中央为一个 $8 \times 8$ 的浅灰格子（占用网格），中心格标"Agent $i$"（绿色）；周围几个格子中标有"Agent $j_1$"、"Agent $j_2$"（蓝色）。
- **LSTM 模块**：每个 Agent 旁配一个小 LSTM 方块（标注 $h_{j,t-1}$），用箭头指向网格对应格子。
- **Pool 操作**：从网格发出箭头，经过"max-pooling"符号，汇成"$H_i^{\text{pool}}$"向量。
- **LSTM 更新**：$H_i^{\text{pool}}$ 拼接个人嵌入后输入中心 Agent 的 LSTM，输出预测轨迹。
- **限制标注**：网格边缘用红色虚线框高亮，标注"Fixed Grid Resolution"和"Scalability Bottleneck"。

### AI 生成 Prompt

```
Create a clean technical diagram illustrating the Social LSTM pedestrian trajectory prediction mechanism for an academic paper.

Center: An 8×8 grid representing the social occupancy map centered on "Agent i" (highlighted center cell in green). Several cells contain small blue circles labeled "Agent j₁", "Agent j₂", "Agent j₃" representing neighboring pedestrians within spatial threshold.

For each agent (i and each j):
- Draw a small LSTM block to the right/left labeled "LSTM" with hidden state hⱼ,t₋₁ shown as a vector
- Draw an arrow from each neighbor's LSTM block to its corresponding grid cell

Below the grid:
- Arrow down labeled "Element-wise max pooling" → "H_i^pool (pooled hidden state tensor)"

To the right:
- H_i^pool concatenated with individual embedding eᵢ → fed into "LSTM Agent i" → outputs "Predicted Trajectory"

Add a red dashed border around the grid with a callout: "Limitation: Fixed grid resolution — cannot scale to dense intersections"

Style: academic diagram, white background, flat design, occupancy grid with light gray cells, green center cell, blue agent cells, clean arrows, sans-serif labels. Suitable for journal publication figure.
```

---

## Fig. 7：VectorNet 两级 GNN 架构

### 插入位置

在 `\subsubsection{VectorNet: Vectorized Scene Representation with GNNs}` 内、两级 GNN 描述列表（enumerate）之后、`\paragraph{Relevance to Multi-Agent Settings.}` 之前（约第 434 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/fig7_vectornet.pdf}
  \caption{VectorNet 两级层次图神经网络架构。底层子图网络对每条折线（车道线、Agent 历史轨迹）内的向量关系进行局部编码，生成折线级节点特征 $p_i$；顶层全局交互图通过多头注意力（式~\ref{eq:vn_attn}）对所有折线节点建模全局依赖，最终输出用于轨迹预测的上下文特征。}
  \label{fig:vectornet}
\end{figure}
```

### 图表设计说明

- **底部（子图层）**：三列独立的小图，每列代表一条折线（Lane 1、Agent Trajectory、Lane 2），每条折线中有 3-4 个向量节点（小圆）用局部边连接，输出一个聚合节点 $p_i$。
- **顶部（全局图层）**：将所有 $p_i$ 节点（来自不同折线）连成一个全连接图，边上标注多头自注意力（MultiHead Attention）。
- **向量表示**：在一条折线展示中，标注向量起点、终点坐标和语义属性（type: lane, speed limit: 50）。
- **输出**：全局图右侧输出"Context Features $p_i'$"→ 轨迹预测头。

### AI 生成 Prompt

```
Create a two-level hierarchical graph neural network architecture diagram for VectorNet in an academic paper.

BOTTOM LEVEL — "Subgraph Network (Local GNNs)":
- Show three separate small graph clusters side by side:
  1. "Lane Segment 1": 4 nodes connected in sequence (representing vectors on a lane centerline), each node labeled with small attributes (start point, end point, type: lane)
  2. "Agent Trajectory": 4 nodes connected in sequence (historical waypoints), labeled "vehicle past trajectory"
  3. "Lane Segment 2": similar to Lane Segment 1
- Below each cluster, draw an aggregation arrow → producing one output node labeled p₁, p₂, p₃ (polyline-level features)

TOP LEVEL — "Global Interaction Graph":
- The three output nodes p₁, p₂, p₃ are connected in a fully-connected graph
- Each edge is labeled "Multi-Head Self-Attention"
- Output of each node: p₁', p₂', p₃' (updated global context features)

Right side output:
- Arrow from the global graph to a box labeled "Trajectory Prediction Head → future waypoints"

A small inset legend shows: "vector vᵢ = [start_point, end_point, semantic_attrs]"

Style: clean technical diagram, white background, blue nodes for lane vectors, orange nodes for agent trajectory, gray edges, green output nodes, sans-serif labels. Academic journal quality.
```

---

## Fig. 8：PiP 预测–规划双向反馈环

### 插入位置

在 `\subsubsection{PiP: Closing the Prediction--Planning Loop}` 内、PiP 公式之后（约第 463 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.9\linewidth]{figures/fig8_pip_loop.pdf}
  \caption{PiP 预测–规划双向耦合机制。规划模块生成 $K$ 条候选自车轨迹 $\{\tau^k_{\text{ego}}\}$，预测模块以此为条件输出周围智能体的反应预测 $\hat{Y}_i$；规划模块依据全局最优预测选定最终轨迹，实现博弈论意义上的双向交互建模，解决"冻结机器人"问题。}
  \label{fig:pip}
\end{figure}
```

### 图表设计说明

- **左侧（规划模块）**：一个方块"Planning Module"，发出 $K=3$ 条不同颜色的候选轨迹（三条曲线，颜色不同）。
- **中央（场景）**：俯视角道路示意，ego 车（绿色）在下，前方有一辆目标车（蓝色），左侧一辆背景车（灰色）。
- **右侧（预测模块）**：方块"Prediction Module（条件化于 $\tau^k_{\text{ego}}$）"，接收三条候选轨迹并输出三组目标车预测轨迹（虚线）。
- **选优箭头**：规划模块从三组结果中选出全局最优，标注"Select globally safest + efficient plan"。
- **核心标注**：用红色标出"Frozen Robot Problem"（当 ego 意图未知时，预测模块预测对方切入 ego 路径）；绿色标出解决方案。

### AI 生成 Prompt

```
Create a bidirectional prediction-planning loop diagram for an academic paper illustrating the PiP (Planning-informed Prediction) method.

Scene (center): Bird's-eye view of a road. 
- Green car (ego-vehicle) at bottom center 
- Blue car (target agent) ahead and slightly right
- Gray car (context agent) to the left

Left side — "Planning Module":
- Rectangle labeled "Ego Planning Module"
- Three curved arrows emanating from the green car: three candidate trajectories τ¹_ego (red), τ²_ego (blue), τ³_ego (green) going forward

Right side — "Conditional Prediction Module":
- Rectangle labeled "Prediction Module (conditioned on τᵏ_ego)"
- For each candidate ego trajectory, show a corresponding dashed predicted trajectory for the blue target car:
  - τ¹_ego → target car predicts aggressive lane change (collision risk!)
  - τ²_ego → target car predicts staying in lane
  - τ³_ego → target car predicts yielding

Bottom — "Plan Selection":
- Arrow from prediction results to "Select τ²_ego: globally safest + most efficient"

Callout box in red: "Without PiP (Frozen Robot Problem): predictor assumes worst case → ego halts indefinitely"
Callout box in green: "With PiP: ego's intent conditions predictions → bidirectional interaction modeled"

Style: clean bird's-eye view diagram, white background, academic style, colored trajectory curves with dashed prediction lines, sans-serif labels, journal-quality.
```

---

## Fig. 9：MADDPG 集中训练分散执行架构

### 插入位置

在 `\subsubsection{MADDPG: Centralized Training, Decentralized Execution}` 内、MADDPG 梯度公式（式 \ref{eq:maddpg}）之后、`\paragraph{Impact on MAAD.}` 之前（约第 532 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/fig9_maddpg_ctde.pdf}
  \caption{MADDPG 集中训练–分散执行（CTDE）架构。训练阶段：集中式评论家 $Q_i(\mathbf{o}, a^1, \dots, a^N)$ 接收所有智能体的联合观察与动作，在稳态联合分布下估计价值函数；执行阶段：每个分散式演员 $\pi_i(a^i \mid o^i)$ 仅依赖本地观察，无需全局协调。}
  \label{fig:maddpg}
\end{figure}
```

### 图表设计说明

- **左半（训练阶段，蓝色底色）**：
  - 三个 Agent（圆形）各自输出 $o^i, a^i$；
  - 所有 $o^i, a^i$ 汇入中央"Centralized Critic $Q_i$"（大方块）；
  - Critic 输出 $Q_i$ 值，反向传播梯度至各 Actor（用橙色虚线）；
  - 标注"Global state/action access: Training Only"。
- **右半（执行阶段，绿色底色）**：
  - 三辆汽车图标，每辆仅接收本地摄像头图像 $o^i$，各自运行"Decentralized Actor $\pi_i$"，输出独立动作 $a^i$；
  - 标注"No communication required at runtime"。
- **中间分隔线**：灰色竖线，标注"Training ↔ Deployment"。

### AI 生成 Prompt

```
Create a side-by-side architecture diagram illustrating MADDPG (Multi-Agent Deep Deterministic Policy Gradient) Centralized Training, Decentralized Execution (CTDE) paradigm for an academic paper.

LEFT PANEL — "Centralized Training Phase" (light blue background):
- Three agent icons (colored circles: Agent 1 red, Agent 2 green, Agent 3 blue) each with:
  - A small "Decentralized Actor πᵢ(aⁱ|oⁱ)" block
  - Arrows labeled "oⁱ" (observation) and "aⁱ" (action) flowing downward
- All observation and action arrows (o¹,a¹), (o²,a²), (o³,a³) converge into a large central box:
  "Centralized Critic Qᵢ(o, a¹, a², a³)"
- Orange dashed gradient arrows flowing back up from Critic to each Actor labeled "∇θᵢJ"
- Label at bottom: "Joint state access — training only"

RIGHT PANEL — "Decentralized Execution Phase" (light green background):
- Three car icons with local sensor feeds (camera icon → local observation oⁱ only)
- Each car has its own small "Actor πᵢ" box producing action aⁱ independently
- NO connections between agents
- Label: "No V2X communication required at runtime"

CENTER: vertical gray dashed line labeled "Training ↔ Deployment"

Style: clean academic diagram, flat design, white background with light colored panel backgrounds, clear arrows, sans-serif font, suitable for journal publication.
```

---

## Fig. 10：V2VNet V2X 中间特征融合

### 插入位置

在 `\subsection{Cooperative Perception via V2X: V2VNet}` 内、V2VNet 聚合公式之后（约第 613 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/fig10_v2vnet.pdf}
  \caption{V2VNet 三种 V2X 信息共享策略对比（上）及中间特征图融合管道（下）。原始传感器数据带宽过高、高层轨迹表示丢失上下文，而中间特征图在带宽与感知精度之间取得最优折中。接收车辆通过空间感知 GNN 对齐并融合邻居特征图，用于联合感知与预测。}
  \label{fig:v2vnet}
\end{figure}
```

### 图表设计说明

- **上半部分（三种策略对比）**：
  - 三列图标：①原始 LiDAR 点云（紫色）+ 标注"High Bandwidth (infeasible)"；②边界框列表（橙色）+ 标注"Low BW but loses context"；③特征图矩阵（绿色）+ 标注"Optimal tradeoff ✓"。
- **下半部分（融合管道）**：
  - 两辆汽车鸟瞰图，距离 ≤70m；
  - 左车（SDV A）：CNN Backbone → 特征图 $\mathbf{F}_A$，广播给右车；
  - 右车（SDV B）：接收 $\mathbf{F}_A$，空间变换 $T_{A \to B}$，与自身特征图 $\mathbf{F}_B$ 拼接输入 GNN 聚合模块，输出融合特征 $\mathbf{F}_B^{\text{fused}}$ → 联合感知与预测头。

### AI 生成 Prompt

```
Create a two-part technical diagram for an academic paper illustrating V2VNet's V2X cooperative perception approach.

TOP SECTION — "Three V2X Sharing Strategies Comparison":
Three columns with icons and labels:
1. "Raw LiDAR Data": Purple point cloud icon → "Very High Bandwidth: infeasible (×)"
2. "High-level Bounding Boxes": Orange boxes list → "Low BW, but loses context (△)"  
3. "Intermediate Feature Maps": Green matrix/tensor grid → "Optimal Bandwidth-Accuracy Tradeoff (✓)" [highlighted with green border]

BOTTOM SECTION — "V2VNet Feature Fusion Pipeline":
- Bird's-eye road view with two autonomous vehicles (SDV A and SDV B) within 70m range, connected by a wireless signal arc labeled "V2X link"

SDV A (left):
- Camera/LiDAR sensors → CNN Backbone → Compressed Feature Map F_A (tensor icon) → broadcast arrow to SDV B

SDV B (right, ego vehicle):
- Own sensors → CNN Backbone → Feature Map F_B
- Receives F_A → Spatial Transformation block T_{A→B} (alignment arrows) 
- F_B and transformed F_A → GNN Aggregation Module
- Output: F_B^fused → "Joint Perception & Prediction Head" → detection boxes + trajectory predictions

Style: clean technical diagram, white background, purple/orange/green color coding for the three strategies, bird's-eye road view with simplified car icons, academic journal quality, sans-serif font.
```

---

## Fig. 11：LLM 认知驾驶智能体对比概览

### 插入位置

在 `\section{LLM-Based Cognitive Agents}` 导引段落结束处、`\subsection{Drive Like a Human}` 之前（约第 636 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\linewidth]{figures/fig11_llm_overview.pdf}
  \caption{四种基于 LLM 的认知驾驶智能体架构概览。各方法在 LLM 功能角色（横轴）和底层执行控制机制（纵轴）上呈现明显差异：Drive Like a Human 以链式推理进行场景解读但无记忆；DiLu 引入反思与记忆库实现持续适应；GPT-Driver 将轨迹生成转化为语言建模任务；LanguageMPC 通过分层神经符号架构解决实时性问题。}
  \label{fig:llm_overview}
\end{figure}
```

### 图表设计说明

- **形式**：$2 \times 2$ 象限图，横轴为"LLM Role"（High-Level Reasoning ↔ Trajectory Generation），纵轴为"Low-Level Control"（External Interpreter ↔ Integrated MPC）。
- **四个象限各放一个方法**：
  - 右上：Drive Like a Human（链式推理，外部控制器）
  - 左上：DiLu（推理+记忆，外部控制器）
  - 右下：GPT-Driver（轨迹语言建模，自身即控制器）
  - 左下（空白或标注 "LanguageMPC"）：LLM 策略 + MPC 硬控制
- **每个方法方块内**：方法名 + 核心特性 + 一个微型图标（链式思考气泡/记忆库/token 序列/双层架构）。
- **颜色**：四个象限各用淡色背景区分（蓝/绿/橙/紫）。

### AI 生成 Prompt

```
Create a 2×2 quadrant comparison diagram for an academic paper comparing four LLM-based autonomous driving agents.

Quadrant axes:
- Horizontal axis: "LLM Role" — left: "Scene Reasoning", right: "Trajectory Generation"
- Vertical axis: "Low-Level Control" — bottom: "Integrated Controller", top: "External Interpreter"

Four quadrants (each as a colored rounded rectangle with label and icon):

TOP-LEFT quadrant (light blue): 
"Drive Like a Human (Fu et al. 2023)"
Icon: thought bubble with "Obs→Reason→Decide" chain
Key: "Chain-of-Thought reasoning, no memory, outputs text decisions"

TOP-RIGHT quadrant (light green):
"DiLu (Wen et al. 2023)"  
Icon: brain with memory bank cylinder
Key: "Reasoning + Reflection + Memory retrieval → continual adaptation"

BOTTOM-RIGHT quadrant (light orange):
"GPT-Driver (Mao et al. 2023)"
Icon: text token stream "w₁ w₂ ... wL → trajectory"
Key: "Motion planning as language modeling, in-context learning"

BOTTOM-LEFT quadrant (light purple):
"LanguageMPC (Sha et al. 2025)"
Icon: two-layer pyramid (LLM @ 1Hz on top, MPC @ 20Hz below)
Key: "Strategic LLM + real-time MPC, neuro-symbolic hierarchy"

Center intersection: small icon labeled "LLM"

Axis labels styled as clean arrows with text. Each quadrant has a distinct pastel background.

Style: clean academic infographic, white background for axis area, pastel colored quadrants, flat design, sans-serif font, suitable for journal figure.
```

---

## Fig. 12：LanguageMPC 双层次控制架构

### 插入位置

在 `\subsection{LanguageMPC: Neuro-Symbolic Hierarchical Control}` 内、系统双时间尺度描述（enumerate 列表）之后、`\paragraph{Comparison Across LLM Methods.}` 之前（约第 780 行后）：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.88\linewidth]{figures/fig12_languagempc.pdf}
  \caption{LanguageMPC 双时间尺度神经符号控制架构。战略层（$\sim$1--2\,Hz）：LLM 解析自然语言场景描述，生成目标车道 $l^*$、目标速度 $v^*$ 及 MPC 代价权重向量 $\mathbf{w}$；执行层（10--20\,Hz）：MPC 在车辆动力学约束和硬安全约束下求解受约束轨迹优化（式~\ref{eq:mpc}），以低延迟闭环输出控制指令。}
  \label{fig:languagempc}
\end{figure}
```

### 图表设计说明

- **上层（LLM 战略层，橙色底色）**：
  - 输入："Scene Description (NL)"（文字输入框）→ LLM（大脑图标或 GPT 图标）；
  - 输出："Behavioral Directive: 'Overtake slow vehicle, merge left'"、参数包：$l^*, v^*, \mathbf{w}$（数值向量）；
  - 时钟标注：$\sim$1--2\,Hz。
- **连接箭头**：从上层向下，粗实线，标注"High-level parameters"。
- **下层（MPC 执行层，蓝色底色）**：
  - 输入：$l^*, v^*, \mathbf{w}$ + 车辆当前状态 $x_k$；
  - MPC 求解器方块：标注约束优化公式（简化版：$\min \sum \mathbf{w}^\top \phi(x_k, u_k)$ s.t. dynamics + safety）；
  - 输出：控制指令 $u^*$（转向、油门/刹车）→ 车辆图标；
  - 时钟标注：10--20\,Hz。
- **反馈箭头**：从车辆状态反馈回上层（绿色虚线，标注"State feedback"）。
- **右侧对比标注**：竖向对比框，标注"LLM latency: ~500ms" vs. "MPC cycle: ~50ms"。

### AI 生成 Prompt

```
Create a hierarchical two-level control architecture diagram for LanguageMPC autonomous driving system, for an academic paper.

TOP LEVEL — "Strategic Layer: LLM @ ~1-2 Hz" (light orange background rectangle):
- Input box on left: "Natural Language Scene Description: 'A slow truck is blocking the right lane, clear road ahead on left'"
- Central block: Large Language Model (LLM) — show a brain/GPT icon inside a rectangle
- Output on right: Three parameter boxes:
  1. "Target Lane l* = left lane"
  2. "Target Speed v* = 60 km/h"  
  3. "MPC Cost Weights w = [w_lane, w_speed, w_comfort]"
- Clock badge: "~1-2 Hz (low frequency)"

Downward thick arrow labeled: "High-Level Parameters Passed to MPC"

BOTTOM LEVEL — "Execution Layer: MPC @ 10-20 Hz" (light blue background rectangle):
- Input on left: parameters (l*, v*, w) from LLM + "Current State xₖ (position, velocity, heading)"
- Central block: "MPC Solver" — shows minimization: min Σ w^T φ(xₖ,uₖ) subject to: vehicle dynamics f(xₖ,uₖ), safety constraints g(xₖ,uₖ)≤0
- Output on right: "Control Commands u* (steering δ, throttle/brake a)" → small car icon
- Clock badge: "10-20 Hz (real-time)"

Green dashed feedback arrow from car back up to LLM input labeled "State Feedback"

Right side: small comparison table:
"LLM query latency: ~200-500ms"
"MPC solve time: ~5-50ms"
"→ Decoupling enables real-time safety"

Style: clean technical architecture diagram, white background with colored level backgrounds, thick downward arrows between levels, sans-serif font, academic journal quality.
```

---

## 附录：LaTeX 图表引用汇总

在将所有图表生成并保存为 PDF/PNG 文件后，建议在 `revised.tex` 的 preamble 中添加 `figures/` 目录路径：

```latex
\graphicspath{{figures/}}
```

所有图片文件命名建议：

| 文件名 | 图表 |
|--------|------|
| `fig1_paradigm_timeline.pdf` | Fig. 1 三范式时间线 |
| `fig2_taxonomy.pdf` | Fig. 2 分类体系总图 |
| `fig3_pomdp_vs_posg.pdf` | Fig. 3 POMDP vs POSG |
| `fig4_dave2_architecture.pdf` | Fig. 4 DAVE-2 架构 |
| `fig5_chauffeurnet_pipeline.pdf` | Fig. 5 ChauffeurNet 管道 |
| `fig6_social_lstm.pdf` | Fig. 6 Social LSTM 池化 |
| `fig7_vectornet.pdf` | Fig. 7 VectorNet GNN |
| `fig8_pip_loop.pdf` | Fig. 8 PiP 双向环 |
| `fig9_maddpg_ctde.pdf` | Fig. 9 MADDPG CTDE |
| `fig10_v2vnet.pdf` | Fig. 10 V2VNet 特征融合 |
| `fig11_llm_overview.pdf` | Fig. 11 LLM 方法对比 |
| `fig12_languagempc.pdf` | Fig. 12 LanguageMPC 架构 |

---

## 工具使用建议

| 工具 | 适合图表类型 | 备注 |
|------|-------------|------|
| **DALL·E 3 (ChatGPT/API)** | 概念图、信息图（Fig. 1, 2, 11） | 对文字标注支持较好 |
| **GPT-4o with image generation** | 所有图表 | 可迭代修改，最适合本任务 |
| **Midjourney v6** | 视觉效果图（Fig. 10 场景图） | 需配合 ControlNet 控制布局 |
| **Adobe Firefly** | 学术风格图表 | 支持矢量导出 |
| **Stable Diffusion + ControlNet** | 所有图表（布局精确控制） | 需要手绘草图作为 ControlNet 输入 |
| **Napkin.ai / Whimsical** | 流程图、架构图（Fig. 3-9, 12） | 可导出 SVG/PDF，质量最高 |

**强烈推荐**：对于学术论文中需要精确数学标注的架构图（Fig. 3–10, 12），建议先用 DALL·E 3 或 GPT-4o 生成草图，再使用 **Inkscape** 或 **draw.io** 进行后处理（添加准确的 LaTeX 公式标注），确保学术严谨性。对于信息型概述图（Fig. 1, 2, 11），可直接使用 AI 工具生成。
