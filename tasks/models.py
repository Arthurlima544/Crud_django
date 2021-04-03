from django.db import models

""" modelo de tarefas... uma tarefa possue titulo , informação se está completa e a dtata que foi emitida a task """
""" title, complete e data são fields do model -> mapeados para os fields do banco de dados """

class Task(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    info = models.CharField(max_length=100)
    """ método para devolver uma string """
    def __str__(self):
        return self.title
