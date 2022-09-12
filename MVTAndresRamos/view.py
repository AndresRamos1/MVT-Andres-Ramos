from django.http import HttpResponse
from django.template import loader
from familiares.models import familia

def inicio(request):
    return HttpResponse(f'Hola soy una base de datos de familiares :D')

def familiar(self):
    data = {'nombremadre':'Josefina De La Hoz', 'edadmadre':'65','fechamadre':'18-03-1957',
    'nombrehermano':'Jorge Ramos', 'edadhermano':'34','fechahermano':'30-04-1988',
    'nombreprimo':'Andres Ramos', 'edadprimo':'30','fechaprimo':'04-05-1992',
    }
    planilla = loader.get_template('template.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def fam(self):
    familiar1 = familia(nombre="Josefina De La Hoz", edad="65",fecha="1957-03-18")
    familiar1.save()
    
    documento = f'nombre: {familiar1.nombre} edad: {familiar1.edad} fecha: {familiar1.fecha}' 
    return HttpResponse(documento)

