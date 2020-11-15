from django.db import models


class Tag(models.Model):
    """ファイルのタグ"""
    text = models.TextField('テキスト')

    def __str__(self):
        """タグのテキストを返す"""
        return self.text


class UploadFile(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.FileField('ファイル')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url
