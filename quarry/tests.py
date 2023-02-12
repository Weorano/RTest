from django.test import TestCase
from .models import DumpTrucks, DumpTruckModels


class DumpTrucksTest(TestCase):

    def test_save_method(self):
        model = DumpTruckModels.objects.create(
            name='БелАЗ',
            load_capacity_max=120
        )

        dump_truck = DumpTrucks.objects.create(
            tactical_number='102',
            model=model,
            current_weight=126,
        )

        self.assertEqual(dump_truck.overload, 5)

        dump_truck.current_weight = 150
        dump_truck.save()

        self.assertEqual(dump_truck.overload, 25)

        dump_truck2 = DumpTrucks.objects.create(
            tactical_number='К104',
            model=model,
            current_weight=None,
        )

        self.assertIsNone(dump_truck2.overload)
