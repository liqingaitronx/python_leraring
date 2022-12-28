from  urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('https://www.taobao.com/')
rp.read()
print(rp.can_fetch('*','https://item.taobao.com/item.htm?spm=a21bo.jianhua.201876.20.5af911d9eP0WR1&id=574194201886&scm=1007.40986.275655.0&pvid=9651a76a-f330-4016-bbbf-bab5d642baf1'))