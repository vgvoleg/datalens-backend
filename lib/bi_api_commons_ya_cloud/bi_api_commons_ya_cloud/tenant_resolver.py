from typing import Optional

from bi_api_commons.base_models import TenantDef, TenantYCOrganization, TenantYCFolder, TenantDCProject
from bi_api_commons.tenant_resolver import TenantResolver


class TenantResolverYC(TenantResolver):
    def resolve_tenant_def_by_tenant_id(self, tenant_id_str: Optional[str]) -> TenantDef:
        if tenant_id_str is None:
            raise ValueError("Got 'None' tenant in YC tenant ID.")

        if tenant_id_str.startswith(TenantYCOrganization.tenant_id_prefix):
            return TenantYCOrganization(org_id=tenant_id_str.removeprefix(TenantYCOrganization.tenant_id_prefix))
        return TenantYCFolder(folder_id=tenant_id_str)


class TenantResolverDC(TenantResolver):
    def resolve_tenant_def_by_tenant_id(self, tenant_id_str: Optional[str]) -> TenantDef:
        if tenant_id_str is None:
            raise ValueError("Got 'None' tenant in DC tenant ID.")

        return TenantDCProject(tenant_id_str)