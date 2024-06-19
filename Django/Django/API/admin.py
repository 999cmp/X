from django.contrib import admin
import API.models as models

admin.site.register(models.Task)
admin.site.register(models.Tarife)
admin.site.register(models.Transactions)
admin.site.register(models.Users)
admin.site.register(models.CommentTask)