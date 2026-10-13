# Java 程序员学习 Python + AI Agent：24 周个人执行计划

## 一、学习目标与节奏

**目标：** 转型 AI 应用开发岗位。  
**当前基础：** Java 开发经验；Python 基础较少；熟悉 Linux、Docker 和服务运维。  
**投入时间：** 每周 5–7 小时，按每周 6 小时规划。  
**周期：** 24 周，约 144 小时。

24 周后，目标是具备开发和展示一个完整 AI 应用项目的能力。是否达到具体岗位要求，还取决于项目质量、面试表现和岗位标准。

### 最终能力目标

- 使用 Python、Pydantic、FastAPI 编写可测试的后端服务。
- 掌握模型 API、结构化输出、Tool Calling、RAG、LangGraph 工作流与状态管理。
- 集成 PostgreSQL、Redis、现有 Java 服务和 MCP 工具。
- 使用 Docker 部署，编写测试，并处理超时、重试、日志、权限和模型调用成本。

### 每周固定学习节奏

| 学习时段 | 时长 | 任务 |
|---|---:|---|
| 第 1 天 | 2 小时 | 阅读官方教程、理解概念、运行最小示例 |
| 第 2 天 | 2 小时 | 从空文件开始写代码、调试并补充类型注解 |
| 第 3 天 | 2 小时 | 集成到项目、编写测试、提交 Git、复盘 |

每周至少产出一个可运行的代码提交。不要把所有时间都花在看视频上。

---

## 二、24 周逐日执行计划

每周安排 3 次学习，每次 2 小时。

## 第一阶段：Python 基础（第 1–4 周）

### 第 1 周：环境与基本语法

**第 1 天（2 小时）**
- 安装 Python 3.12、VS Code 或 PyCharm、Git。
- 创建虚拟环境，学习运行 `.py` 文件。
- 练习字符串、数字、布尔值和 `None`。

**第 2 天（2 小时）**
- 学习 `if`、`for`、`while`、函数和返回值。
- 实现一个命令行计算器。

**第 3 天（2 小时）**
- 学习模块导入、异常处理和文件读写。
- 编写日志分析程序：统计文件中的 `ERROR`、`WARN`、`INFO`。

**验收标准：** 能独立编写一个读取日志文件、统计错误次数并输出报告的程序。

### 第 2 周：数据结构与面向对象

**第 1 天**
- 学习 `list`、`dict`、`set`、`tuple`。
- 对比 Java 的 `ArrayList`、`HashMap` 和 Python 容器。

**第 2 天**
- 学习类、继承、组合、实例方法、类方法。
- 实现 `Server`、`Service` 两个类。

**第 3 天**
- 学习列表推导式、字典推导式、`dataclass`。
- 将服务器状态整理成结构化对象，并输出 JSON。

**验收标准：** 输入多台服务器的状态数据，能按状态筛选、排序、统计，并输出 JSON 报告。

### 第 3 周：类型注解与工程化

**第 1 天**
- 学习 `typing`、`Optional`、`list[str]`、`dict[str, int]`。
- 理解 Python 动态类型与 Java 静态类型的差异。

**第 2 天**
- 学习 Pydantic 模型、字段校验和异常。
- 定义服务器状态和告警事件的数据模型。

**第 3 天**
- 学习项目目录、依赖管理、Git 分支。
- 给代码添加类型注解，并编写基本测试。

**验收标准：** 能拒绝格式错误的输入，并将有效输入转换为标准化数据对象。

### 第 4 周：HTTP、FastAPI 与异步基础

**第 1 天**
- 学习 HTTP、REST、JSON、状态码。
- 用 FastAPI 实现 `/health`。

**第 2 天**
- 实现 `GET /servers`、`GET /servers/{id}`。
- 学习请求参数、Pydantic 请求模型和响应模型。

**第 3 天**
- 学习 `async`、`await` 的基本用法。
- 用 `httpx` 调用另一个 HTTP 服务，处理超时和错误。

**验收标准：** 服务可以启动，接口可以通过 Swagger UI 调试，输入验证和错误响应正常。

