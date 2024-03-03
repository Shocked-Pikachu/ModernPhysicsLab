# ModernPhysicsLab

Modern physics lab reports written in $\LaTeX$ (2023 fall) @ School of Physics, Peking University

2023秋 近代物理实验报告，北京大学物理学院

此项目记录了本人在近代物理实验（I）这门课程中撰写的所有实验报告。由于本人在写实验报告时经历了一些折磨，现也把曾经写过的东西向大家分享出来，以期待能稍微减少一些后人的痛苦。但本人在实验和撰写实验报告这方面并没有突出的天赋，以现在的眼光看，报告中不免有多处纰漏，而且整个项目的文件管理也十分混乱，大家谨慎参考。

如果有任何问题，欢迎 pull requests，但我不一定会改​ :ghost:

## 包含实验

+ [塞曼效应]()
+ [光泵磁共振](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/光泵磁共振/lab_report)
+ [半导体泵浦固体激光调Q与光学二倍频](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/半导体泵浦固体激光调Q与光学二倍频/lab_report)
+ [实时高温电阻测量研究MgB2相变](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/实时高温电阻测量研究MgB2相变/lab_report)
+ [脉冲核磁共振与成像](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/脉冲核磁共振与成像/lab_report)
+ [硅的霍尔系数及电阻率的测量](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/硅的霍尔系数及电阻率的测量/lab_report)
+ [核磁共振](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/核磁共振/lab_report)

## 编译

本项目中所有实验报告都使用了来自 [CastleStar14654/PKUMpLtX](https://github.com/CastleStar14654/PKUMpLtX) 的模版（在近代物理实验网站上也有提供），在编译前请将 [`mpltx.cls`](https://github.com/Shocked-Pikachu/ModernPhysicsLab/blob/main/template/mpltx.cls) 文件放入tex文件所在的目录下。

编译时请使用 XeLaTeX。

## 致谢

本项目大量参考 [bryango/PKUModernPhyLabReport_LaTeX](https://github.com/bryango/PKUModernPhyLabReport_LaTeX) 和 [chaserhkj/ModPhyLab](https://github.com/chaserhkj/ModPhyLab)，在此致以真诚的感谢 :rose:！

## 其他说明

报告中的大多数图像都是使用Python的matplotlib.pyplot库绘制，但由于程序在读取文件的时候涉及到文件路径，并且考虑到绘图工作并不是写实验报告时的主要工作，本仓库不包含实验数据和使用数据绘图的Python脚本。

等之后修完近代物理实验（II）（当然也可能选修其他的实验课程），这个项目还会进行更新，当然更新速度取决于本人的摆烂程度（x）

## License

Works in this repository is licensed under CC0, which is very similar to the Unlicense.

In other words, you may copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.