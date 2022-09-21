import imp
from django.db import models
from utils.db_utils.common import set_sql_for_field
from django.conf import settings
from django.utils import timezone
from django.db.models.constraints import UniqueConstraint
from django.db.models import Q 


class XxyhImsWsManifestHdr(models.Model):
    STATUS_CHOICES = (('CREATED', "CREATED"), ('UPDATED', "UPDATED"), ('CLOSED', "CLOSED"))
    manifest_id = models.IntegerField(primary_key=True, null=True)
    manifest_name = models.CharField(max_length=150)
    from_organization_id = models.IntegerField(blank=True, null=True)
    from_organization_code = models.CharField(max_length=3, blank=True, null=True)
    to_organization_id = models.IntegerField(blank=True, null=True)
    to_organization_code = models.CharField(max_length=3, blank=True, null=True)
    estimated_ship_date = models.DateField(blank=True, null=True)
    actual_ship_date = models.DateTimeField(blank=True, null=True)
    airway_bill = models.CharField(max_length=150, blank=True, null=True)
    seal = models.CharField(max_length=150, blank=True, null=True)
    ship_to_name = models.CharField(max_length=255, blank=True, null=True)
    ship_from_name = models.CharField(max_length=255, blank=True, null=True)
    process_status = models.CharField(max_length=30, blank=True, null=False, choices=STATUS_CHOICES)
    group_name = models.CharField(max_length=150, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    source_system = models.CharField(max_length=150, blank=True, null=True)
    error_fields = models.CharField(max_length=4000, blank=True, null=True)
    error_code = models.CharField(max_length=150, blank=True, null=True)
    error_message = models.CharField(max_length=4000, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True )
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'XXYH_IMS_WS_MANIFEST_HDR'
        ordering = ['manifest_id']
        constraints = [
            UniqueConstraint(
                fields=['from_organization_code', 'to_organization_code','process_status', 'airway_bill'], 
                name='unique_with_airway_bill'),
            UniqueConstraint(
                fields=['from_organization_code', 'to_organization_code','process_status'],
                condition=Q(airway_bill=None), 
                name='unique_without_airway_bill')
        ]

    @set_sql_for_field('manifest_id', f'select {settings.DB_USER}.XXYH_IMS_WS_MANIFEST_ID_S.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class XxyhImsWsManifestLns(models.Model):
    manifest_line_id = models.IntegerField(primary_key=True, null=True)
    manifest_id = models.IntegerField(blank=True, null=True)
    manifest_name = models.CharField(max_length=150, blank=True, null=True)
    from_organization_code = models.CharField(max_length=3, blank=True, null=True)
    to_organization_code = models.CharField(max_length=3, blank=True, null=True)
    pallet = models.CharField(max_length=100, blank=True, null=True)
    ia_ticket_numbers = models.CharField(max_length=150, blank=True, null=True)
    site_name = models.CharField(max_length=150, blank=True, null=True)
    email_date = models.DateTimeField(blank=True, null=True)
    inventory_item_id = models.IntegerField(blank=True, null=True)
    item_number = models.CharField(max_length=40, blank=True, null=True)
    item_description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    shipment_header_id = models.IntegerField(blank=True, null=True)
    shipment_number = models.CharField(max_length=30, blank=True, null=True)
    shipment_line_id = models.IntegerField(blank=True, null=True)
    requisition_number = models.CharField(max_length=40, blank=True, null=True)
    requisition_header_id = models.IntegerField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    order_header_id = models.IntegerField(blank=True, null=True)
    order_line_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=240, blank=True, null=True)
    jira = models.CharField(max_length=150, blank=True, null=True)
    gscc = models.CharField(max_length=150, blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    process_status = models.CharField(max_length=30, blank=True, null=True)
    group_name = models.CharField(max_length=150, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    source_system = models.CharField(max_length=150, blank=True, null=True)
    error_fields = models.CharField(max_length=4000, blank=True, null=True)
    error_code = models.CharField(max_length=150, blank=True, null=True)
    error_message = models.CharField(max_length=4000, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'XXYH_IMS_WS_MANIFEST_LNS'
        ordering = ['manifest_line_id']
        

    @set_sql_for_field('manifest_line_id', f'select {settings.DB_USER}.XXYH_IMS_WS_MANIFEST_LINE_ID_S.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class XxyhJobs(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_name = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'XXYH_JOBS'