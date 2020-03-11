from django.contrib import admin
from .models import Alert,Dropdown_loss_category, Dropdown_activity, Dropdown_status, Dropdown_by_root_cause, Dropdown_Category_root_cause_tag, Exception_By_Category
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.site_header = "ECOBANK IS COMPLIANCE"
admin.site.site_title = "ECOBANK IS COMPLIANCE"
admin.site.index_title = "Acl Alerts"

@admin.register(Alert)
class AclAdmin(ImportExportModelAdmin):
    list_display = ['Account_Name','Acccount_Number','Exception_Category','Affiliate_Code','Affiliate_Name','Initiating_Branch','Date_Discovered','Amount_Involved_LCY']
    list_filter = ['statusCheck','camtDecision','Status_REGULARIZED_UNREGULARIZED','Exception_By_Category_Type','Affiliate_Code','Date_Discovered']
    search_fields = ['Exception_Category','Affiliate_Code','Date_Discovered','id']

admin.site.register(Dropdown_loss_category)
admin.site.register(Dropdown_activity)
admin.site.register(Dropdown_by_root_cause)
admin.site.register(Dropdown_Category_root_cause_tag)
admin.site.register(Dropdown_status)
admin.site.register(Exception_By_Category)
