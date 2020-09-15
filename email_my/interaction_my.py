def fun2():
    """发邮件
    """
    from email.mime.text import MIMEText

    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

    import smtplib

    # 输入Email地址和口令:
    from_addr = '1293909048@qq.com'
    password = 'uxzsljbuxkjngchj'
    to_addr = '928711070@qq.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'

    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    # server.starttls() # 如果是SSL，则用 587 端口，再加上这句代码就行了
    server.set_debuglevel(1)    # 打印出和SMTP服务器交互的所有信息
    server.login(from_addr, password)   # 登录SMTP服务器
    server.sendmail(from_addr, [to_addr], msg.as_string())    # 发邮件
    server.quit()

def fun1():
    """收邮件
    """
    from email.parser import Parser
    import poplib

    # 输入邮件地址, 口令和POP3服务器地址:
    email = '1293909048@qq.com'
    password = 'uxzsljbuxkjngchj'
    pop3_server = 'pop.qq.com'

    # 连接到POP3服务器:
    server = poplib.POP3_SSL(pop3_server)
    # 可以打开或关闭调试信息:
    server.set_debuglevel(1)

    # 身份认证:
    server.user(email)
    server.pass_(password)

    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    resp, lines, octets = server.retr(index)

    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)
    print(msg)
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()

fun1()

