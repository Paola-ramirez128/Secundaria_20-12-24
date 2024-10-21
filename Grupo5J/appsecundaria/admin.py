from django.contrib import admin
from.models import AlumnoT,Frase

# Register your models here.
class ComentarioIntLine(admin.TabularInline):
    model=Frase
    extra=1

class AlumnoAdmin(admin.ModelAdmin):
    fields=["APaterno","AMaterno","Nombre","Fecha_nacimiento","Fecha_ingreso"]
    list_display=["APaterno","AMaterno","Nombre"]
    inlines=[ComentarioIntLine]

admin.site.register(AlumnoT,AlumnoAdmin)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    fields=["comentario","Alumno_fk"]
    list_display=["comentario"]

