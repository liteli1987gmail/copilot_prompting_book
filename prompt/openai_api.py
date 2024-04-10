# me: 直接在python文件的头部写文档字符串的后果是：
"""
open the csv file called "nfl_offensive_stats.csv" and read in
the csv data from the file
"""
# copilot: ? 

from openai import OpenAI
class OpenAIAutoCompleteClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def complete(self, prompt):
        client = OpenAI(api_key=self.api_key, base_url="https://api.moonshot.cn/v1")
        completion = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {
                    "role": "system",
                    "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"
                },
                {
                    "role": "user",
                    "content": "你好，我叫李特丽,1+1等于几？"
                }
            ],
            temperature=0.3
        )
        return completion.choices[0].message



# 更改前的代码
def calculate_(length, width):
    return length * width
