# 7.1) Подготовьте любой графический файл для выполнения практической работы.
# Напишите программу, которая открывает и выводит этот файл на экран.
# Получите и выведите в консоль информацию о размере изображения, его формате, его цветовой модели.
def firsst():
    from PIL import Image
    image = Image.open('7lab_strawberry.jpg')
    image.show()
    print("image size:", image.size, "file format:", image.format, "color model:", image.mode)

#7.2) Напишите программу, которая создаёт уменьшенную в три раза копию изображения.
# Получите горизонтальный и вертикальный зеркальный образ изображения. Сохраните изображения в текущую папку под новым именем.
def second():
    from PIL import Image, ImageOps
    ch = int(input("how many times do you want to shrink the image? "))
    img_orig = Image.open("7lab_cat.jpg")
    resize1 = img_orig.width // ch
    resize2 = img_orig.height // ch
    resized_image = img_orig.resize((resize1, resize2))
    resized_image.save('7lab_cat_resized.jpg')
    def resflip():
        imageres = Image.open("7lab_cat_resized.jpg")
        img = ImageOps.flip(imageres)
        img.save('7lab_cat_res_vertical.png')
        img = ImageOps.mirror(imageres)
        img.save('7lab_cat_res_horizontal.png')
    def origflip():
        imageorig = Image.open("7lab_cat.jpg")
        img = ImageOps.flip(imageorig)
        img.save('7lab_cat_orig_vertical.png')
        img = ImageOps.mirror(imageorig)
        img.save('7lab_cat_orig_horizontal.png')
    flipch = input("do you want to flip resized image, original image or both? ").upper()
    if (flipch == "RESIZED" or flipch == "RESIZE"):
        resflip()
    elif flipch == "ORIGINAL":
        origflip()
    elif flipch == "BOTH":
        origflip(), resflip()
    else:
        print("you need to type 'resize' or 'original' or 'both'")

#7.3) Подготовьте 5 графических файлов с именами 1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg.
# Напишите программу, которая применит ко всем этим файлам сразу любой фильтр (кроме размытия, т.к. он рассматривался на лекции).
# Сохраните изображения в новую папку под новыми именами.
def third():
    from PIL import Image, ImageFilter
    for i in range(1, 6):
        orig = Image.open(f"7lab_{i}.jpg")
        filt = orig.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 12, -1, -1, -1, -1), 1, 0))
        filt.save(f'D:\\newphotos\\7lab_filter{i}.jpg')

#7.4) Напишите программу, которая добавляет на изображение водяной знак. Можно тоже применять сразу к нескольким изображениям.
def fou2():
    from PIL import Image
    for i in range(1, 6):
        img = Image.open(f"7lab_{i}.jpg")
        watermark = Image.open('7lab_watermark.png')
        img_width, img_height = img.size
        watermark_width, watermark_height = watermark.size
        position = ((img_width - watermark_width) // 2, (img_height - watermark_height) // 2)
        img.paste(watermark, position, watermark)
        img.save(f'7lab_markedphoto{i}.png')

firsst(), second(), fou2()