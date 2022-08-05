## Coin and circle counters for python using OpenCV
![](https://img.shields.io/badge/language-python-green.svg)  ![](https://img.shields.io/badge/Coin_Counter-v1.0.6-519dd9.svg) ![](https://img.shields.io/badge/dependency-opencv-orange.svg)

A program that detects the number of coins or circles in an image    
> 一个可以检测图片中硬币或者圆圈数量的程序
## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background
When studying CV basic operations, I want to use these skills to detect some thing, and that's why I made this proj                 
在学习计算机视觉基础操作的时候，我想利用这些技巧去检测一些东西，受到一些项目启发，做了这个项目来对图片或者实时视频中的硬币或圆形物体进行检测
## Install
Just **Download** and **Unzip** the repo!
## Usage
##### 1.Find coins in an image statically
```
python3 coin_counter_test_to_find_good_parameter.py
```
```mermaid
graph LR
    start[start] --> load[load image]
    subgraph gray
    load -- Convert to gray scale --> grayscale[Gray Image]
    end
    grayscale -- Apply median blur --> mblur[Image Blurred]
    subgraph blur
    mblur -- Apply gaussian blur --> gblur[Image Blurred]
    end
    subgraph edge detection
    gblur -- Canny Edge Detection --> cEdge[Edges]
    end
    subgraph draw contours
    cEdge -- Find contours --> contours[Contours]
    end
    contours -- Draw and Count the contours --> stop[stop]
    
```
<!--load image -> convert to grey scale -> apply median blur -> apply gaussian blur -> apply canny edge detection -> find contours -> draw contours -> count the number of contours -> thus, count the number of coins.<br><br>-->


##### 2.Find circles from video instantly
```
python3 Find_Circles_And_Say.py
```
examples:

<img src="./find_circles_ex/find_circles_test_1.png" width="600"  alt="test_1"/>
<img src="./find_circles_ex/find_circles_test_2.png" width="600"  alt="test_2"/>

## Related Efforts
## Maintainers
[@DenryDu](https://github.com/DenryDu)
## Contributors
## License

***
If you find this useful, please star it! :)
Denry Du 2019
