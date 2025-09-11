# 知食 - 你的饮食小助手

一个基于DashScope API的营养膳食助手，提供科学、健康、个性化的饮食建议。

## 功能特性

- 个性化饮食建议
- 食物营养信息查询
- 详细菜谱生成
- 专业饮食指导

## 项目结构

```
.
├── index.html          # 前端界面
├── backend.py          # 后端服务
├── requirements.txt    # 依赖列表
├── agent.py           # 原始命令行版本
└── prompts.md         # AI角色设定
```

## 安装和运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行后端服务

```bash
python backend.py
```

默认运行在 `http://localhost:5000`

### 3. 打开前端页面

在浏览器中打开 `index.html` 文件

## 使用说明

1. 直接在右侧输入你的饮食需求
2. 点击"发送"获取个性化饮食建议

## API接口

### /chat (POST)

与AI助手进行对话

**请求参数:**
```json
{
  "prompt": "你的问题"
}
```

**响应:**
```json
{
  "success": true,
  "response": "AI的回答"
}
```

## 开发指南

### 前端开发

前端使用纯HTML、CSS和JavaScript实现，文件为 `index.html`。

### 后端开发

后端使用Flask框架实现，主要文件为 `backend.py`。

## 注意事项

1. 后端服务必须在运行状态才能正常使用前端页面
2. 确保网络连接正常

## 许可证

MIT
