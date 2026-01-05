from flask import Flask

app = Flask(__name__)


YOUR_NAME = "智慧养老平台初步"

@app.route('/')
def show_name():
    # 一个极简的HTML页面
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{YOUR_NAME} 的网站</title>
        <style>
            body {{
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
                font-family: Arial, sans-serif;
            }}
            h1 {{
                font-size: 5em;
                color: white;
                text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
            }}
        </style>
    </head>
    <body>
        <h1>{YOUR_NAME}</h1>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    print(f"✅ 网站启动！正在显示: {YOUR_NAME}")
    print("🌐 请用浏览器访问: http://127.0.0.1:5000")
    app.run(debug=True)