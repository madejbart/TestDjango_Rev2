from django.shortcuts import render, redirect


from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .forms import VariableForm, DeviceForm
from .models import Value, Var, Device, ModbusDevice


# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'testapp/index.html')

def devices(request):
    """Show all devices """
    devices = Device.objects.order_by('date')
    context = {'devices': devices}
    return render(request, 'testapp/devices.html', context)

def device(request, dev_id):
    """show a single device and all its variables"""
    device = Device.objects.get(id = dev_id)
    variables = device.var_set.order_by('user')
    context = {'device': device, 'variables': variables}
    return render(request, 'testapp/dev.html', context)

class ValueListView(ListView):
    template_name = "testapp/values.html"
    context_object_name = "values"
    model = Value
    def get_last(self):
        return Question.objects.order_by('date_created')[:5]



class VariablesListView(ListView):
    template_name = "testapp/variables.html"
    context_object_name = "variables"
    model = Var


class EditVariableView(UpdateView):
    template_name = "testapp/update_variable.html"
    success_url = reverse_lazy("testapp:variables")
    form_class = VariableForm
    model = Var

class NewVariableView(CreateView):
    template_name = "testapp/new_variable.html"
    success_url = reverse_lazy("testapp:variables")
    form_class = VariableForm
    model = Var

class NewDevView(CreateView):
    template_name = "testapp/new_dev.html"
    success_url = reverse_lazy("testapp:devices")
    form_class = DeviceForm
    model = Device

class DelDeviceView(DeleteView):
    template_name = "testapp/delete.html"
    success_url = reverse_lazy("testapp:devices")
    form_class = DeviceForm
    model = Device

class DelVariableView(DeleteView):
    template_name = "testapp/delete.html"
    success_url = reverse_lazy("testapp:variables")
    form_class = VariableForm
    model = Var


class ModbusDeviceCreateView(CreateView):
    model = ModbusDevice
    success_url = reverse_lazy("uzupelnic")
    template_name =  "testapp/new_modbus_device.html"
    fields = "__all__"