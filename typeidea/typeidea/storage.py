# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: storage
@time:2023/5/23
@Author:majiaqin 170479
@Desc:实现文件存储
'''
from io import BytesIO

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image, ImageDraw, ImageFont

class WatermarkStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        # 处理逻辑
        if 'image' in content.content_type:
            # 加水印
            image = self.watermark_with_text(content, 'the5fire.com', 'red')
            content = self.convert_image_to_file(image, name)
        return super(WatermarkStorage, self).save(name, content, max_length=max_length)

    def convert_image_to_file(self, image, name):
        temp = BytesIO()
        image.save(temp, format='PNG')
        file_size = temp.tell()
        return InMemoryUploadedFile(temp, None, name, 'image/png', file_size, None)

    def watermark_with_text(self, file_obj, text, color, fontfamily=None):
        image = Image.open(file_obj).convert('RGBA')
        draw = ImageDraw.Draw(image)
        width, height = image.size
        margin = 10
        if fontfamily:
            font = ImageFont.truetype(fontfamily, int(height/20))
        else:
            font = None

        textWidth, textHeight = draw.textsize(text, font)
        # 计算横轴位置
        x = (width-textWidth-margin)/2
        # 计算纵轴位置
        y = height-textHeight-margin
        draw.text((x, y), text, color, font)
        return image