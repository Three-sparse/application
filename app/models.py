from django.db import models


class UploadFile(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.FileField('ファイル')

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url