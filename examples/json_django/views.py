import json
import os

from django.conf import settings
from django.views.generic import TemplateView


class ReadJsonView(TemplateView):
    template_name = 'readJson.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_path = os.path.join(settings.BASE_DIR, "FMCD.json")
        try:
            with open(json_path, "r", encoding="utf-8") as file:
                context["data"] = json.load(file)
        except FileNotFoundError:
            context["data"] = []
            context["error"] = f"File not found: {json_path}"
        except json.JSONDecodeError:
            context["data"] = []
            context["error"] = "Invalid JSON format in FMCD.json"
        return context
    
class WriteJsonView(TemplateView):
    template_name = 'writeJson.html'