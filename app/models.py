from django.db import models


class Tag(models.Model):
    """ファイルのタグ"""
    text = models.TextField('テキスト', unique=True)

    def __str__(self):
        """タグのテキストを返す"""
        return self.text


class UploadFile(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.FileField('ファイル')

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url
