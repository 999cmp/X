from django.db import models
from datetime import datetime

from django.db import models
import uuid


class Tarife(models.Model):
    title: str = models.CharField('title', max_length=255, null=False)
    descriptions: str = models.TextField('descriptions')
    price: float = models.FloatField('price', default=0.0)

    class Meta:
        db_table = 'Tarife'


class Users(models.Model):
    name: str = models.CharField(max_length=255, null=False)
    surname: str = models.CharField(max_length=255, null=False)
    login: str = models.CharField(max_length=255, null=False, unique=True)
    password: str = models.CharField(max_length=255, null=False)
    email: str = models.CharField(max_length=255, null=False, unique=True)
    created_at: datetime = models.DateField(default=datetime.now)
    banned: bool = models.BooleanField(default=False)
    tarife_id = models.ForeignKey(Tarife, on_delete=models.PROTECT)
    token = models.UUIDField(default=uuid.uuid4, editable=False)

    def generate_token(self):
        self.token = uuid.uuid4()

    def check_token(self, token):
        return str(self.token) == token

    class Meta:
        db_table = 'Users'


class Transactions(models.Model):
    uuid: str = models.UUIDField('uuid', default=uuid.uuid4())
    user_id: str = models.ForeignKey(Users, on_delete=models.PROTECT)
    parametrs: dict = models.JSONField('parametrs')
    created: datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'Transactions'


class Task(models.Model):
    title = models.CharField('title', max_length=255, null=False)
    descriptions = models.TextField('descriptions')
    time_added = models.DateTimeField(default=datetime.now())
    time_finish = models.DateTimeField(default=datetime.now())
    appointed = models.ForeignKey(Users, related_name='appointed_tasks', on_delete=models.PROTECT, verbose_name='appointed')
    executor = models.ForeignKey(Users, related_name='executor_tasks', on_delete=models.PROTECT, verbose_name='executor')
    status = models.CharField(max_length=55)
    token = models.UUIDField(default=uuid.uuid4, editable=False)

    def generate_token(self):
        self.token = uuid.uuid4()

    def check_token(self, token):
        return str(self.token) == token

    class Meta:
        db_table = 'Task'

class CommentTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    text: str = models.TextField()
    user_token = models.ForeignKey(Users, on_delete=models.PROTECT)
    created = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'CommentTask'
