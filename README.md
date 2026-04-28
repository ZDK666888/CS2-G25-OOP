# 个人财务与数字资产管理系统

> Personal Finance and Digital Asset Management System with Blockchain-style Audit Ledger

本项目是 JC1503 Object-Oriented Programming 小组大作业，使用 Python 开发一个面向对象的个人数据管理系统。系统用于管理个人账户、收入、支出、转账、预算分类、数字资产和操作审计记录，并通过区块链式审计日志记录关键操作历史。

项目重点不是实现真实区块链网络，而是将“区块链式哈希链”作为审计日志机制，用于提升数据可追踪性和系统专业性。主业务系统仍然完整支持创建、查询、更新、删除、文件保存和重新加载，确保符合 OOP 作业要求。

---

## 1. 项目定位

### 1.1 中文名称

个人财务与数字资产管理系统 + 区块链式审计日志

### 1.2 英文名称

Personal Finance and Digital Asset Management System with Blockchain-style Audit Ledger

### 1.3 核心目标

开发一个完整、可运行、可持久化保存数据的 Python OOP 系统，用于模拟真实个人财务管理场景。

系统需要做到：

- 支持账户、交易、分类、预算和数字资产管理。
- 支持记录的创建、查询、更新和删除。
- 支持数据保存到文件，并在程序重启后恢复状态。
- 使用面向对象方式组织系统结构。
- 自己实现并在业务中使用指定数据结构。
- 使用区块链式审计日志追踪关键操作。
- 提供测试，证明核心功能和数据结构可靠。

---

## 2. 项目背景

个人财务管理是一个典型的数据管理场景。用户通常需要记录不同账户中的余额、收入来源、日常支出、账户间转账、预算分类和数字资产信息。

普通财务系统只关注当前数据状态，而本项目额外引入区块链式审计日志：

- 业务数据可以正常修改或删除，满足真实使用需求。
- 每次关键操作都会写入审计链，形成不可随意篡改的操作历史。
- 审计链通过 `previous_hash` 和 `current_hash` 连接区块，用于验证历史记录是否被修改。

这种设计兼顾了实用性和专业性：主系统满足 CRUD 和持久化要求，审计链体现数据完整性和追踪能力。

---

## 3. 系统功能范围

### 3.1 账户管理

系统支持管理多种账户，例如：

- 现金账户
- 银行账户
- 数字钱包账户
- 投资账户

账户管理功能包括：

- 创建账户
- 查看账户
- 更新账户信息
- 删除账户
- 查看账户余额
- 根据账户 ID 快速查找账户

---

### 3.2 交易管理

系统支持三类核心交易：

- 收入交易：增加账户余额
- 支出交易：减少账户余额
- 转账交易：从一个账户扣款，向另一个账户入账

交易管理功能包括：

- 创建收入记录
- 创建支出记录
- 创建转账记录
- 修改交易信息
- 删除错误交易
- 查询交易详情
- 按 ID 查询交易
- 按金额范围查询交易
- 按日期、分类或关键词查询交易
- 浏览交易时间线

---

### 3.3 分类与预算管理

系统使用树结构组织财务分类，例如：

```text
Expense
├── Food
│   ├── Grocery
│   └── Restaurant
├── Transport
│   ├── Bus
│   └── Taxi
└── Entertainment
    ├── Games
    └── Movies
```

分类和预算功能包括：

- 创建分类
- 查看分类树
- 为分类设置预算
- 查询分类预算
- 递归统计某个分类及其子分类的总支出

---

### 3.4 数字资产管理

系统将数字资产作为个人财务的一部分进行记录，例如：

- 数字钱包余额
- 虚拟资产账户
- 投资账户
- 积分或其他数字化资产

本项目不实现真实加密货币交易、挖矿、共识算法或智能合约，只记录和管理用户的数字资产数据。

---

### 3.5 待处理交易队列

系统使用队列保存待处理交易。

典型场景：

- 用户先创建一批 pending transactions。
- 系统按先进先出顺序处理这些交易。
- 先加入队列的交易先被执行。

这体现 Queue 的 FIFO 特性。

---

### 3.6 撤销操作

系统使用栈支持撤销最近一次关键操作。

可撤销操作包括：

- 撤销新增交易
- 撤销删除交易
- 撤销更新交易

这体现 Stack 的 LIFO 特性。

