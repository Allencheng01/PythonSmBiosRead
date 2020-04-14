# PythonSmBiosRead
Read SMBIOS information by python

This practice is
1. Using Kernel32.dll, function GetSystemFirmwareTable to get SMBIOS information.
2. from edk2 codebase(https://github.com/tianocore/edk2) get the SMBIOS Structure.
3. Parsing Structure by ctypes.

Support OS: Windows.
Todo: Add linux support, maybe parsing the result of DMIDECODE.

Currently only parsing SMBIOS Type0 information.
