from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'stazwappaz001' # Must be replaced by your <storage_account_name>
    account_key = 'LHepEX6bNVgegZiHQN46pl8YjGCQqemhsRAkbrr3cpzVAdKBrbxt3JVac2dJWzcgdVjCNbQqKU46zIiErPpdYg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'stazwappaz001' # Must be replaced by your storage_account_name
    account_key = 'LHepEX6bNVgegZiHQN46pl8YjGCQqemhsRAkbrr3cpzVAdKBrbxt3JVac2dJWzcgdVjCNbQqKU46zIiErPpdYg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