---

### 3.7 区块链式审计日志

系统为关键操作生成审计区块，例如：

- 创建账户
- 修改账户
- 删除账户
- 创建交易
- 修改交易
- 删除交易
- 处理待处理交易
- 执行撤销操作

每个审计区块包含：

- 区块编号
- 时间戳
- 操作类型
- 目标记录 ID
- 操作摘要
- 前一个区块哈希
- 当前区块哈希

审计链功能包括：

- 追加审计区块
- 查看操作历史
- 验证审计链完整性
- 检测审计数据是否被篡改

---

## 4. OOP 设计要求对应

本项目将通过以下方式体现面向对象设计：

| OOP 要求 | 本项目实现方式 |
|---|---|
| 类和对象 | 使用 Account、Transaction、Budget、AuditBlock、FinanceSystem 等类 |
| 封装 | 账户余额、交易变更和审计写入通过方法控制，不允许随意直接修改 |
| 继承 | Transaction 派生 IncomeTransaction、ExpenseTransaction、TransferTransaction |
| 多态 | 不同交易类型实现统一的 apply 和 revert 行为 |
| 组合 | FinanceSystem 组合账户管理、交易管理、分类管理、审计管理和存储模块 |
| 抽象类或基类 | 使用 BaseRecord、BaseTransaction 等定义公共属性和接口 |
| 自定义异常 | 使用 InvalidAmountError、RecordNotFoundError、InsufficientFundsError 等异常 |

---

## 5. 数据结构使用计划

本项目必须自己实现并实际使用指定数据结构，不能只写孤立示例。

| 数据结构 | 业务用途 | 设计理由 |
|---|---|---|
| Hash Table / Map | 根据 account_id、transaction_id 快速查找记录 | 平均 O(1) 查找，适合 ID 精确查询 |
| Binary Search Tree | 按金额或日期组织交易，支持范围查询和排序输出 | 平均 O(log n) 插入和搜索，适合结构化查询 |
| Tree | 财务分类树 | 分类天然具有层级关系，适合递归遍历 |
| Doubly Linked List | 交易时间线 | 支持上一笔和下一笔交易的双向浏览 |
| Stack | 撤销最近操作 | 后进先出符合 undo 行为 |
| Queue | 待处理交易队列 | 先进先出符合 pending transaction 处理流程 |
| Blockchain-style Ledger | 操作审计日志 | 通过哈希链实现操作历史追踪和完整性验证 |

---

## 6. 推荐项目目录结构

```text
CS2-G25-OOP/
├── main.py
├── README.md
├── CLAUDE.md
├── progress.md
├── requirements.txt
├── data/
│   └── system_state.json
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── cli.py
│   ├── exceptions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── account.py
│   │   ├── transaction.py
│   │   ├── category.py
│   │   ├── budget.py
│   │   └── audit.py
│   ├── managers/
│   │   ├── __init__.py
│   │   ├── finance_system.py
│   │   ├── account_manager.py
│   │   ├── transaction_manager.py
│   │   ├── category_manager.py
│   │   └── audit_manager.py
│   ├── data_structures/
│   │   ├── __init__.py
│   │   ├── doubly_linked_list.py
│   │   ├── stack.py
│   │   ├── queue.py
│   │   ├── tree.py
│   │   ├── binary_search_tree.py
│   │   └── hash_table.py
│   └── storage/
│       ├── __init__.py
│       └── json_storage.py
└── tests/
    ├── test_accounts.py
    ├── test_transactions.py
    ├── test_data_structures.py
    ├── test_storage.py
    ├── test_audit_ledger.py
    └── test_system_flow.py
```

说明：实际开发时可以根据实现复杂度适当调整，但必须保持模块职责清晰。

---

## 7. 核心类设计

### 7.1 模型类

#### BaseRecord

所有业务记录的基类。

主要职责：

- 保存通用字段，例如 id、created_at、updated_at。
- 提供基础序列化接口，例如 to_dict 和 from_dict。

#### Account

表示一个财务账户。

主要职责：

- 保存账户名称、账户类型、余额等信息。
- 通过 deposit、withdraw、transfer 等方法修改余额。
- 防止非法金额或余额不足导致错误状态。

#### Transaction

交易抽象基类。

主要职责：

- 保存交易通用字段，例如 transaction_id、amount、date、category、description。
- 定义 apply 和 revert 接口。

