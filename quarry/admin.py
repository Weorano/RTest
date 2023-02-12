from django.contrib import admin

from quarry.models import DumpTruckModels, DumpTrucks


@admin.register(DumpTruckModels)
class DumpTruckModelsAdmin(admin.ModelAdmin):
    model = DumpTruckModels


@admin.register(DumpTrucks)
class DumpTrucksAdmin(admin.ModelAdmin):
    model = DumpTrucks
    list_display = (
        'tactical_number',
        'model',
        'model_load_capacity_max',
        'current_weight',
        'overload'
    )
    list_filter = ('model',)

    @admin.display(description='Макс. грузоподъёмность')
    def model_load_capacity_max(self, obj):
        return obj.model.load_capacity_max

