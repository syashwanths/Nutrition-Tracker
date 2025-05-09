from django.shortcuts import render,get_object_or_404,redirect
from Nutritionapp.models import FoodData,TrackerData
from Nutritionapp.forms import FoodForm
from django.db.models import Sum

# Create your views here.
def food_list(request):
    foods = FoodData.objects.all()
    return render(request,"food_list.html",{"foods" : foods})

def food_detail(request,id=0):
    details = get_object_or_404(FoodData,id = id)
    return render(request,"food_detail.html",{"details" : details})


def caloriTracker(request):
    foods = FoodData.objects.all()  
    calorie_entries = TrackerData.objects.all()  
    form = FoodForm()

    # Calculate total values
    totals = calorie_entries.aggregate(
        total_calories=Sum('calories'),
        total_proteins=Sum('proteins'),
        total_fat=Sum('fat'),
        total_carbohydrates=Sum('carbohydrates'),
    )

    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database
            return redirect('calorie_tracker')

    return render(request, 'tracker.html', {
        'foods': foods, 
        'calorie_entries': calorie_entries, 
        'form': form,
        'totals': totals  # Pass total values to the template
    })