#### IncomeTransaction

收入交易。

主要职责：

- 执行时增加目标账户余额。
- 撤销时减少目标账户余额。

#### ExpenseTransaction

支出交易。

主要职责：

- 执行时减少目标账户余额。
- 撤销时恢复目标账户余额。

#### TransferTransaction

转账交易。

主要职责：

- 从 source_account 扣款。
- 向 target_account 入账。
- 撤销时反向恢复账户余额。

#### CategoryNode

财务分类树节点。

主要职责：

- 保存分类名称。
- 管理父分类和子分类关系。
- 支持递归遍历。

#### Budget

预算记录。

主要职责：

- 绑定某个分类。
- 保存预算周期和预算金额。
- 用于后续预算统计和超支检查。

#### AuditBlock

区块链式审计日志节点。

主要职责：

- 保存操作摘要。
- 保存 previous_hash 和 current_hash。
- 支持审计链完整性验证。

---

### 7.2 管理类

#### FinanceSystem

系统总协调者。

主要职责：

- 组合各个 manager。
- 统一协调账户、交易、分类、预算、审计和存储流程。
- 为 CLI 提供高层接口。

#### AccountManager

账户管理器。

主要职责：

- 创建、查询、更新、删除账户。
- 使用 HashTable 维护账户索引。

#### TransactionManager

交易管理器。

主要职责：

- 创建、查询、更新、删除交易。
- 同步维护交易索引、交易时间线、BST 查询结构。
- 确保交易变更与账户余额一致。

#### CategoryManager

分类管理器。

主要职责：

- 创建和展示分类树。
- 递归遍历分类。
- 统计某个分类及其子分类的总支出。

#### AuditManager

审计管理器。

主要职责：

- 在关键操作后追加 AuditBlock。
- 展示审计链。
- 验证审计链完整性。

#### JsonStorage

文件存储模块。

主要职责：

- 保存完整系统状态到 JSON 文件。
- 从 JSON 文件恢复系统状态。
- 首次运行时生成初始数据。

---

## 8. 数据持久化设计

系统使用 JSON 文件保存数据，推荐保存到：

```text
data/system_state.json
```

需要持久化的数据包括：

- 账户列表
- 交易列表
- 分类树
- 预算记录
- 待处理交易队列
- 审计链

系统启动时：

1. 检查是否存在 `data/system_state.json`。
2. 如果存在，则加载历史数据。
3. 如果不存在，则生成初始数据集。
4. 加载完成后重建 HashTable、BST、DoublyLinkedList 等运行时索引结构。

系统退出时：

1. 将当前系统状态序列化。
2. 写入 JSON 文件。
3. 确保下次运行可以恢复当前状态。

---

## 9. 初始数据要求

首次运行时建议生成一批较完整的示例数据：

- 4–5 个账户
- 30–50 条交易
- 10 个以上分类节点
- 若干预算记录
- 对应的审计区块

目的：

- 避免系统看起来像空壳。
- 满足作业对 substantial number of records 的要求。
- 方便演示搜索、统计、BST 范围查询、分类树递归遍历和审计验证。

---

## 10. 开发阶段计划

### Phase 0：项目骨架与规则确认

目标：确认目录结构、运行方式、测试方式和基础配置。

主要任务：

- 创建项目目录结构。
- 创建 main.py。
- 创建 requirements.txt。
- 确认 CLI 作为主要交互方式。
- 确认 JSON 作为持久化格式。
- 确认使用 Python 标准库和 pytest。

验收标准：

- 可以执行 `python main.py`。
- 可以执行 `python -m pytest`。
- 目录结构清晰。

---

### Phase 1：基础模型与异常体系

目标：建立系统核心 OOP 模型。

主要任务：

- 实现 BaseRecord。
- 实现 Account。
- 实现 Transaction 抽象基类。
- 实现 IncomeTransaction、ExpenseTransaction、TransferTransaction。
- 实现基础自定义异常。

验收标准：

- 可以创建账户和不同类型交易对象。
- 交易 apply 和 revert 能正确影响账户余额。
- 非法金额、余额不足、找不到记录等错误能被安全处理。

---

### Phase 2：自定义数据结构实现

目标：完成作业要求的全部数据结构。

主要任务：

