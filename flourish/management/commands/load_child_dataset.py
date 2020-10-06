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
                infant_sex = parser.parse(options.get('infant_sex'))
            except parser.ParserError:
                options.update(infant_sex=None)
            else:
                options.update(infant_sex=infant_sex)

            try:
                infant_azt_birth = parser.parse(options.get('infant_azt_birth'))
            except parser.ParserError:
                options.update(infant_azt_birth=None)
            else:
                options.update(infant_azt_birth=infant_azt_birth)

            try:
                infant_sdnvp_birth = parser.parse(options.get('infant_sdnvp_birth'))
            except parser.ParserError:
                options.update(infant_sdnvp_birth=None)
            else:
                options.update(infant_sdnvp_birth=infant_sdnvp_birth)

            try:
                infant_hiv_exposed = parser.parse(options.get('infant_hiv_exposed'))
            except parser.ParserError:
                options.update(infant_hiv_exposed=None)
            else:
                options.update(infant_hiv_exposed=infant_hiv_exposed)

            try:
                infant_hiv_status = parser.parse(options.get('infant_hiv_status'))
            except parser.ParserError:
                options.update(infant_hiv_status=None)
            else:
                options.update(infant_hiv_status=infant_hiv_status)

            try:
                infant_breastfed = parser.parse(options.get('infant_breastfed'))
            except parser.ParserError:
                options.update(infant_breastfed=None)
            else:
                options.update(infant_breastfed=infant_breastfed)

            try:
                weaned = parser.parse(options.get('weaned'))
            except parser.ParserError:
                options.update(weaned=None)
            else:
                options.update(weaned=weaned)

            try:
                weancat = parser.parse(options.get('weancat'))
            except parser.ParserError:
                options.update(weancat=None)
            else:
                options.update(weancat=weancat)

            try:
                birthwtcat = parser.parse(options.get('birthwtcat'))
            except parser.ParserError:
                options.update(birthwtcat=None)
            else:
                options.update(birthwtcat=birthwtcat)

            try:
                low_birthweight = parser.parse(options.get('low_birthweight'))
            except parser.ParserError:
                options.update(low_birthweight=None)
            else:
                options.update(low_birthweight=low_birthweight)

            try:
                infant_premature = parser.parse(options.get('infant_premature'))
            except parser.ParserError:
                options.update(infant_premature=None)
            else:
                options.update(infant_premature=infant_premature)

            try:
                infant_vitalstatus_final = parser.parse(options.get('infant_vitalstatus_final'))
            except parser.ParserError:
                options.update(infant_vitalstatus_final=None)
            else:
                options.update(infant_vitalstatus_final=infant_vitalstatus_final)

            try:
                deathcause = parser.parse(options.get('deathcause'))
            except parser.ParserError:
                options.update(deathcause=None)
            else:
                options.update(deathcause=deathcause)

            try:
                infantvacc_bcg = parser.parse(options.get('infantvacc_bcg'))
            except parser.ParserError:
                options.update(infantvacc_bcg=None)
            else:
                options.update(infantvacc_bcg=infantvacc_bcg)

            try:
                infantvacc_dtap = parser.parse(options.get('infantvacc_dtap'))
            except parser.ParserError:
                options.update(infantvacc_dtap=None)
            else:
                options.update(infantvacc_dtap=infantvacc_dtap)

            try:
                infantvacc_hbv = parser.parse(options.get('infantvacc_hbv'))
            except parser.ParserError:
                options.update(infantvacc_hbv=None)
            else:
                options.update(infantvacc_hbv=infantvacc_hbv)

            try:
                infantvacc_hiv = parser.parse(options.get('infantvacc_hiv'))
            except parser.ParserError:
                options.update(infantvacc_hiv=None)
            else:
                options.update(infantvacc_hiv=infantvacc_hiv)

            try:
                infantvacc_measles = parser.parse(options.get('infantvacc_measles'))
            except parser.ParserError:
                options.update(infantvacc_measles=None)
            else:
                options.update(infantvacc_measles=infantvacc_measles)

            try:
                infantvacc_mmr = parser.parse(options.get('infantvacc_mmr'))
            except parser.ParserError:
                options.update(infantvacc_mmr=None)
            else:
                options.update(infantvacc_mmr=infantvacc_mmr)

            try:
                infantvacc_pneum = parser.parse(options.get('infantvacc_pneum'))
            except parser.ParserError:
                options.update(infantvacc_pneum=None)
            else:
                options.update(infantvacc_pneum=infantvacc_pneum)

            try:
                infantvacc_polio = parser.parse(options.get('infantvacc_polio'))
            except parser.ParserError:
                options.update(infantvacc_polio=None)
            else:
                options.update(infantvacc_polio=infantvacc_polio)

            try:
                infantvacc_rota = parser.parse(options.get('infantvacc_rota'))
            except parser.ParserError:
                options.update(infantvacc_rota=None)
            else:
                options.update(infantvacc_rota=infantvacc_rota)

            try:
                infant_offstudy_reason = parser.parse(options.get('infant_offstudy_reason'))
            except parser.ParserError:
                options.update(infant_offstudy_reason=None)
            else:
                options.update(infant_offstudy_reason=infant_offstudy_reason)

            try:
                ChildDataset.objects.get()
            except ChildDataset.DoesNotExist:
                ChildDataset.objects.create(**options)
                created += 1
            else:
                already_exists += 1

        self.stdout.write(self.style.SUCCESS(f'A total of {created} have been creeated'))
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
            'screening_identifier', ]
        fields = []
        for field in ChildDataset._meta.get_fields():
            if not field.name in exclude_fields:
                fields.append(field.name)
        return fields
