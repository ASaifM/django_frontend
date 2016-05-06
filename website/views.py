from django.shortcuts import redirect, render, get_object_or_404
from .forms import IngredientForm
from .models import Ingredient
# Create your views here.

def base(request):
	if request.method == "POST":
		form = IngredientForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('req_ing', pk=post.pk)
	else:
		form = IngredientForm()
		return render(request, 'website/base.html', {'form': form})

def req_ing (request, pk):
	post = get_object_or_404(Ingredient, pk=pk)
	return render(request, 'website/req_ing.html', {'post': post})