---

## 第二阶段：大模型应用开发（第 5–8 周）

### 第 5 周：模型 API 与 Prompt

**第 1 天**
- 理解 Token、上下文窗口、System Prompt、User Prompt。
- 申请一个可用的大模型 API，配置环境变量。

**第 2 天**
- 编写模型调用函数。
- 处理 API 错误、超时、重试和返回内容。

**第 3 天**
- 实现日志分析 Prompt。
- 输入一段服务器日志，输出故障摘要、可能原因和建议。

**验收标准：** 能从 Python 程序调用模型，分析一段日志并输出结果；API Key 不写入源代码或 Git。

### 第 6 周：结构化输出

**第 1 天**
- 学习 JSON Schema、Pydantic 的数据校验。

**第 2 天**
- 将模型的分析结果转换为 `severity`、`summary`、`causes`、`actions` 字段。

**第 3 天**
- 测试空内容、无效 JSON、缺少字段和错误类型。

**验收标准：** 模型返回的分析结果经过校验后才能进入业务逻辑；无法校验时能安全报错或重试。

### 第 7 周：Tool Calling

**第 1 天**
- 理解模型提出工具调用请求的机制。
- 编写 `query_server_status` 函数。

**第 2 天**
- 编写 `search_error_logs` 和 `get_service_metrics`。
- 为工具定义清晰的名称、用途、参数和返回结果。

**第 3 天**
- 将工具接入模型调用循环。
- 处理不存在的服务器、无效参数和工具执行失败。

**验收标准：** 用户可以用自然语言查询服务器，模型能选择工具，程序执行真实查询，再生成最终答复。

### 第 8 周：对话状态与会话管理

**第 1 天**
- 学习消息角色、对话历史和上下文窗口限制。

**第 2 天**
- 使用 `session_id` 保存不同用户的对话。
- 实现历史消息读取、截断与清理。

**第 3 天**
- 将聊天能力接入 FastAPI。
- 加入基础日志、错误追踪和请求验证。

**验收标准：** 两个会话的消息相互隔离，接口可连续对话，并能正确处理服务异常。

**阶段项目 A：AI 运维查询助手。** 到这里，完成一个可以演示的 LLM 应用。

---

## 第三阶段：RAG 知识库（第 9–12 周）

### 第 9 周：文档解析与切分

**第 1 天**
- 准备 10–20 份技术文档，包含 Markdown、TXT 和 PDF。

**第 2 天**
- 提取文档文本、标题、页码和来源。
- 实现固定长度切分与重叠切分。

**第 3 天**
- 为每个文本片段记录文档 ID、标题、页码和片段 ID。

**验收标准：** 输入文档能够转换为带有来源信息的文本片段。

### 第 10 周：Embedding 与向量检索

**第 1 天**
- 理解 Embedding、向量相似度和 Top-K 检索。

**第 2 天**
- 选择一个可用的 Embedding 模型。
- 学习 PostgreSQL + pgvector，建立向量存储。

**第 3 天**
- 将文档片段写入数据库，实现相似度检索。

**验收标准：** 输入一个技术问题，系统能检索出相关文档片段，并返回其来源。

### 第 11 周：RAG 问答链

**第 1 天**
- 将检索到的文本与用户问题组合成 Prompt。

**第 2 天**
- 生成基于文档的答案，并输出引用来源。

**第 3 天**
- 对无检索结果、无依据的问题设置拒答或澄清逻辑。

**验收标准：** 能回答知识库中存在的问题，给出正确来源；文档没有答案时不伪造引用。

### 第 12 周：RAG 评估与优化

**第 1 天**
- 准备至少 30 道测试题，包括有答案和无答案问题。

**第 2 天**
- 比较不同切分长度、Top-K 和检索条件。

**第 3 天**
- 记录检索命中率、引用正确性、响应延迟和错误案例。

**验收标准：** 有一份可重复执行的 RAG 测试集和评估报告。

**阶段项目 B：企业技术知识库。** 应用同时具备业务查询与文档检索能力。

---

## 第四阶段：Agent 与工作流（第 13–16 周）

