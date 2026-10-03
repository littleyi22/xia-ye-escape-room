# -*- coding: utf-8 -*-
"""星空少年去背圖：透明底，戴睡帽、提星星燈的少年"""
from PIL import Image, ImageDraw
import random, math
W, H = 360, 480
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
random.seed(7)
# 小星星灑在周圍（避開中央人物區）
for _ in range(60):
    x = random.randint(5, W - 5)
    y = random.randint(5, H - 5)
    if 90 < x < 270 and 90 < y < 430:
        continue
    r = random.choice([1, 1, 2, 2, 3])
    c = random.choice([(255, 255, 255, 230), (255, 233, 163, 230), (255, 215, 110, 230)])
    d.ellipse([x - r, y - r, x + r, y + r], fill=c)

cx = W // 2
SKIN = (255, 214, 170, 255)
HAIR = (45, 35, 40, 255)
PAJ = (38, 70, 140, 255)      # 睡衣藍
PAJ_D = (28, 52, 110, 255)
SHOE = (120, 72, 40, 255)

# 腳
d.ellipse([cx - 62, 400, cx - 18, 430], fill=SHOE)
d.ellipse([cx + 18, 400, cx + 62, 430], fill=SHOE)
# 腿（睡褲）
d.rounded_rectangle([cx - 58, 330, cx - 12, 408], radius=18, fill=PAJ_D)
d.rounded_rectangle([cx + 12, 330, cx + 58, 408], radius=18, fill=PAJ_D)
# 身體（睡衣）
d.rounded_rectangle([cx - 70, 220, cx + 70, 340], radius=34, fill=PAJ)
# 睡衣星星紋
for sx, sy in [(cx - 40, 260), (cx + 35, 250), (cx - 5, 300), (cx - 45, 315), (cx + 45, 315)]:
    d.ellipse([sx - 4, sy - 4, sx + 4, sy + 4], fill=(255, 233, 163, 255))
# 左手下垂
d.rounded_rectangle([cx - 96, 240, cx - 66, 320], radius=14, fill=PAJ_D)
d.ellipse([cx - 94, 315, cx - 68, 340], fill=SKIN)
# 右手高舉拿星星棒
d.line([cx + 70, 260, cx + 128, 170], fill=SKIN, width=22)
d.ellipse([cx + 114, 152, cx + 142, 180], fill=SKIN)
d.line([cx + 128, 166, cx + 128, 120], fill=(150, 110, 60, 255), width=7)
# 星星光暈
for rr, alpha in [(46, 60), (34, 90), (24, 130)]:
    d.ellipse([cx + 128 - rr, 92 - rr, cx + 128 + rr, 92 + rr],
              fill=(255, 215, 110, alpha))
# 五角星
def star(cxx, cyy, R, rot=-90):
    pts = []
    for i in range(10):
        r = R if i % 2 == 0 else R * 0.45
        a = math.radians(rot + i * 36)
        pts.append((cxx + r * math.cos(a), cyy + r * math.sin(a)))
    return pts
d.polygon(star(cx + 128, 92, 30), fill=(255, 200, 60, 255))
d.polygon(star(cx + 128, 92, 14), fill=(255, 240, 180, 255))
# 脖子＋頭
d.rectangle([cx - 20, 190, cx + 20, 228], fill=SKIN)
d.ellipse([cx - 58, 100, cx + 58, 216], fill=SKIN)
# 頭髮（兩側＋瀏海）
d.arc([cx - 60, 98, cx + 60, 218], start=180, end=360, fill=HAIR, width=26)
d.ellipse([cx - 62, 130, cx - 28, 170], fill=HAIR)
d.ellipse([cx + 28, 130, cx + 62, 170], fill=HAIR)
# 睡帽：藍色三角帽＋星＋絨球
d.polygon([(cx - 52, 116), (cx + 52, 116), (cx + 96, 30)], fill=(43, 90, 180, 255))
d.ellipse([cx + 78, 12, cx + 114, 48], fill=(255, 255, 255, 255))
d.ellipse([cx - 30, 88, cx - 18, 100], fill=(255, 233, 163, 255))
d.ellipse([cx + 8, 80, cx + 20, 92], fill=(255, 233, 163, 255))
# 閉眼微笑（幸福）
d.arc([cx - 38, 150, cx - 10, 172], start=10, end=170, fill=(60, 40, 40, 255), width=4)
d.arc([cx + 10, 150, cx + 38, 172], start=10, end=170, fill=(60, 40, 40, 255), width=4)
d.ellipse([cx - 48, 176, cx - 30, 190], fill=(255, 150, 150, 200))
d.ellipse([cx + 30, 176, cx + 48, 190], fill=(255, 150, 150, 200))
d.arc([cx - 14, 182, cx + 14, 202], start=15, end=165, fill=(150, 70, 70, 255), width=4)
out = "escape-xiaye-full/assets/img/character.png"
img.save(out)
print("saved", out, img.size)
