from pprint import pprint
from decimal import Decimal
from dateutil import parser

from django.core.management.base import BaseCommand

from flourish_child.models import ChildDataset


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str,
                            help='Data fine path, csv file')

    def handle(self, *args, **kwargs):
        already_exists = 0
        created = 0
        file_path = kwargs['file_path']
        data = self.data(file_path=file_path)

        for data_item in data:
            options = {}
            for field_name in self.all_model_fields:
                options[field_name] = data_item.get(field_name)

            # Update identifiers
            options.update(study_child_identifier=data_item.get('bid'))

            # Convert date to date objects
            try:
                infant_enrolldate = parser.parse(options.get('infant_enrolldate')).date()
            except parser.ParserError:
                options.update(infant_enrolldate=None)
            else:
                options.update(infant_enrolldate=infant_enrolldate)

            try:
                infant_randdt = parser.parse(options.get('infant_randdt')).date()
            except parser.ParserError:
                options.update(infant_randdt=None)
            else:
                options.update(infant_randdt=infant_randdt)

            try:
                infant_azt_startdate = parser.parse(options.get('infant_azt_startdate')).date()
            except parser.ParserError:
                options.update(infant_azt_startdate=None)
            else:
                options.update(infant_azt_startdate=infant_azt_startdate)

            try:
                infant_azt_stopdate = parser.parse(options.get('infant_azt_stopdate')).date()
            except parser.ParserError:
                options.update(infant_azt_stopdate=None)
            else:
                options.update(infant_azt_stopdate=infant_azt_stopdate)

            try:
                weandt = parser.parse(options.get('weandt')).date()
            except parser.ParserError:
                options.update(weandt=None)
            else:
                options.update(weandt=weandt)

            try:
                deathdt = parser.parse(options.get('deathdt')).date()
            except parser.ParserError:
                options.update(deathdt=None)
            else:
                options.update(deathdt=deathdt)

            try:
                firsthospdt = parser.parse(options.get('firsthospdt')).date()
            except parser.ParserError:
                options.update(firsthospdt=None)
            else:
                options.update(firsthospdt=firsthospdt)

            try:
                infant_offstudydate = parser.parse(options.get('infant_offstudydate')).date()
            except parser.ParserError:
                options.update(infant_offstudydate=None)
            else:
                options.update(infant_offstudydate=infant_offstudydate)

            try:
                infant_lastcontactdt = parser.parse(options.get('infant_lastcontactdt')).date()
            except parser.ParserError:
                options.update(infant_lastcontactdt=None)
            else:
                options.update(infant_lastcontactdt=infant_lastcontactdt)

            # Convert int values to int objects
            try:
                infant_azt_days = int(options.get('infant_azt_days'))
            except ValueError:
                options.update(infant_azt_days=None)
            else:
                options.update(infant_azt_days=infant_azt_days)

            try:
                infant_breastfed_days = int(options.get('infant_breastfed_days'))
            except ValueError:
                options.update(infant_breastfed_days=None)
            else:
                options.update(infant_breastfed_days=infant_breastfed_days)

            try:
                apgarscore_1min = int(options.get('apgarscore_1min'))
            except ValueError:
                options.update(apgarscore_1min=None)
            else:
                options.update(apgarscore_1min=apgarscore_1min)

            try:
                apgarscore_5min = int(options.get('apgarscore_5min'))
            except ValueError:
                options.update(apgarscore_5min=None)
            else:
                options.update(apgarscore_5min=apgarscore_5min)

            try:
                apgarscore_10min = int(options.get('apgarscore_10min'))
            except ValueError:
                options.update(apgarscore_10min=None)
            else:
                options.update(apgarscore_10min=apgarscore_10min)

            try:
                hospnum = int(options.get('hospnum'))
            except ValueError:
                options.update(hospnum=None)
            else:
                options.update(hospnum=hospnum)

            try:
                idth = int(options.get('idth'))
            except ValueError:
                options.update(idth=None)
            else:
                options.update(idth=idth)

            try:
                idth_days = int(options.get('idth_days'))
            except ValueError:
                options.update(idth_days=None)
            else:
                options.update(idth_days=idth_days)

            try:
                ihiv = int(options.get('ihiv'))
            except ValueError:
                options.update(ihiv=None)
            else:
                options.update(ihiv=ihiv)

            try:
                ihiv_days = int(options.get('ihiv_days'))
            except ValueError:
                options.update(ihiv_days=None)
            else:
                options.update(ihiv_days=ihiv_days)

            try:
                ihosp = int(options.get('ihosp'))
            except ValueError:
                options.update(ihosp=None)
            else:
                options.update(ihosp=ihosp)

            try:
                ihosp_days = int(options.get('ihosp_days'))
            except ValueError:
                options.update(ihosp_days=None)
            else:
                options.update(ihosp_days=ihosp_days)

            try:
                infant_onstudy_days = int(options.get('infant_onstudy_days'))
            except ValueError:
                options.update(infant_onstudy_days=None)
            else:
                options.update(infant_onstudy_days=infant_onstudy_days)

            # Convert decimal values to decimal objects
            if options.get('birthweight') and not options.get('birthweight') == '.':
                birthweight = Decimal(options.get('birthweight'))
                options.update(birthweight=birthweight)
            else:
                options.update(birthweight=None)

            if options.get('height_0') and not options.get('height_0') == '.':
                height_0 = Decimal(options.get('height_0'))
                options.update(height_0=height_0)
            else:
                options.update(height_0=None)

            if options.get('headcirc_0') and not options.get('headcirc_0') == '.':
                headcirc_0 = Decimal(options.get('headcirc_0'))
                options.update(headcirc_0=headcirc_0)
            else:
                options.update(headcirc_0=None)

            if options.get('height_6mo') and not options.get('height_6mo') == '.':

                height_6mo = Decimal(options.get('height_6mo'))
                options.update(height_6mo=height_6mo)
            else:
                options.update(height_6mo=None)

            if options.get('height_18mo') and not options.get('height_18mo') == '.':
                height_18mo = Decimal(options.get('height_18mo'))
                options.update(height_18mo=height_18mo)
            else:
                options.update(height_18mo=None)

            if options.get('height_24mo') and not options.get('height_24mo') == '.':
                height_24mo = Decimal(options.get('height_24mo'))
                options.update(height_24mo=height_24mo)
            else:
                options.update(height_24mo=None)

            if options.get('headcirc_18mo') and not options.get('headcirc_18mo') == '.':
                headcirc_18mo = Decimal(options.get('headcirc_18mo'))
                options.update(headcirc_18mo=headcirc_18mo)
            else:
                options.update(headcirc_18mo=None)

            if options.get('headcirc_24mo') and not options.get('headcirc_24mo') == '.':
                headcirc_24mo = Decimal(options.get('headcirc_24mo'))
                options.update(headcirc_24mo=headcirc_24mo)
            else:
                options.update(headcirc_24mo=None)

            if options.get('weight_18mo') and not options.get('weight_18mo') == '.':
                weight_18mo = Decimal(options.get('weight_18mo'))
                options.update(weight_18mo=weight_18mo)
            else:
                options.update(weight_18mo=None)

            if options.get('weight_24mo') and not options.get('weight_24mo') == '.':
                weight_24mo = Decimal(options.get('weight_24mo'))
                options.update(weight_24mo=weight_24mo)
            else:
                options.update(weight_24mo=None)

            try:
                ChildDataset.objects.get(study_child_identifier=data_item.get('bid'))
            except ChildDataset.DoesNotExist:
                ChildDataset.objects.create(**options)
                created += 1
            else:
                already_exists += 1

        self.stdout.write(self.style.SUCCESS(f'A total of {created} have been created'))
        self.stdout.write(self.style.WARNING(f'Total items {already_exists} already existed'))

    def data(self, file_path=None):
        data = []
        f = open(file_path, 'r')
        lines = f.readlines()
        header = lines[0]
        lines.pop(0)
        header = header.strip()
        header = header.split(',')
        self.stdout.write(self.style.WARNING(f'Total items {len(lines)}'))
        for line in lines:
            line = line.strip()
            line = line.split(',')
            data_item = dict(zip(header, line))
            data.append(data_item)
        return data

    @property
    def all_model_fields(self):
        """Returns a list of maternal dataset model fields.
        """
        exclude_fields = [
            'created',
            'modified',
            'user_created',
            'user_modified',
            'hostname_created',
            'hostname_modified',
            'revision',
            'device_created',
            'device_modified',
            'id',
            'site',
            'subject_identifier',
            'subject_identifier',
            'study_maternal_identifier', ]
        fields = []
        for field in ChildDataset._meta.get_fields():
            if not field.name in exclude_fields:
                fields.append(field.name)
        return fields
