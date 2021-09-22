from django.contrib import admin
from .models import (
    ClientModel,
    SpecialistsModel,
    ServiceRequestModel,
    ServiceRequestCategoryModel,
    IssueSolutionModel
)


@admin.register(ServiceRequestModel)
class ServiceRequestModelAdmin(admin.ModelAdmin):
    list_display = ('issue_title', 'issue_date_created', 'issue_customer', 'issue_category')


@admin.register(ServiceRequestCategoryModel)
class ServiceRequestCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category_name', )


@admin.register(ClientModel)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'client_name', )


@admin.register(SpecialistsModel)
class SpecialistsModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialist_last_name')


@admin.register(IssueSolutionModel)
class IssueSolutionModelAdmin(admin.ModelAdmin):
    list_display = ('issue', 'solution_description', 'solution_date', 'solution_executor')














