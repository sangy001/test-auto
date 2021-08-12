import requests
import os


def send_message():
    
    if os.getenv("WEIXIN_URL") is None:
        url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=62002e06-2ebf-41c3-a17f-b99b31b284c2"
    else:
        url = os.getenv("WEIXIN_URL")

    # url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=62002e06-2ebf-41c3-a17f-b99b31b284c2"  # test 机器人
    # url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=7e39ce84-77c9-4882-b637-314a8ceb52bd"  # dce406机器人
    header = {
        "Content-Type": "application/json"
    }

    body = {
        "msgtype": "markdown",
        "markdown": {
            "content":
                f"DX-ARCH已经安装完成\n" 
            }
    }
    response = requests.post(url=url, json=body, headers=header)
    print(response.content)


if __name__ == "__main__":
    # initLogging()
    print("run")
    send_message()