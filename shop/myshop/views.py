from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm


def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(count__gt=0)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    return render(request, 'myshop/products_list.html', 
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  }
                  )

#myshop/product_detail.html

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, count__gt=0)
    cart_product_form = CartAddProductForm()
    return render(request, 'myshop/product_detail.html', {'product': product,
                                                          'cart_product_form': cart_product_form,
                                                          })
