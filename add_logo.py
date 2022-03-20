#!/usr/bin/env python3
import sys
import os 

try:
    from PIL import Image
except ImportError:
    print("Please install Pillow from: https://pypi.python.org/pypi/Pillow/3.0.0")
    sys.exit(1)


def run(a,b,c,d):
    print(a,b,c,d)
    inimage, logo, outimage, size = a, b, c , d
    add_logo(inimage, logo, outimage, size)

    return 0

def for_all():
    os.makedirs("withlogo", exist_ok = True)
    os.makedirs("image", exist_ok = True)

    logo_file = "logo.png"

    for filename in os.listdir("./image"):
        if not (filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".JPG")) or filename == logo_file:
            continue
        run("./image/"+filename, logo_file,"./withlogo/"+filename,"size.png" )

def add_logo(mfname, lfname, outfname, sizename):

    mimage = Image.open(mfname)
    limage = Image.open(lfname)
    sizeimage = Image.open(sizename)


    # resize logo
    wsize = int(min(mimage.size[0], mimage.size[1]) * 0.25)
    wpercent = (wsize / float(limage.size[0]))
    hsize = int((float(limage.size[1]) * float(wpercent)))
    simage = limage.resize((wsize, hsize))

    # resize size badge
    wsize = int(min(mimage.size[0], mimage.size[1]) * 0.25)
    wpercent = (wsize / float(sizeimage.size[0]))
    hsize = int((float(sizeimage.size[1]) * float(wpercent)))
    resizeSizeimage = sizeimage.resize((wsize, hsize))

    mbox = mimage.getbbox()
    sbox = simage.getbbox()
    sizebox = resizeSizeimage.getbbox()
    # right bottom corner
    box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
    mimage.paste(simage, box)
    box = ( 0, mbox[3] - sizebox[3])
    mimage.paste(resizeSizeimage, box)

    mimage.save(outfname)

for_all()