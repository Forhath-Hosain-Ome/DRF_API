def UploadPath(instance, filename):
    folder_name = getattr(instance, 'name', None) or getattr(instance, 'title', 'Default')
    return f'resources/{folder_name}/{filename}'