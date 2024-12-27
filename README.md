# ModernPhysicsLab

Modern physics lab reports written in $\LaTeX$ (2023 fall & 2024 fall) @ School of Physics, Peking University

2023 秋 / 2024 秋 近代物理实验报告，北京大学物理学院

此项目记录了本人在近代物理实验（I）以及（II）这两门课程中撰写的所有实验报告。由于本人在写实验报告时经历了一些折磨，现也把曾经写过的东西向大家分享出来，以期待能稍微减少一些后人的痛苦。但本人在实验和撰写实验报告这方面并没有突出的天赋，以现在的眼光看，报告中不免有多处纰漏，而且整个项目的文件管理也十分混乱，大家谨慎参考。

如果有任何问题，欢迎 pull requests，但我不一定会改​ :ghost:

## 包含实验

+ [塞曼效应](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/塞曼效应)
+ [光泵磁共振](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/光泵磁共振)
+ [半导体泵浦固体激光调Q与光学二倍频](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/半导体泵浦固体激光调Q与光学二倍频)
+ [实时高温电阻测量研究MgB2相变](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/实时高温电阻测量研究MgB2相变)
+ [脉冲核磁共振与成像](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/脉冲核磁共振与成像)
+ [硅的霍尔系数及电阻率的测量](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/硅的霍尔系数及电阻率的测量)
+ [核磁共振](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/核磁共振)
+ [用传输式谐振腔观测铁磁共振](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/用传输式谐振腔观测铁磁共振)
+ [约瑟夫森效应](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/约瑟夫森效应)
+ [穆斯堡尔效应](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/穆斯堡尔效应)
+ [扫描隧穿显微镜](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/扫描隧穿显微镜)
+ [扫描电子显微镜](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/扫描电子显微镜)
+ [非线性热对流斑图](https://github.com/Shocked-Pikachu/ModernPhysicsLab/tree/main/非线性热对流斑图)

## 编译

本项目中所有实验报告都使用了来自 [CastleStar14654/PKUMpLtX](https://github.com/CastleStar14654/PKUMpLtX) 的模版（在近代物理实验网站上也有提供），在编译前请将 [`mpltx.cls`](https://github.com/Shocked-Pikachu/ModernPhysicsLab/blob/main/template/mpltx.cls) 文件放入tex文件所在的目录下。

编译时请使用 XeLaTeX，由于交叉引用的原因，需要连续两次编译才能正确编译出引用的链接。

## 致谢

本项目大量参考 [bryango/PKUModernPhyLabReport_LaTeX](https://github.com/bryango/PKUModernPhyLabReport_LaTeX) 和 [chaserhkj/ModPhyLab](https://github.com/chaserhkj/ModPhyLab)，在此致以真诚的感谢 :rose:！

## 其他说明

报告中的大多数图像都是使用 Python 的 `matplotlib.pyplot` 库绘制，但由于程序在读取文件的时候涉及到文件路径，并且考虑到绘图工作并不是写实验报告时的主要工作，本仓库不一定包含实验数据和使用数据绘图的 Python 脚本。

## 说在最后

本 repo 至此已经更新完毕，一年的时间转瞬即逝，我不知道如果没有这些实验报告，我对于近代物理实验的回忆还能够剩下多少。诚然，对于学院来说，培养学生的动手实验和写报告能力是十分重要的，但是不幸的是，这门课程最后呈现的效果可能和学院最初设想的目标相去甚远。我周围听到的，包括我自己感受到的，多是对于实验仪器老旧、实验题材过时的抱怨，以及对于一言难尽实验报告的口诛笔伐。也许在实验课的过程中有那么一两个瞬间让我能够感受到这个实验课能够带给我一些有价值的东西（如非线性热对流斑图实验），但是课程结束之后，回顾这段旅程，发现除了这短暂的瞬间，也没有什么值得回忆的事情了。

好在一切已经结束，至少看着这些实验报告，我心里还是有一点点成就感的。

## License

Works in this repository is licensed under CC0, which is very similar to the Unlicense.

In other words, you may copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.