from django.db import models


class TeaType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Tea(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(default=5000, max_digits=10, decimal_places=2)
    type = models.ForeignKey('TeaType', on_delete=models.CASCADE)
    image = models.FileField(default='tea.jpg', upload_to='tea_pics')

    def __str__(self):
        return f'{self.name}'
