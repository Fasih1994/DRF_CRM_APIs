from django_filters import rest_framework as filters, CharFilter, DateFilter, NumberFilter
from manifest.models.MANIFEST import XxyhImsWsManifestLns

class XxyhImsWsManifestHdrFilterSet(filters.FilterSet):

	#Header Filters
	#Number filters
	manifest_id = NumberFilter(lookup_expr='exact', field_name='manifest_id')
	group_id = NumberFilter(lookup_expr='exact', field_name='group_id')

	#Char Filters
	manifest_name = CharFilter(lookup_expr='exact', field_name='manifest_name')
	from_organization_code = CharFilter(lookup_expr='iexact', field_name='from_organization_code')
	to_organization_code = CharFilter(lookup_expr='iexact', field_name='to_organization_code')
	airway_bill = CharFilter(lookup_expr='exact', field_name='airway_bill')
	user_name = CharFilter(lookup_expr='iexact', field_name='user_name')

	#Date Filters
	actual_ship_date_gte = DateFilter(lookup_expr='gte', field_name='actual_ship_date')
	actual_ship_date_gt = DateFilter(lookup_expr='gt', field_name='actual_ship_date')
	actual_ship_date_lt = DateFilter(lookup_expr='lt', field_name='actual_ship_date')
	actual_ship_date_lte = DateFilter(lookup_expr='lte', field_name='actual_ship_date')
	actual_ship_date = DateFilter(lookup_expr='exact', field_name='actual_ship_date')

	estimated_ship_date = DateFilter(lookup_expr='exact', field_name='estimated_ship_date')
	estimated_ship_date_gt = DateFilter(lookup_expr='gt', field_name='estimated_ship_date')
	estimated_ship_date_gte = DateFilter(lookup_expr='gte', field_name='estimated_ship_date')
	estimated_ship_date_lt = DateFilter(lookup_expr='lt', field_name='estimated_ship_date')
	estimated_ship_date_lte = DateFilter(lookup_expr='lte', field_name='estimated_ship_date')

	#Line Filters
	#Char Filters
	ia_ticket_numbers = CharFilter(method='get_parent_ids_from_child')
	site_name = CharFilter(method='get_parent_ids_from_child')
	item_number = CharFilter(method='get_parent_ids_from_child')
	shipment_number = CharFilter(method='get_parent_ids_from_child')


	def get_parent_ids_from_child(self, queryset, key, value):
		kwargs = {}
		try:
			if key == 'ia_ticket_numbers':
				kwargs['ia_ticket_numbers__contains']: value
			elif key == 'site_name':
				kwargs['site_name']: value
			elif key == 'item_number':
				kwargs['item_number']: value
			elif key == 'shipment_number':
				kwargs['shipment_number']: value

			manifest_id_list = XxyhImsWsManifestLns.objects.filter(**kwargs).values_list('manifest_id', flat=True)
			return queryset.filter(manifest_id__in=manifest_id_list)
		except:
			return queryset




class XxyhImsWsManifestLnsFilterSet(filters.FilterSet):

    manifest_line_id = NumberFilter(lookup_expr='exact', field_name='manifest_line_id')
    manifest_id = NumberFilter(lookup_expr='exact', field_name='manifest_id')
    manifest_name = CharFilter(lookup_expr='exact', field_name='manifest_name')
    from_organization_code = CharFilter(lookup_expr='exact', field_name='from_organization_code')
    to_organization_code = CharFilter(lookup_expr='exact', field_name='to_organization_code')
    pallet = CharFilter(lookup_expr='exact', field_name='pallet')
    ia_ticket_numbers = CharFilter(lookup_expr='exact', field_name='ia_ticket_numbers')
    site_name = CharFilter(lookup_expr='exact', field_name='site_name')
    inventory_item_id = NumberFilter(lookup_expr='exact', field_name='inventory_item_id')
    item_number = CharFilter(lookup_expr='exact', field_name='item_number')
    item_description = CharFilter(lookup_expr='exact', field_name='item_description')
    quantity = NumberFilter(lookup_expr='exact', field_name='quantity')
    shipment_header_id = NumberFilter(lookup_expr='exact', field_name='shipment_header_id')
    shipment_number = CharFilter(lookup_expr='exact', field_name='shipment_number')
    shipment_line_id = NumberFilter(lookup_expr='exact', field_name='shipment_line_id')
    requisition_number = CharFilter(lookup_expr='exact', field_name='requisition_number')
    requisition_header_id = NumberFilter(lookup_expr='exact', field_name='requisition_header_id')
    order_number = NumberFilter(lookup_expr='exact', field_name='order_number')
    order_header_id = NumberFilter(lookup_expr='exact', field_name='order_header_id')
    order_line_id = NumberFilter(lookup_expr='exact', field_name='order_line_id')
    job_id = NumberFilter(lookup_expr='exact', field_name='job_id')
    job_name = CharFilter(lookup_expr='exact', field_name='job_name')
    jira = CharFilter(lookup_expr='exact', field_name='jira')
    gscc = CharFilter(lookup_expr='exact', field_name='gscc')
    width = NumberFilter(lookup_expr='exact', field_name='width')
    length = NumberFilter(lookup_expr='exact', field_name='length')
    height = NumberFilter(lookup_expr='exact', field_name='height')
    weight = NumberFilter(lookup_expr='exact', field_name='weight')
    process_status = CharFilter(lookup_expr='exact', field_name='process_status')
    group_name = CharFilter(lookup_expr='exact', field_name='group_name')
    group_id = NumberFilter(lookup_expr='exact', field_name='group_id')
    source_system = CharFilter(lookup_expr='exact', field_name='source_system')
    error_fields = CharFilter(lookup_expr='exact', field_name='error_fields')
    error_code = CharFilter(lookup_expr='exact', field_name='error_code')
    error_message = CharFilter(lookup_expr='exact', field_name='error_message')
    user_name = CharFilter(lookup_expr='exact', field_name='user_name')
    user_id = NumberFilter(lookup_expr='exact', field_name='user_id')

    email_date = DateFilter(lookup_expr='exact', field_name='email_date')
    email_date_gt = DateFilter(lookup_expr='gt', field_name='email_date')
    email_date_lt = DateFilter(lookup_expr='lt', field_name='email_date')
    email_date_gte = DateFilter(lookup_expr='gte', field_name='email_date')
    email_date_lte = DateFilter(lookup_expr='lte', field_name='email_date')

    creation_date = DateFilter(lookup_expr='exact', field_name='creation_date')
    creation_date_gt = DateFilter(lookup_expr='gt', field_name='creation_date')
    creation_date_lt = DateFilter(lookup_expr='lt', field_name='creation_date')
    creation_date_lte = DateFilter(lookup_expr='gte', field_name='creation_date')
    creation_date_gte = DateFilter(lookup_expr='lte', field_name='creation_date')

    last_update_date = DateFilter(lookup_expr='exact', field_name='last_update_date')
    last_update_date_gt = DateFilter(lookup_expr='gt', field_name='last_update_date')
    last_update_date_lt = DateFilter(lookup_expr='lt', field_name='last_update_date')
    last_update_date_gte = DateFilter(lookup_expr='gte', field_name='last_update_date')
    last_update_date_lte = DateFilter(lookup_expr='lte', field_name='last_update_date')