from django.test import TestCase
from .models import DumpTrucks, DumpTruckModels


class DumpTrucksTest(TestCase):
    def setUp(self):
        self.model = DumpTruckModels.objects.create(name='БелАЗ', load_capacity_max=120)
        self.dump_truck = DumpTrucks.objects.create(tactical_number='Н101', model=self.model)

    def test_current_weight_less_than_load_capacity_max(self):
        self.dump_truck.current_weight = 50
        self.dump_truck.save()
        self.assertEqual(self.dump_truck.overload, 0)

    def test_current_weight_equal_to_load_capacity_max(self):
        self.dump_truck.current_weight = 120
        self.dump_truck.save()
        self.assertEqual(self.dump_truck.overload, 0)

    def test_current_weight_greater_than_load_capacity_max(self):
        self.dump_truck.current_weight = 121
        self.dump_truck.save()
        self.assertEqual(self.dump_truck.overload, 0.8)

    def test_load_capacity_max_changed(self):
        self.dump_truck.current_weight = 120
        self.dump_truck.save()
        self.assertEqual(self.dump_truck.overload, 0)

        self.model.load_capacity_max = 80
        self.model.save()
        self.dump_truck.refresh_from_db()
        self.assertEqual(self.dump_truck.overload, 50)