- 实现 DoublyLinkedList。
- 实现 Stack。
- 实现 Queue。
- 实现 Tree / CategoryTree。
- 实现 BinarySearchTree。
- 实现 HashTable。

验收标准：

- 每个数据结构都有测试。
- 每个数据结构都有明确业务用途。
- 不出现“实现了但系统不用”的情况。

---

### Phase 3：账户、交易、分类和预算功能

目标：完成主业务系统的 CRUD 和查询。

主要任务：

- AccountManager 支持账户 CRUD。
- TransactionManager 支持收入、支出、转账 CRUD。
- CategoryManager 支持分类树创建、展示、递归统计。
- Budget 功能支持预算设置和查询。
- 交易索引同步写入 HashTable、BST、DoublyLinkedList。

验收标准：

- 用户可以创建、修改、删除、查询账户和交易。
- 分类树可以递归统计支出。
- 交易时间线、ID 查询、金额范围查询都能工作。

---

### Phase 4：待处理队列、撤销和审计账本

目标：完成高分功能和技术亮点。

主要任务：

- 使用 Queue 实现 pending transactions。
- 使用 Stack 实现 undo。
- 实现 AuditBlock 和 AuditManager。
- 每次关键业务操作自动写入审计链。
- 实现 validate_chain。

验收标准：

- 待处理交易可以按 FIFO 顺序处理。
- Undo 可以撤销最近一次关键操作。
- 审计链可以显示所有关键操作。
- 审计链可以检测数据篡改。

---

### Phase 5：文件持久化与初始数据

目标：确保系统像真实应用一样保留状态。

主要任务：

- 使用 JSON 保存完整系统状态。
- 程序启动时自动加载已有数据。
- 首次运行时生成初始数据。
- 保存账户、交易、分类、预算和审计链。

验收标准：

- 第一次运行可以生成可用数据集。
- 退出后再次运行，之前数据仍然存在。
- 初始数据包含足够记录和实体关系。

---

### Phase 6：CLI 菜单与系统流程整合

目标：形成完整、可演示的软件系统。

主要任务：

- 实现主菜单。
- 实现账户管理子菜单。
- 实现交易管理子菜单。
- 实现分类和预算子菜单。
- 实现数据结构功能展示菜单。
- 实现审计账本菜单。
- 统一处理用户输入错误。

验收标准：

- 普通用户可以通过菜单完成所有核心操作。
- 输入非法选项、非法金额、非法 ID 时程序不崩溃。
- 菜单流程适合录制演示视频。

---

### Phase 7：测试与质量检查

目标：用测试证明系统可靠，并为报告提供证据。

主要任务：

- 编写模型单元测试。
- 编写数据结构测试。
- 编写存储测试。
- 编写审计链测试。
- 编写系统流程测试。
- 修复测试发现的问题。

验收标准：

- `python -m pytest` 可以通过。
- 测试覆盖创建、更新、删除、查询、保存、加载、错误输入和审计验证。
- 可以从测试结果中总结至少一个开发改进点，用于报告 Development and Testing 部分。

---

### Phase 8：报告和视频素材准备

目标：把代码实现转化为最终可评分材料。

主要任务：

- 整理系统设计说明。
- 整理 OOP 使用说明。
- 整理数据结构使用位置和复杂度分析。
- 整理测试过程、问题和修复。
- 准备演示视频脚本。
- 准备过程展示视频脚本。
- 明确每个组员贡献。

验收标准：

- 报告覆盖 Problem and System Design、Technical Design、Development and Testing、Reflection。
- 演示视频展示创建、查询、更新、删除、非法输入、保存加载和审计验证。
- 过程视频说明系统演进、关键问题、设计调整、测试影响和组员贡献。

---

## 11. 运行方式

### 11.1 创建虚拟环境

Windows cmd：

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

如果 `python` 命令不可用，可以尝试：

```cmd
py -3 -m venv venv
venv\Scripts\activate.bat
```

### 11.2 安装依赖

```cmd
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 11.3 运行程序

```cmd
python main.py
```

### 11.4 运行测试

```cmd
python -m pytest
```

---

## 12. 团队协作流程

本项目使用 GitHub Fork + Issue + Pull Request 工作流。

核心流程：

```text
创建 Issue
    ↓
组员 Fork 项目
    ↓
Clone 自己的 fork 到本地
    ↓
