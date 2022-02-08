from django.contrib import admin

from .models import Company, PriceLookUpEvent

admin.site.register(PriceLookUpEvent)


class PriceLookUpEventAdmin(admin.TabularInline):
    model = PriceLookUpEvent
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    # inlines = [PriceLookUpEventAdmin]
    readonly_fields = ["periodic_task"]

    class Meta:
        model = Company


admin.site.register(Company, CompanyAdmin)
