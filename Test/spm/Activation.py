
# try create a activation service ,now already use user and password implement
# import base64
# import hashlib
# import re
# import uuid
#
# import pyperclip
# import wmi
#
#
# class acv():
#     @staticmethod
#     def getcode():
#         c = wmi.WMI()
#         # CPU序列号
#         code = ""
#         for cpu in c.Win32_Processor():
#             code = cpu.ProcessorId.strip()
#         mac = uuid.uuid1().hex[-12:].upper()
#
#         mac = "".join(re.findall(r".{2}", mac))
#         return mac + code.replace("B", "F")
#
#     @staticmethod
#     def inputacvcode():
#         machineID = acv.getcode()
#         print('''机器识别码：
#     {}
# --机器码已复制到剪切板按Ctrl+V即可粘贴到其他地方--
#         '''.format(machineID))
#
#         pyperclip.copy(machineID)
#         inputcode = input("请输入激活码:")
#         if acv.checkcode(machineID, inputcode):
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def checkcode(ID, code):
#         s = str(base64.b64encode(ID.encode("utf-8")), "utf-8")
#         m = hashlib.md5()
#         m.update(s.encode("utf8"))
#         strc = m.hexdigest()
#         if str(strc) == code:
#             return True
#         else:
#             return False
