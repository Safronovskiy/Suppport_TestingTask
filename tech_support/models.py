from django.db import models
from django.contrib.auth.models import User


class ClientModel(models.Model):
    """       """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    client_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('client_name', )

    def __str__(self):
        return f'{self.client_name}'


class SpecialistsModel(models.Model):
    """       """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    specialist_first_name = models.CharField('Имя', max_length=250)
    specialist_last_name = models.CharField('Фамилия', max_length=250)

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
        ordering = ('specialist_last_name', )

    def __str__(self):
        return f'{self.user} / {self.specialist_last_name}'



class ServiceRequestModel(models.Model):
    """       """
    issue_category = models.ForeignKey('ServiceRequestCategoryModel', on_delete=models.SET_NULL, null=True,
                                       verbose_name='Категория')
    issue_customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик/Клиент')
    issue_title = models.CharField(max_length=250, unique=True, verbose_name='Заголовок')
    issue_description = models.TextField('Описание проблемы', null=True)
    issue_occurence_date = models.DateTimeField('Дата возникновения проблемы', null=True)
    issue_date_created = models.DateTimeField('Дата создания сообщения', auto_now_add=True)
    issue_executor = models.ForeignKey(SpecialistsModel, on_delete=models.SET_NULL, blank=True, null=True)

    is_new = models.BooleanField('Статус заявки-"новая":', default=True)
    is_processed = models.BooleanField('Статус заявки-"обрабатывается":', default=False)
    is_completed = models.BooleanField('Статус заявки-"завершена":', default=False)
    is_in_archive = models.BooleanField('Статус заявки-"в архиве":', default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('issue_date_created', )

    def __str__(self):
        return f'{self.issue_title[:20]} / {self.issue_date_created}'



class IssueSolutionModel(models.Model):
    """       """
    issue = models.ForeignKey(ServiceRequestModel, on_delete=models.CASCADE, verbose_name='')
    solution_description = models.TextField('Описание решения', null=True)
    solution_date = models.DateTimeField('Время')
    solution_executor = models.ForeignKey(SpecialistsModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'
        ordering = ('issue', )

    def __str__(self):
        return f'{self.issue} / {self.solution_description}'


class ServiceRequestCategoryModel(models.Model):
    """       """
    category_name = models.CharField('Название категории/раздела', max_length=250, unique=True)
    category_description = models.TextField('Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name', )

    def __str__(self):
        return f'{self.category_name}'








