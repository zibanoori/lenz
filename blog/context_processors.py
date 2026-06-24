from .models import Category


def site_categories(request):
    categories = Category.objects.all()

    return {
        'categories': categories
    }