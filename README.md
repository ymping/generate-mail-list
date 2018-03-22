# generate-mail-list
Generate mail list from SisenMESS database.

从IM软件--[布谷鸟](http://www.sisen.com)的数据中查询数据，然后生成可用于导入Outlook通讯列表。
可以使用[PyInstaller](http://www.pyinstaller.org/)打包代码成exe.

## Getting Started
1. 在数据库中执行 ` GetTopWorkGroupName.sql `
2. (可选)使用PyInstall打包代码，` pyinstaller main.py `
3. 设置定时任务，` python main.py --help ` or ` main.exe --help ` 获取帮助