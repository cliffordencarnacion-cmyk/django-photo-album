from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm


class AlbumAdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_staff or user.groups.filter(name='Album Administrator').exists()


class AlbumListView(ListView):
    model = Album
    template_name = 'albums/album_list.html'
    context_object_name = 'albums'
    paginate_by = 12


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album_detail.html'
    context_object_name = 'album'


class AlbumCreateView(AlbumAdminRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(AlbumAdminRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')


class AlbumDeleteView(AlbumAdminRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album-list')


class PhotoCreateView(AlbumAdminRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'albums/photo_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.album = Album.objects.get(pk=kwargs['album_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = self.album
        return context

    def form_valid(self, form):
        form.instance.album = self.album
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('album-detail', kwargs={'pk': self.album.pk})


class PhotoUpdateView(AlbumAdminRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'albums/photo_form.html'

    def get_success_url(self):
        return reverse('album-detail', kwargs={'pk': self.object.album.pk})


class PhotoDeleteView(AlbumAdminRequiredMixin, DeleteView):
    model = Photo
    template_name = 'albums/photo_confirm_delete.html'

    def get_success_url(self):
        return reverse('album-detail', kwargs={'pk': self.object.album.pk})