### 第 13 周：理解 Agent 执行循环

**第 1 天**
- 学习规划、工具选择、观察结果和终止条件。

**第 2 天**
- 手写最小 Agent 循环，接入两个只读工具。

**第 3 天**
- 增加最大步骤数、超时、工具白名单和参数校验。

**验收标准：** 能解释并演示 Agent 每一步为什么调用某个工具，以及何时结束。

### 第 14 周：LangGraph 入门

**第 1 天**
- 学习 State、Node、Edge、START 和 END。

**第 2 天**
- 将日志分析、知识检索和工具查询拆成独立节点。

**第 3 天**
- 增加条件路由：问题属于知识咨询还是服务器查询。

**验收标准：** 能画出并实现一个有条件分支的 Agent 工作流。

### 第 15 周：状态持久化与人工审批

**第 1 天**
- 学习 checkpoint、线程 ID 和状态恢复。

**第 2 天**
- 模拟一个需要审批的操作，例如重启测试服务。

**第 3 天**
- 实现暂停、人工批准、拒绝和恢复流程。

**验收标准：** Agent 可以暂停等待审批，恢复后继续执行，并记录审批结果。

### 第 16 周：MCP 工具接入

**第 1 天**
- 理解 MCP Host、Client、Server，以及 Tools、Resources、Prompts。

**第 2 天**
- 用 Python MCP SDK 编写一个只读的服务器状态工具服务。

**第 3 天**
- 通过 MCP Client 发现工具、调用工具并处理结果。

**验收标准：** 独立 MCP Client 可以调用你编写的 MCP Server。

**阶段项目 C：状态化运维 Agent。** 具备多步骤执行、工具调用和人工审批能力。

---

## 第五阶段：生产工程化（第 17–20 周）

### 第 17 周：后端架构与数据库

**第 1 天**
- 将 API、业务逻辑、Agent、数据库访问拆分成模块。

**第 2 天**
- 用 SQLAlchemy 实现服务器、告警和任务记录的 CRUD。

**第 3 天**
- 加入事务、配置管理、数据库连接异常处理。

**验收标准：** Agent 不直接拼接 SQL；业务数据访问层可单独测试。

### 第 18 周：测试与可靠性

**第 1 天**
- 学习 Pytest、fixture、mock 和参数化测试。

**第 2 天**
- 为工具、API、检索模块编写单元测试和集成测试。

**第 3 天**
- 模拟模型超时、工具失败、空检索结果和重复请求。

**验收标准：** 核心逻辑有自动化测试，常见故障不会导致整个服务崩溃。

### 第 19 周：安全与可观测性

**第 1 天**
- 增加请求 ID、结构化日志和关键步骤耗时记录。

**第 2 天**
- 加入身份验证、用户权限、工具白名单和敏感数据脱敏。

**第 3 天**
- 记录模型调用次数、Token 用量、延迟和工具执行结果。

**验收标准：** 可以根据请求 ID 追踪一次 Agent 执行，并定位失败步骤。

### 第 20 周：Docker 部署与 Java 集成

**第 1 天**
- 编写 Python 服务的 Dockerfile 和 Compose 配置。

**第 2 天**
- 部署 Python 服务、PostgreSQL 和必要的依赖服务。

**第 3 天**
- 用现有 Java / Spring Boot 服务通过 HTTP 调用 Agent API。

**验收标准：** 能从干净环境启动服务，并从 Java 程序调用 Agent、读取结果和处理失败。

---

## 第六阶段：综合项目与求职准备（第 21–24 周）

### 第 21 周：完善 OpsPilot 核心功能

**第 1 天**
- 整合服务器状态查询、日志分析和 RAG 知识库。

**第 2 天**
- 用 LangGraph 组织任务流程，加入异常分支。

**第 3 天**
- 设计统一 API 响应结构和错误码。

**验收标准：** 三类核心能力能从同一 API 入口调用。

### 第 22 周：稳定性和效果评估

**第 1 天**
- 准备至少 30 条业务测试场景。

**第 2 天**
- 测试工具选择正确性、RAG 引用准确性和异常处理。

