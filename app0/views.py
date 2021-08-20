from django.shortcuts import render
from django.http import JsonResponse, Http404


def handler404(request, *args, **kwargs):
    return JsonResponse({
        'success': False,
        "message": "not found",
        "data": None
    }, status=404)


def handler500(request, *args, **kwargs):
    return JsonResponse({
        'success': False,
        "message": "some error in server",
        "data": None
    }, status=500)


def raise_404_view(request):
    raise Http404("not exist")


def raise_500_view(request):
    _ = request.test()
