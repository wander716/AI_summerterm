import os
from http import HTTPStatus
from dashscope import Application

API_KEY = "sk-xxx"  # 内置API密钥

# 你的应用 ID（在百炼控制台创建应用后获取）
APP_ID = "4b668f15d6bf4733b42125d4052e6473"

def chat():
    print("=== 我是你的饮食小助手：知食 ===")
    print("输入你的饮食需求（输入 exit 退出）")

    while True:
        prompt = input("\n用户: ")
        if prompt.lower() in ["exit", "quit", "退出"]:
            print("再见 👋")
            break
    
        response = Application.call(
                api_key=API_KEY,
                app_id=APP_ID,
                prompt=prompt
            )
    
        if response.status_code != HTTPStatus.OK:
            print(f"\n❌ 出错：")
            print(f"request_id={response.request_id}")
            print(f"code={response.status_code}")
            print(f"message={response.message}")
            print("参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
        else:
            print(f"\nAI: {response.output.text}")

if __name__ == "__main__":
    chat()
