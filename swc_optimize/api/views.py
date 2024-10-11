import json

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import fetch_monster_data
from django.views.generic import TemplateView
from .models import Rune

@api_view(['GET'])
def get_routes(request):
    return Response({'message': 'Hello, world!'})

@api_view(['GET'])
def get_monsters(request):
    page = request.query_params.get('page', 1)
    data = fetch_monster_data()
    return Response(data)

@api_view(['GET'])
def get_monster_detail(request, monster_id):
    data = fetch_monster_data(monster_id)
    return Response(data)


class HomePageView(TemplateView):
    template_name = 'home.html'


@api_view(['GET', 'POST'])
def rune_interface(request):
    if request.method == 'POST':
        json_file = request.FILES.get('json_file')
        if json_file:
            data = json_file.read().decode('utf-8')
            try:
                parsed_data = json.loads(data)
                # Handle different JSON structures
                if 'runes' in parsed_data:
                    rune_data_list = parsed_data['runes']
                elif isinstance(parsed_data, list):
                    rune_data_list = parsed_data
                elif isinstance(parsed_data, dict):
                    rune_data_list = [parsed_data]
                else:
                    return Response("Invalid JSON structure.", status=400)

                for rune_data_item in rune_data_list:
                    rune_id = rune_data_item.get('rune_id')
                    # Save or update rune data
                    Rune.objects.update_or_create(
                        rune_id=rune_id,
                        defaults={
                            'wizard_id': rune_data_item.get('wizard_id'),
                            'occupied_type': rune_data_item.get('occupied_type'),
                            'occupied_id': rune_data_item.get('occupied_id'),
                            'slot_no': rune_data_item.get('slot_no'),
                            'rank': rune_data_item.get('rank'),
                            'rune_class': rune_data_item.get('class'),
                            'set_id': rune_data_item.get('set_id'),
                            'upgrade_limit': rune_data_item.get('upgrade_limit'),
                            'upgrade_curr': rune_data_item.get('upgrade_curr'),
                            'base_value': rune_data_item.get('base_value'),
                            'sell_value': rune_data_item.get('sell_value'),
                            'pri_eff': rune_data_item.get('pri_eff'),
                            'prefix_eff': rune_data_item.get('prefix_eff'),
                            'sec_eff': rune_data_item.get('sec_eff'),
                            'extra': rune_data_item.get('extra'),
                        }
                    )
                return redirect('rune_interface')
            except json.JSONDecodeError:
                return Response("Invalid JSON file.", status=400)
        else:
            return Response("No file uploaded.", status=400)
    else:
        # Display runes
        runes = Rune.objects.all()
        context = {'runes': runes}
        return render(request, 'rune_interface.html', context)
