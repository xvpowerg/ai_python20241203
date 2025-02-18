from openai import OpenAI
import json
openAiKey = ''
def handle_message(user_message):
    messages = [{"role": "system", "content": "你好!"}]
    messages.append({"role": "user", "content": user_message})
    client = OpenAI(api_key=openAiKey)
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=256,
            temperature=0.5
        )
    reply_msg = response.choices[0].message.content
    print(reply_msg)

msg = input("請問問題?(Q離開)")
while msg != "Q" and msg != "q":    
    handle_message(msg)
    msg = input("請問問題?(Q離開)")
