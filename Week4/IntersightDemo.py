#! /usr/bin/env python
from intersight.intersight_api_client import IntersightApiClient
from intersight.apis import equipment_device_summary_api

# Create an Intersight API Client instance
API_INSTANCE = IntersightApiClient(
    host="https://intersight.com/api/v1",\
    private_key="/Path_to/SecretKey.txt",\
    api_key_id="your_own_api_key_id")

# Create an equipment device handle
D_HANDLE = equipment_device_summary_api.EquipmentDeviceSummaryApi(API_INSTANCE)
DEVICES = D_HANDLE.equipment_device_summaries_get().results

print('{0:35s}{1:40s}{2:13s}{3:14s}'.format(
    "DN",
    "MODEL",
    "SERIAL",
    "OBJECT TYPE"))
print('-'*105)

# Loop through devices and extract data
for DEVICE in DEVICES:
    print('{0:35s}{1:40s}{2:13s}{3:14s}'.format(
        DEVICE.dn,
        DEVICE.model,
        DEVICE.serial,
        DEVICE.source_object_type))