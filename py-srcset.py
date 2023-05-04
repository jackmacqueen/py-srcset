from pathlib import Path
from PIL import Image
import pillow_avif

#Output sizes
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 1000, 1200, 1600]
#Input file
source = Path('your_image_location.png')
#This will be appended to the file names in the output string
cdnURL = 'https://www.your_cdn_url.com/'
#Quality settings
webp_quality = 70
jpeg_quality = 90
avif_quality = 50
png_quality = 90
#Whether or not image uses alpha channel, generates a png fallback if true or jpeg if false
usesAlpha = False

def convert_AVIF(source, sizes):

    #Creates directory for file outputs, by default {current_directory}/{image_name}/AVIF/
    save_dir = Path(f"{source.stem}", 'AVIF')
    save_dir.mkdir(parents=True, exist_ok=True)

    print('AVIF srcset string')


    #This will be the string you use as a srcset value, it will be printed to the console
    output_string = ''

    for size in sizes:

        #File destination and name, default {current_directory}/{image_name}/AVIF/{image_name}-{size}.AVIF
        destination= Path(f"{source.stem}\AVIF\{source.stem}" + "-" + str(size) + ".AVIF")

        image = Image.open(source)
        #Use thumbnail to preserve aspect ratio
        image.thumbnail((size, image.size[1]), Image.Resampling.LANCZOS)
        image.save(destination, format="AVIF", quality=avif_quality)

        #Construct output string
        if size == sizes[0]:
            output = f"'{cdnURL}{source.stem}/AVIF/{source.stem}-{str(size)}.AVIF {str(size)}w, "
            output_string += str(output)
        elif size == sizes[-1]:
            output = f"{cdnURL}{source.stem}/AVIF/{source.stem}-{str(size)}.AVIF {str(size)}w'"
            output_string += str(output)
        else:
            output = f"{cdnURL}{source.stem}/AVIF/{source.stem}-{str(size)}.AVIF {str(size)}w, "
            output_string += str(output)
    
    print(output_string)


def convert_webp(source, sizes):

    #Creates directory for file outputs, by default {current_directory}/{image_name}/webp/
    save_dir = Path(f"{source.stem}", 'webp')
    save_dir.mkdir(parents=True, exist_ok=True)

    print('WebP srcset string')

    #This will be the string you use as a srcset value, it will be printed to the console
    output_string = ''

    for size in sizes:

        #File destination and name, default {current_directory}/{image_name}/webp/{image_name}-{size}.webp
        destination= Path(f"{source.stem}\webp\{source.stem}" + "-" + str(size) + ".webp")

        image = Image.open(source)
        #Use thumbnail to preserve aspect ratio
        image.thumbnail((size, image.size[1]), Image.Resampling.LANCZOS)
        image.save(destination, format="webp", quality=webp_quality)

        #Construct output string
        if size == sizes[0]:
            output = f"'{cdnURL}{source.stem}/webp/{source.stem}-{str(size)}.webp {str(size)}w, "
            output_string += str(output)
        elif size == sizes[-1]:
            output = f"{cdnURL}{source.stem}/webp/{source.stem}-{str(size)}.webp {str(size)}w'"
            output_string += str(output)
        else:
            output = f"{cdnURL}{source.stem}/webp/{source.stem}-{str(size)}.webp {str(size)}w, "
            output_string += str(output)
    
    print(output_string)


def convert_jpeg(source, sizes):

    #Creates directory for file outputs, by default {current_directory}/{image_name}/jpeg/
    save_dir = Path(f"{source.stem}", 'jpeg')
    save_dir.mkdir(parents=True, exist_ok=True)

    print('JPEG srcset string')


    #This will be the string you use as a srcset value, it will be printed to the console
    output_string = ''

    for size in sizes:

        #File destination and name, default {current_directory}/{image_name}/jpeg/{image_name}-{size}.jpeg
        destination= Path(f"{source.stem}\jpeg\{source.stem}" + "-" + str(size) + ".jpeg")

        image = Image.open(source)
        #Use thumbnail to preserve aspect ratio
        image.thumbnail((size, image.size[1]), Image.Resampling.LANCZOS)
        image.save(destination, format="jpeg", quality=jpeg_quality)

        #Construct output string
        if size == sizes[0]:
            output = f"'{cdnURL}{source.stem}/jpeg/{source.stem}-{str(size)}.jpeg {str(size)}w, "
            output_string += str(output)
        elif size == sizes[-1]:
            output = f"{cdnURL}{source.stem}/jpeg/{source.stem}-{str(size)}.jpeg {str(size)}w'"
            output_string += str(output)
        else:
            output = f"{cdnURL}{source.stem}/jpeg/{source.stem}-{str(size)}.jpeg {str(size)}w, "
            output_string += str(output)
    
    print(output_string)

def convert_png(source, sizes):

    #Creates directory for file outputs, by default {current_directory}/{image_name}/png/
    save_dir = Path(f"{source.stem}", 'png')
    save_dir.mkdir(parents=True, exist_ok=True)

    print('PNG srcset string')


    #This will be the string you use as a srcset value, it will be printed to the console
    output_string = ''

    for size in sizes:

        #File destination and name, default {current_directory}/{image_name}/png/{image_name}-{size}.png
        destination= Path(f"{source.stem}\png\{source.stem}" + "-" + str(size) + ".png")

        image = Image.open(source)
        #Use thumbnail to preserve aspect ratio
        image.thumbnail((size, image.size[1]), Image.Resampling.LANCZOS)
        image.save(destination, format="png", quality=png_quality)

        #Construct output string
        if size == sizes[0]:
            output = f"'{cdnURL}{source.stem}/png/{source.stem}-{str(size)}.png {str(size)}w, "
            output_string += str(output)
        elif size == sizes[-1]:
            output = f"{cdnURL}{source.stem}/png/{source.stem}-{str(size)}.png {str(size)}w'"
            output_string += str(output)
        else:
            output = f"{cdnURL}{source.stem}/png/{source.stem}-{str(size)}.png {str(size)}w, "
            output_string += str(output)
    
    print(output_string)


if(usesAlpha):
    convert_AVIF(source, sizes)
    convert_webp(source, sizes)
    convert_png(source, sizes)
else:
    convert_AVIF(source, sizes)
    convert_webp(source, sizes)
    convert_jpeg(source, sizes)