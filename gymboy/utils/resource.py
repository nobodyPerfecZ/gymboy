from importlib import resources


def resource_path(resource: str) -> str:
    """
    Returns the complete resourcce path within the package.

    Args:
        resource (str):
            The relative path to the resource within the package

    Returns:
        str:
            The complete path to the resource
    """
    with resources.as_file(resources.files("gymboy").joinpath(resource)) as path:
        path = str(path)
    return path
