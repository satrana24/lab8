from PIL import Image, ImageFont, ImageDraw


def first():
    name = 'new_year2.jpg'
    with Image.open(name) as img:
        img.load()

    img.show()

    cropped_img = img.crop((153, 110, 640, 450))
    cropped_img.save("cropped_postcard_new_year.jpg")
    cropped_img.show()


def second():
    holidays = {1: 'happy_birthday.jpg', 2: '8_march.jpg', 3: 'new_year.jpg', 4: '23_february.jpg'}

    print('''Выберите праздник из списка, на тематику которого хотите получить открытку.
1 -- День рождение
2 -- Международный Женский день
3 -- Новый год
4 -- День Защитника Отечества''')
    choice = int(input('Введите цифру: '))

    postcard = holidays[choice]
    with Image.open(postcard) as img:
        img.load()

    img.show()


def third():
    name = 'postcard.jpg'
    with Image.open(name) as img:
        img.load()

    text = str(input('Введите имя человека, которого хотите поздравить: '))

    font = ImageFont.truetype('arial.ttf', 25)
    drawer = ImageDraw.Draw(img)
    drawer.text((img.width // 2 - 90, 70), f'{text}, поздравляю!', font=font, stroke_width=1, fill=(255, 105, 180))

    img.save('postcard_' + text + '.png')
    img.show()
