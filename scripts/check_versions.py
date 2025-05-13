import os


class VersionNotSameError(Exception):
    pass


class LoadInitFileVersionError(Exception):
    pass


class LoadPyprojectVersionError(Exception):
    pass


def get_version_from_init_file() -> str:
    with open(file='simple_mongodb/__init__.py', mode='r') as file:
        for line in file.readlines():
            if not '__version__ = ' in line:
                continue
            version: str = line.replace('__version__ = ', '').replace('\'', '')
            return version.replace('\n', '')
    raise LoadInitFileVersionError(
        '__version__ in simple_mongodb/__init__.py not found'
    )


def get_version_from_pyproject_toml() -> str:
    with open(file='pyproject.toml', mode='r') as file:
        for line in file.readlines():
            if not "version = '" in line:
                continue
            version: str = line.replace('version = ', '').replace('\'', '')
            return version.replace('\n', '')
    raise LoadPyprojectVersionError('version in pyproject.toml not found')


def main() -> None:
    init_file_version: str = get_version_from_init_file()
    pyproject_version: str = get_version_from_pyproject_toml()

    print(f'init-file-version: {init_file_version}')
    print(f'pyproject.toml-version: {pyproject_version}')

    if not init_file_version == pyproject_version:
        raise VersionNotSameError('The versions are not the same')

    if os.getenv('GITHUB_ACTIONS') == 'true':
        os.system(f'echo "PACKAGE_VERSION={pyproject_version}" >> $GITHUB_ENV')


if __name__ == '__main__':
    main()
