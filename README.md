# py-srcset
Python script for reformatting images and generating srcset strings

## Usage

Clone the project to a directory of your choice, enter it and run the following to install dependencies.

```
pip install Pillow avif-pillow-plugin
```

Open py-srcset.py and modify the values in the file.
```
sizes
```
This array holds the sizes you want for output images. Currently it only applies to the width of images.

```
source
```
This is the path to your input image.
Output images will be created in the directory this script is executed from in the following layout
```
py-srcset
  - image_name
    -webp
    -png
    -jpeg
    -avif
```

```
cdnURL
```
This is appended to the location and name of each file generated and output to the console. Copy the string from the console and use as the value for srcset in your html file. I chose to do it this way as I wanted to append my CDN url to each item.
As an example, if your CDN is ```https://www.cdn.com/folder/``` then your output string for WebP images would look like ```'https://www.cdn.com/folder/image/webp/image-100.webp 100w, https://www.cdn.com/folder/image/webp/image-200.webp 200w'```.

```
webp_quality = 70
jpeg_quality = 90
avif_quality = 50
png_quality = 90
```
These are the quality settings for each format in use.

```
usesAlpha = False
```
Whether or not to use the alpha channel. If true then PNG files be generated as the fallback image format, if false then JPEGs.

Currently there are no options for running through the terminal only however I may update to include that in the future.

## Benchmark
I used the following Unsplash image for testing the script, the original image is 3992 x 2242 and weighs in at 2073 KB.

![test](https://user-images.githubusercontent.com/3427530/236096510-6a24ec96-1270-490b-bd3e-84209f0fd131.jpg)
Photo by <a href="https://unsplash.com/de/@burntime?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alex Kulikov</a> on <a href="https://unsplash.com/photos/vBpefozS0As?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

The table below has the compression results for different sizes, formats and quality levels.

| Width | AVIF 50% (KB) | WebP 70% (KB) | JPEG 90% (KB) | PNG 90% (KB) |
|-------|---------------|---------------|---------------|--------------|
| 100   | 5             | 2             | 3             | 15           |
| 200   | 7             | 5             | 10            | 50           |
| 300   | 11            | 10            | 20            | 108          |
| 400   | 16            | 18            | 36            | 190          |
| 500   | 24            | 28            | 56            | 298          |
| 600   | 32            | 40            | 80            | 427          |
| 700   | 41            | 55            | 109           | 579          |
| 800   | 53            | 71            | 142           | 754          |
| 1000  | 85            | 116           | 226           | 1181         |
| 1200  | 123           | 167           | 324           | 1686         |
| 1600  | 210           | 292           | 567           | 2928         |
  
AVIF quality seems to be very stable when pushed to low compression rates. WebP, JPEG and PNG results could be improved by fine tuning the quality values for them, however this is dependant on the type of image you are compressing and how much detail you need to preserve.
