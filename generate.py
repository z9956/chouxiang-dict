from PIL import Image, ImageDraw, ImageFont
import os

LETTERS = '典孝急乐麻批蚌盒赢输对退寄创绝谔鼠兔神躺卷润狂图了献忠支爆死歇反共中美日党雅俗佛草逼冲浪汗爹包子习毛偷傻善编恰哈拉摇晶哥粪钓灵软硬抄爬原马唉资本我爷'

FONT = ImageFont.truetype('三极隶书简体.ttf', 650)

os.makedirs('output', exist_ok=True)

for letter in LETTERS:
    image = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))

    draw = ImageDraw.Draw(image)
    draw.ellipse((10, 10, 990, 990), outline='black', fill='white', width=30)
    draw.ellipse((80, 80, 920, 920), outline='black', fill='white', width=60)
    draw.text((500, 410), letter, fill='black', anchor='mm', font=FONT)

    image.resize((100, 100), Image.LANCZOS).save(f'output/{letter}.png')