添加 upstream 指向原仓库
    ↓
同步 upstream/main 最新代码
    ↓
创建功能分支
    ↓
本地开发和测试
    ↓
提交 commit
    ↓
推送到自己的 fork
    ↓
发起 Pull Request
    ↓
Code Review
    ↓
合并到上游 main
```

详细协作命令和 Windows cmd 操作规范见 `progress.md`。

---

## 13. 推荐演示流程

演示视频建议按以下顺序展示：

1. 启动系统，展示加载已有数据或首次初始化数据。
2. 查看账户列表和余额。
3. 创建一笔收入交易。
4. 创建一笔支出交易。
5. 修改一笔交易。
6. 删除一笔错误交易。
7. 按 ID 或关键词查询交易。
8. 使用 BST 按金额范围查询交易。
9. 展示分类树，并递归统计某个分类的总支出。
10. 添加一笔 pending transaction，并从队列处理。
11. 使用 undo 撤销最近操作。
12. 查看审计链。
13. 验证审计链完整性。
14. 保存并退出。
15. 重新启动程序，证明数据没有丢失。

---

## 14. 报告写作方向

最终报告建议覆盖四个部分。

### 14.1 Problem and System Design

说明：

- 为什么个人财务管理是一个真实数据管理场景。
- 系统管理哪些实体：账户、交易、分类、预算、审计记录。
- 实体之间如何关联。
- 用户如何通过菜单与系统交互。
- 为什么该系统不是简单脚本，而是一个有状态、可扩展、可维护的软件系统。

### 14.2 Technical Design

说明：

- 类之间的职责划分。
- 如何体现封装、继承、多态、组合、抽象类和自定义异常。
- 每个数据结构在哪里使用，以及为什么适合。
- 区块链式审计日志如何工作。
- 关键操作的复杂度分析。

### 14.3 Development and Testing

说明：

- 系统从基础 CRUD 到数据结构集成，再到审计账本的演进过程。
- 遇到的关键问题，例如余额一致性、删除交易后的索引同步、保存加载后的对象重建。
- 如何通过测试发现问题并修复。
- 测试如何影响最终设计。

### 14.4 Reflection

说明：

- 哪些设计做得好，例如业务数据和审计日志分离。
- 当前限制，例如 CLI 交互不如 GUI 直观，BST 未做自动平衡。
- 如果继续开发，可以增加图形界面、报表可视化、多用户支持、加密存储等。
- 从项目中学到的 OOP、数据结构和软件工程经验。

---

## 15. 技术风险与控制

| 风险 | 控制方式 |
|---|---|
| 区块链主题偏离作业要求 | 区块链只作为审计日志，不作为主业务系统；主系统仍完整支持 CRUD |
| 数据结构显得硬塞 | 每个数据结构必须绑定真实业务功能，并在演示和报告中展示 |
| 系统范围过大 | 优先完成 CLI、CRUD、持久化、数据结构和测试，不做真实区块链网络或 GUI |
| 交易更新/删除导致余额和索引不一致 | 所有交易变更必须通过 TransactionManager 统一处理 |
| 保存加载后对象关系丢失 | JsonStorage 统一序列化和反序列化，加载后重建运行时索引 |

---

## 16. 当前最优开发顺序

1. 确认目录结构和运行方式。
2. 实现基础模型：Account、Transaction、异常体系。
3. 实现并测试六种数据结构。
4. 实现账户和交易 CRUD。
5. 集成 HashTable、BST、DoublyLinkedList。
6. 实现分类树和递归统计。
7. 实现 Queue pending transaction 和 Stack undo。
8. 实现区块链式审计账本。
9. 实现 JSON 持久化和初始数据。
10. 实现 CLI 菜单。
11. 补齐 pytest 测试。
12. 整理报告和视频脚本。

---

## 17. 项目边界

本项目明确不做以下内容：

- 不实现真实 P2P 区块链网络。
- 不实现真实加密货币交易。
- 不实现挖矿、共识算法或智能合约。
- 不开发复杂 GUI。
- 不引入大型外部框架。

项目优先级：

1. 满足 OOP 作业要求。
2. 保证系统可运行、可测试、可持久化。
3. 保证数据结构真正参与业务。
4. 保证报告和视频有清晰材料可写、可展示。
5. 在上述基础上体现区块链式审计日志的专业亮点。
