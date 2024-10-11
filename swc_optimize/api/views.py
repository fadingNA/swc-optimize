import json

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .utils import fetch_monster_data
from django.views.generic import TemplateView
from .models import Rune
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import RuneSelectionForm

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
                    return HttpResponse("Invalid JSON structure.", status=400)

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
                return HttpResponse("Invalid JSON file.", status=400)
        else:
            return HttpResponse("No file uploaded.", status=400)
    else:
        # Display runes
        runes = Rune.objects.all()
        context = {'runes': runes}
        return render(request, 'rune_interface.html', context)
    
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
@login_required
@require_http_methods(["POST"])
def rune_delete(request):
    try:
        runes = Rune.objects.all()
        runes.delete()
        return redirect('rune_interface')
    except Exception as e:
        return HttpResponse(f"Error deleting runes: {e}", status=400)
        

def rune_optimize(request):
    if request.method == 'POST':
        # Handle rune selection
        form = RuneSelectionForm(request.POST)
        if form.is_valid():
            rune_set_id = form.cleaned_data['rune_set']
            selected_rune_ids = [
                form.cleaned_data.get(f'slot_{slot}') for slot in range(1, 7)
            ]
            # Save selected runes in session or database as needed
            request.session['selected_runes'] = selected_rune_ids
    else:
        form = RuneSelectionForm()

    rune_sets = Rune.objects.values_list('set_id', flat=True).distinct()
    rune_set_choices = {set_id: Rune.RUNE_SET_CHOICES.get(set_id, 'Unknown') for set_id in rune_sets}

    context = {
        'form': form,
        'rune_sets': rune_set_choices,
    }
    return render(request, 'rune_optimize.html', context)

def get_runes_by_set(request):
    set_id = request.GET.get('set_id')
    runes = Rune.objects.filter(set_id=set_id)
    rune_data = {}
    for slot in range(1, 7):
        slot_runes = runes.filter(slot_no=slot)
        rune_data[f'slot_{slot}'] = [
            {
                'id': rune.rune_id,
                'description': f'Rune {rune.rune_id} (+{rune.upgrade_curr})',
            }
            for rune in slot_runes
        ]
    return JsonResponse(rune_data)

@csrf_exempt
def chat_with_optimizer(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        selected_rune_ids = request.session.get('selected_runes', [])
        selected_runes = Rune.objects.filter(rune_id__in=selected_rune_ids)

        # Prepare context using selected runes
        context = "Selected Runes:\n"
        for rune in selected_runes:
            context += f"Slot {rune.slot_no}: {rune.get_set_name()} {rune.get_primary_effect()} with sub-stats {', '.join(rune.get_secondary_effects())}\n"

        # Process the message with the LLM
        # reply = process_query_with_context(message, context)

        # For demonstration, we'll use a placeholder reply
        reply = f"Processed your query with the following context:\n{context}"

        return JsonResponse({'reply': reply})
    else:
        return JsonResponse({'reply': 'Invalid request.'})