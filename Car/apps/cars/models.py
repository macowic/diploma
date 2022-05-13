from typing import Any
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    IntegerField,
    TextField,
    ImageField,
    CASCADE
)

from abstracts.models import AbstractDateTime

class Category(Model):
    
    category = CharField(max_length=50,verbose_name='категория')
    
    def __str__(self) -> str:
        return f'Категория: {self.category}'
    
    class Meta:
        
        ordering = (
            '-category',
        )
        
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        
class Mark(Model):
    
    mark_name = CharField(max_length=40,verbose_name='марка')
    
    def __str__(self) -> str:
        return f'Марка: {self.mark_name}'
    
    class Meta:
        
        ordering = (
            '-mark_name',
        )
        
        verbose_name_plural = 'марки'
        verbose_name = 'марка'
        
class Car(AbstractDateTime):
    
    mdfied = 'modified'
    non_mdfied = 'non_modified'
    
    MOTOR_CHOICES = (
        (mdfied, 'Модифицированный'),
        (non_mdfied, 'Не модифицированный'),
    )
    
    mark = ForeignKey(Mark,on_delete=CASCADE, verbose_name='марка машины')
    model = CharField(max_length=20,verbose_name='модель машины')
    category = ForeignKey(Category,on_delete=CASCADE,verbose_name='категория')
    speed = IntegerField(verbose_name='скорость машины')
    motor = CharField(max_length=40, choices=MOTOR_CHOICES,verbose_name='состояние мотора')
    
    def __str__(self) -> str:
        return f'Машина: {self.mark}|{self.model}'
    
    class Meta:
        
        ordering = (
            '-mark',
        )
        verbose_name_plural = 'машины'
        verbose_name = 'машина'