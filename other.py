# '''
# **********信息提示**********
# setStatusTip(str)  设置信息提示的内容 字符串
# statusBar() 懒加载用到的时候就加载
# StatusTip() 获取提示信息
# setToolTip(str) 设置提示内容
# ToolTip() 获取提示内容
# setToolTipDuration(int) 设置提示显示时间毫秒
# whatsThis() 这是啥提示
# setwhatsThis(str) 设置这是啥提示内容
#
#
# 实例：
#     鼠标停留提示
#     和标签提示
# '''
# # 导入相关模块和包
# from PyQt5.Qt import *
#
#
# # 重写QWidget类
# class Window(QMainWindow):
#     def __init__(self):
#         # 初始化参数
#         super().__init__()
#         # 懒加载，用到的时候才会创建
#         self.statusBar()
#         # 设置窗口标题
#         self.setWindowTitle('信息提示案例')
#         # 设置窗口大小
#         self.resize(500, 500)
#         # 设置鼠标停留提示
#         self.setStatusTip('主窗口')
#         # 调用函数setup_ui()
#         self.setup_ui()
#
#     def setup_ui(self):
#         # 创建一个标签
#         label = QLabel(self)
#         # 设置标签文本
#         label.setText('余生太长，不必慌张')
#         # 设置根据内容调整大小
#         label.adjustSize()
#         # 设置标签提示
#         label.setToolTip('这是一个标签')
#         # 设置标签提示显示时间 单位毫秒
#         label.setToolTipDuration(2000)
#         # 设置停留提示
#         label.setStatusTip('这是标签')
#
#
# # 启动入口
# if __name__ == '__main__':
#     # 导入相关模块和包
#     import sys
#
#     # 创建一个应用程序
#     app = QApplication(sys.argv)
#     # 创建一个窗口对象
#     window = Window()
#     # 展示窗口
#     window.show()
#     # 传递错误码 消息循环 无限循环 app.exec让程序进入循环
#     sys.exit(app.exec_())