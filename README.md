Do not use in production.

This is a copy of isi-sdk-8-1-1, but I ran it through these commands in a feeble attempt to support python3.7

This is a temporary solution until https://github.com/Isilon/isilon_sdk_python/issues/9 is resolved.

    find path/ -type f -exec sed -i 's/async=params.get/is_async=params.get/g' {} +
    find path/ -type f -exec sed -i 's/async=None/is_async=None/g' {} +
    find path/ -type f -exec sed -i 's/if not async/if not is_async/g' {} +
