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
### example1:
* default
```shell
$ python imageaugment.py
```
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
<img src="https://github.com/apple635471/image_augment_python/blob/master/data/0_0.jpg" width="256" height="256"><img src="https://github.com/apple635471/image_augment_python/blob/master/copy_data/copy_0_0.jpg" width="256" height="256">

### example2

* Recursively do image augmentation on all image file(.jpg) under the current directory.
* (Notice !) It will create new directory to store all file and directory created by imageaugment.py

```shell
$ cd image_augment_python/data_2
$ DIRS=`ls -mR * | sed -n 's/://p'`; for DIR in $DIRS; do echo ${PWD}/${DIR}; done

/home/username/image_augment_python/data2/data_2
/home/username/image_augment_python/data2/data_2/data_2a
/home/username/image_augment_python/data2/data_2/data_2b
/home/username/image_augment_python/data2/data_2/data_2c
/home/username/image_augment_python/data2/data_3
/home/username/image_augment_python/data2/data_3/data_3a
/home/username/image_augment_python/data2/data_3/data_3b
/home/username/image_augment_python/data2/data_3/data_3c

$ cd ..
$ cd data2; DIRS=`ls -mR * | sed -n 's/://p'`; for DIR in $DIRS; do mkdir -p ../copy_data2/; python ../imageaugment.py -s ${PWD}/${DIR} -d ../copy_data2/${DIR}; done

.
.
.
.
.
0_7.jpg has been completed
0_4.jpg has been completed
0_9.jpg has been completed
0_6.jpg has been completed
0_3.jpg has been completed

$ cd ..
$ DIRS=`ls -mR * | sed -n 's/://p'`; for DIR in $DIRS; do echo ${PWD}/${DIR}; done

/home/username/image_augment_python/copy_data2
/home/username/image_augment_python/copy_data2/data_2
/home/username/image_augment_python/copy_data2/data_2/data_2a
/home/username/image_augment_python/copy_data2/data_2/data_2b
/home/username/image_augment_python/copy_data2/data_2/data_2c
/home/username/image_augment_python/copy_data2/data_3
/home/username/image_augment_python/copy_data2/data_3/data_3a
/home/username/image_augment_python/copy_data2/data_3/data_3b
/home/username/image_augment_python/copy_data2/data_3/data_3c
/home/username/image_augment_python/data2/data_2
/home/username/image_augment_python/data2/data_2/data_2a
/home/username/image_augment_python/data2/data_2/data_2b
/home/username/image_augment_python/data2/data_2/data_2c
/home/username/image_augment_python/data2/data_3
/home/username/image_augment_python/data2/data_3/data_3a
/home/username/image_augment_python/data2/data_3/data_3b
/home/username/image_augment_python/data2/data_3/data_3c
```
### example3
* imgaug library support multiple images augment
* (Notice !) each images must have same size (ex: totally 512x512)
* 
```python
    ## load multiple image
    images = np.empty((len(image_list),512,512,3))
    for i in range(0, len(image_list)):
        images[i] = cv2.imread(options.sourcepath+"/"+image_list[i], cv2.IMREAD_COLOR)
    print(images.shape)
    images = seq.augment_images(images)
    for i in range(0, len(image_list)):
        cv2.imwrite(options.destinationpath+"/"+image_list[i], images[i])
    print("All images under "+options.sourcepath+" have been completed--------------")
```
