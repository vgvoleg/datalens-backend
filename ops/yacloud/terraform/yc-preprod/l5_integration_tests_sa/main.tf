locals {
  env_name = "yc-preprod"
  cloud_id = "aoeal5mlfb0adjhtufd5"

  sa_data_list = [
    {
      name_suffix  = "creator",
      folder_roles = ["datalens.instances.user"]
    },
    {
      name_suffix  = "viewer-1",
      folder_roles = ["datalens.instances.user"]
    },
    {
      name_suffix  = "viewer-2",
      folder_roles = ["datalens.instances.user"]
    },
    {
      name_suffix  = "nobody",
      folder_roles = []
    },
  ]
}

module "constants" {
  source   = "../../_modules/_constants/v1"
  env_name = local.env_name
}

provider "yandex" {
  token            = var.iam_token
  cloud_id         = local.cloud_id
  folder_id        = module.constants.env_data.folder_id
  endpoint         = module.constants.env_data.cloud_api_endpoint
  storage_endpoint = module.constants.env_data.s3_endpoint
}

terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.73"

  backend "s3" {
    endpoint = "storage.cloud-preprod.yandex.net"
    bucket   = "dl-tf-state"
    region   = "us-east-1"
    key      = "datalens-integration-tests.tfstate"

    skip_region_validation      = true
    skip_credentials_validation = true
  }
}

module "service_accounts" {
  source = "../../_modules/integration_tests/service_accounts"

  cloud_id = local.cloud_id
  sa_data_list = [
    {
      name_suffix  = "creator",
      folder_roles = ["datalens.instances.user"]
    },
    {
      name_suffix  = "viewer-1",
      folder_roles = ["datalens.instances.user"]
    },
    {
      name_suffix  = "viewer-2",
      folder_roles = ["datalens.instances.user"]
    },
    {
      name_suffix  = "nobody",
      folder_roles = []
    },
  ]
}