**第 3 天**
- 分析失败案例，优化 Prompt、检索和工具描述。

**验收标准：** 生成测试报告，明确系统在哪些问题上可靠、哪些问题仍有限制。

### 第 23 周：部署演示与项目文档

**第 1 天**
- 完成 Docker 部署和环境变量示例。

**第 2 天**
- 编写架构图、API 文档、部署手册和故障排查说明。

**第 3 天**
- 录制或准备一段 3–5 分钟的功能演示。

**验收标准：** 其他开发者能根据 README 独立启动项目并复现主要功能。

### 第 24 周：简历与面试准备

**第 1 天**
- 整理项目架构、技术选型和关键实现。

**第 2 天**
- 练习解释 Tool Calling、RAG、Agent Loop、LangGraph 和 MCP。

**第 3 天**
- 进行一次模拟面试，修改项目和简历。

**验收标准：** 能从架构、核心代码、测试结果、失败处理和设计取舍五个角度解释项目。

---

## 三、第一周实战代码：日志分析器

### 1. 创建项目目录

```bash
mkdir opspilot
cd opspilot

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
```

Windows PowerShell 激活命令：

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. 创建 `log_analyzer.py`

```python
from collections import Counter
from pathlib import Path


def analyze_logs(log_text: str) -> dict[str, int]:
    """统计日志中不同级别的数量。"""
    counts: Counter[str] = Counter()

    for line in log_text.splitlines():
        parts = line.split()

        if len(parts) < 2:
            continue

        level = parts[1].upper()

        if level in {"INFO", "WARN", "WARNING", "ERROR"}:
            if level == "WARNING":
                level = "WARN"
            counts[level] += 1

    return dict(counts)


def main() -> None:
    log_file = Path("sample.log")

    if not log_file.exists():
        print(f"日志文件不存在: {log_file}")
        return

    text = log_file.read_text(encoding="utf-8")
    report = analyze_logs(text)

    print("日志统计报告")
    for level, count in sorted(report.items()):
        print(f"{level}: {count}")


if __name__ == "__main__":
    main()
```

### 3. 创建 `sample.log`

```text
2026-10-13 ERROR database connection failed
2026-10-13 INFO service started
2026-10-13 WARN high memory usage
2026-10-13 ERROR connection timeout
```

运行：

```bash
python log_analyzer.py
```

预期结果：

```text
日志统计报告
ERROR: 2
INFO: 1
WARN: 1
```

### 4. 本周扩展练习

1. 增加 `CRITICAL` 日志级别。
2. 统计每种日志级别对应的日志内容。
3. 为 `analyze_logs()` 编写三个测试：正常输入、空输入、格式错误输入。
4. 将代码提交到 Git。

这个程序后续可以演进成 OpsPilot 的日志分析工具。

---

## 四、Java 与 Python 常见概念对照

| Python | Java 中相近的概念 |
|---|---|
| `def` | 方法定义 |
| `dict` | `Map` |
| `Counter` | 计数用的 `Map` 或集合工具 |
| `Path` | 文件路径与文件操作 API |
| `with` | 常见于自动资源管理场景 |
| `if __name__ == "__main__"` | 脚本入口判断，不完全等同于 `main()` |
| Pydantic | 数据校验与模型绑定的组合能力 |
| FastAPI | HTTP API 框架 |
| Pytest | 测试框架 |
| LangGraph | 有状态的 Agent 工作流编排框架 |

---

## 五、推荐学习资料

优先使用官方文档，不需要同时购买多套课程。

1. **Python 官方教程（第 1–3 周）**  
   https://docs.python.org/3/tutorial/

2. **FastAPI 官方教程（第 4–8 周及第 17–20 周）**  
   https://fastapi.tiangolo.com/tutorial/

3. **Pydantic 模型文档（第 3、6、17 周）**  
   https://pydantic.dev/docs/validation/latest/concepts/models/

4. **LangGraph 官方文档（第 14–16 周）**  
   https://docs.langchain.com/oss/python/langgraph/overview

