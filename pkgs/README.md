pkgs文件内包含了运行matplotlib所必备的python库。如果你的电脑纯净安装了python，运行matplotlib之前则需要安装这些库。通常情况下你可以直接使用pip命令快速安装matplotlib及其依赖库。

但在某些不能联网的电脑上，只能提前下载whl文件通过pip离线安装这些库。这个文件夹内包含的就是所有matplotlib依赖库的whl文件（包含matplotlib），您只需要现在此文件夹所有文件并运行setup.bat即可一键安装。（注意：numpy库因为大小超过100MB未能上传到github，需要您自行从网络上下载）

- 所有的库均为2019.5.10日下载的最新版本

matplotlib库所依赖的库（**注意：一定按照如下顺序安装**）：

- numpy
- pyparsing
- pytz
- six
- python_dateutil
- cycler
- kiwisolver
- matplotlib