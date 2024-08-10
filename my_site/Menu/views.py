from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category,MealTime
from .form import ItemForm
from django.views import View
# Create your views here.
def food(request):
    meal_times = MealTime.objects.filter(is_drink=False)
    return render(request,'Menu/food.html',{
        'meal_times':meal_times
    })
def drink(request):
    drink_item = Item.objects.filter(category__is_drink = True)
    drink_menu = {}
    meal_times = MealTime.objects.filter(is_drink = True)
    for meal_time in meal_times:
        drink_menu[meal_time.name] = drink_item.filter(meal_time=meal_time)
    print(drink_menu)
    return render(request,'Menu/drink.html',{
        'meal_times':meal_times,
        'drink_menu':drink_menu
    })
def foodDetail(request, slug):
    # Lấy MealTime dựa trên slug. Nếu không tìm thấy, trả về 404.
    meal_time = get_object_or_404(MealTime, slug=slug)
    
    # Lọc danh sách các món ăn không phải đồ uống cho MealTime này.
    food_items = Item.objects.filter(category__is_drink=False, meal_time=meal_time)

    return render(request, 'Menu/fooddetail.html', {
        'food_menu': food_items,
        'meal_time': meal_time  # Truyền thêm meal_time để hiển thị thông tin
    })
def drinkDetail(request, slug):
    # Lấy MealTime dựa trên slug. Nếu không tìm thấy, trả về 404.
    meal_time = get_object_or_404(MealTime, slug=slug)
    
    # Lọc danh sách các món ăn không phải đồ uống cho MealTime này.
    drink_items = Item.objects.filter(category__is_drink=True, meal_time=meal_time)

    return render(request, 'Menu/drinkdetail.html', {
        'drink_menu': drink_items,
        'meal_time': meal_time  # Truyền thêm meal_time để hiển thị thông tin
    })
class AddMenu(View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'menu/add-menu.html', {
            'form': form
        })

    def post(self, request):
        form = ItemForm(request.POST, request.FILES)
        
        # Debug: In form errors nếu form không hợp lệ
        if not form.is_valid():
            print(form.errors)

        if form.is_valid():
            form.save()
            # Chuyển hướng tới trang 'food' nếu lưu thành công
            return redirect('food')  # Đảm bảo tên này tồn tại trong urls.py
        else:
            # Nếu form không hợp lệ, render lại trang thêm menu
            return render(request, 'menu/add-menu.html', {
                'form': form
            })

def updata(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None , instance=item)
    if request.method == 'GET':
        return render(request,'Menu/updata.html',{'form':form,
                                                  'item':item})
    else:
        if form.is_valid():
            form.save()
            return redirect('food')
    return render(request,'Menu/updata.html',{'form':form,
                                              'item':item})
def delete(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food')
    return render(request,'Menu/delete.html')
def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        result = []
        if query:
            result = Item.objects.filter(name__icontains=query) | Item.objects.filter(content__icontains = query)
        return render(request,'Menu/result.html',{'result':result,
                                          'query':query
                                          })                            