5. **MCP Python SDK 教程（第 16 周）**  
   https://py.sdk.modelcontextprotocol.io/get-started/

前期选择一种能稳定使用的大模型 API 即可，不需要同时学习多个厂商 SDK，也不需要先训练自己的模型。

---

## 六、最终实战项目：OpsPilot

### 项目目标

开发一个 AI 技术支持与运维助手，整合业务查询、日志分析、知识库检索和受控工作流。

### 核心功能

- 查询服务器状态、告警与服务指标。
- 检索技术手册、部署文档和故障处理知识库。
- 分析日志并给出故障排查建议。
- 将处理过程拆分成多个步骤，并记录执行状态。
- 对高风险操作增加人工审批。
- 通过 HTTP API 供 Java / Spring Boot 系统调用。

### 建议架构

```text
用户 / Java 管理平台
        |
        v
FastAPI 接入层
        |
        v
LangGraph 工作流
   |       |       |
   v       v       v
知识检索  状态查询  日志分析
   |       |       |
   +-------+-------+
           |
           v
 PostgreSQL / pgvector
           |
           v
 业务 API / MCP 工具
```

### 建议项目目录

```text
opspilot/
├── app/
│   ├── main.py
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── agent/
│   │   ├── graph.py
│   │   ├── state.py
│   │   └── tools.py
│   ├── rag/
│   │   ├── ingest.py
│   │   └── retrieval.py
│   └── db/
├── tests/
├── documents/
├── Dockerfile
├── compose.yaml
├── pyproject.toml
├── .env.example
├── .gitignore
└── README.md
```

这是建议的组织方式，按学习进度逐步创建即可。

### 功能优先级

| 优先级 | 功能 | 交付标准 |
|---|---|---|
| P0 | 查询服务器状态 | 可调用真实或模拟业务接口 |
| P0 | 日志分析 | 输出结构化分析结果 |
| P0 | RAG 知识库 | 答案有来源，可处理无答案问题 |
| P0 | Agent 工作流 | 能调用多个工具并处理失败 |
| P1 | 人工审批 | 高风险操作必须审批 |
| P1 | Java 集成 | Spring Boot 可以调用 Agent API |
| P1 | Docker 部署 | 可按文档启动并完成健康检查 |
| P2 | 多 Agent 协作 | 仅在单 Agent 无法满足需求时扩展 |

**安全原则：** 最终项目优先以只读查询和模拟操作为主。涉及真实服务器重启、删除文件或修改数据库时，不允许模型直接执行任意 Shell 命令；必须经过工具白名单、权限校验和人工审批。

---

## 七、求职能力自测

在第 24 周结束时，逐项检查：

- [ ] **Python 工程能力：** 能独立组织项目、定义类型、编写测试和处理异常。
- [ ] **LLM 应用能力：** 能解释 Prompt、结构化输出、Tool Calling 和上下文管理。
- [ ] **RAG 能力：** 能解释文档切分、Embedding、召回、引用和效果评估。
- [ ] **Agent 能力：** 能实现工具循环、状态管理、工作流分支和人工审批。
- [ ] **工程交付能力：** 有 Docker 部署、API 文档、日志和故障处理记录。
- [ ] **项目表达能力：** 能现场演示项目，并解释架构取舍、局限和优化方向。

## 八、执行原则

1. **先掌握单 Agent，再研究多 Agent。** 工具调用、RAG、工作流和评估是优先级更高的基础。
2. **每周必须有代码产出。** 看懂教程不等于能独立开发。
3. **优先完成一个完整项目。** 可运行、可测试、可部署的项目通常比多个只有聊天功能的 Demo 更有说服力。
4. **不要过早研究模型训练。** 本计划聚焦 AI 应用开发岗位，不以训练基础模型为目标。
5. **记录实际结果。** 评估工具选择正确性、RAG 引用准确性、延迟、成本和失败率，不要在简历中夸大未经验证的指标。

> 建议现在就从第 1 周开始：搭建环境、编写日志分析器、完成三个测试并提交 Git。每周 6 小时，坚持 24 周，逐步把它演进为 OpsPilot。
