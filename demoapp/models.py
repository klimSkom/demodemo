from django.db import models
from django.contrib.auth.models import User
# Create your models here.


type_choices = (
("Аудитория", "Аудитория"),
("Коворкинг", "Коворкинг"),
("Кинозал", "Кинозал"),
)
payment_choices = (
("СБП", "СБП"),
("Наличными при встрече", "Наличными при встрече"),

)
status_choices = (
("Новая", "Новая"),
("Мероприятие назначено", "Мероприятие назначено"),
("Завершено", "Завершено"),
)
class Zayavka(models.Model):
    type = models.CharField(max_length=30, verbose_name="Тип аудитории", choices=type_choices)
    datetime = models.DateTimeField(verbose_name="Дата и время записи")
    payment = models.CharField(max_length=30, verbose_name="Способ оплаты", choices=payment_choices)
    status = models.CharField(max_length=30, verbose_name="Статус заявки", default="Новая", choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, verbose_name="Пользователь")

    def __str__(self):
        return F"{self.type} | {self.status}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"