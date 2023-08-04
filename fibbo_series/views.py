from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FibonacciNumber

def generate_fibonacci(request):
    if request.method == 'POST':
        n = int(request.POST.get('n', 0))

        if n <= 0:
            return HttpResponse('Invalid input. Please provide a positive integer.')

        # Fetch Fibonacci numbers from the database if already computed
        fibonacci_numbers = FibonacciNumber.objects.all().values_list('value', flat=True)

        if len(fibonacci_numbers) >= n:
            fibonacci_list = ', '.join(str(num) for num in fibonacci_numbers[:n])
        else:
            # Compute the remaining Fibonacci numbers and store them in the database
            fibonacci_numbers = compute_fibonacci(n)
            fibonacci_list = ', '.join(str(num) for num in fibonacci_numbers)

        return render(request, 'fibbo_series/fibbonaci.html', {'fibonacci_list': fibonacci_list})

    return render(request, 'fibbo_series/index.html')

def compute_fibonacci(n):
    fibonacci = [1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        # Store Fibonacci numbers in the database as they are computed
        FibonacciNumber.objects.create(value=fibonacci[-1])
    return fibonacci

