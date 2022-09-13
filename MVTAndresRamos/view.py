from django.http import HttpResponse
from django.template import loader
from familiares.models import familia

def inicio(request):
    return HttpResponse(f'Hola soy una base de datos de familiares :D')

# def familiar(self):
#     data = {'nombremadre':'Josefina De La Hoz', 'edadmadre':'65','fechamadre':'18-03-1957',
#     'nombrehermano':'Jorge Ramos', 'edadhermano':'34','fechahermano':'30-04-1988',
#     'nombreprimo':'Andres Ramos', 'edadprimo':'30','fechaprimo':'04-05-1992',
#     }
#     planilla = loader.get_template('template.html')
#     documento = planilla.render(data)
#     return HttpResponse(documento)

def familiar(self):
    familiar1 = familia(nombre="Josefina De La Hoz", edad="65",fecha="1957-03-18")
    familiar1.save()

    familiar2 = familia(nombre="Jorge Ramos", edad="34",fecha="1988-04-30")
    familiar2.save()

    familiar3 = familia(nombre="Andres Ramos", edad="30",fecha="1992-05-04")
    familiar3.save()
    data = {'response':[{'nombre':familiar1.nombre, 'edad':familiar1.edad, 'fecha':familiar1.fecha},
    {'nombre':familiar2.nombre, 'edad':familiar2.edad, 'fecha':familiar2.fecha},
    {'nombre':familiar3.nombre, 'edad':familiar3.edad, 'fecha':familiar3.fecha}]}
    planilla = loader.get_template('template.html')
    documento = planilla.render(data)
    #documento = f'nombre: {familiar1.nombre} edad: {familiar1.edad} fecha: {familiar1.fecha}, nombre: {familiar2.nombre} edad: {familiar2.edad} fecha: {familiar2.fecha}, nombre: {familiar3.nombre} edad: {familiar3.edad} fecha: {familiar3.fecha}'
    return HttpResponse(documento)

