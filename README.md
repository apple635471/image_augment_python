# image_augment_python
## required packages:
* opencv
```shell
$ pip install opencv-python
```
* scikit-image
```shell
$ pip install -U scikit-image
```
* imgaug
```shell
$ pip install imgaug
```
### usage:
```shell
Usage: imageaugment.py [OPTIONS]

Options:
  -h, --help            show this help message and exit
  -s SOURCEPATH, --source=SOURCEPATH
                        The source path where your images in, will be
                        processed later. default path is "./".
  -d DESTINATIONPATH, --dest=DESTINATIONPATH
                        The destination path where you want to store the
                        images after processing. default path is
                        "./after_process/".
```
### example:
* default
* custom
```shell
$ tree
.
└── data
    ├── 0_0.jpg
    ├── 0_10.jpg
    ├── 0_11.jpg
    ├── 0_1.jpg
    ├── 0_2.jpg
    ├── 0_3.jpg
    ├── 0_4.jpg
    ├── 0_5.jpg
    ├── 0_6.jpg
    ├── 0_7.jpg
    ├── 0_8.jpg
    └── 0_9.jpg
$ python imageaugment.py -s ./data/ -d ./copy_data/
0_2.jpg has been completed
0_5.jpg has been completed
0_1.jpg has been completed
0_11.jpg has been completed
0_0.jpg has been completed
0_8.jpg has been completed
0_10.jpg has been completed
0_7.jpg has been completed
0_4.jpg has been completed
0_9.jpg has been completed
0_6.jpg has been completed
0_3.jpg has been completed
$ tree
.
├── copy_data
│   ├── copy_0_0.jpg
│   ├── copy_0_10.jpg
│   ├── copy_0_11.jpg
│   ├── copy_0_1.jpg
│   ├── copy_0_2.jpg
│   ├── copy_0_3.jpg
│   ├── copy_0_4.jpg
│   ├── copy_0_5.jpg
│   ├── copy_0_6.jpg
│   ├── copy_0_7.jpg
│   ├── copy_0_8.jpg
│   └── copy_0_9.jpg
└── data
    ├── 0_0.jpg
    ├── 0_10.jpg
    ├── 0_11.jpg
    ├── 0_1.jpg
    ├── 0_2.jpg
    ├── 0_3.jpg
    ├── 0_4.jpg
    ├── 0_5.jpg
    ├── 0_6.jpg
    ├── 0_7.jpg
    ├── 0_8.jpg
    └── 0_9.jpg
```
![0_0.jpg](https://github.com/apple635471/image_augment_python/blob/master/data/0_0.jpg)
![copy_0_0.jpg]()
