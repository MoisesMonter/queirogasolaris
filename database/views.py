from django.views.generic import ListView
from .models import Kit
from django.core.paginator import Paginator
# Create your views here.


class KitListView(ListView):
    model = Kit
    template_name = 'kit_list.html'
    context_object_name = 'kits'
    paginate_by = 5  # Define a quantidade de itens por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kits = context['kits']
        paginator = Paginator(kits, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context